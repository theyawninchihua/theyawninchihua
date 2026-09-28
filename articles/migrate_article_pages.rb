require 'nokogiri'
require 'yaml'
require 'json'

ROOT = File.expand_path(__dir__)
ARTICLE_DIRS = Dir.glob(File.join(ROOT, '*')).select { |path| File.directory?(path) && File.file?(File.join(path, 'metadata.yaml')) }.sort

def normalize_text(text)
  text.gsub(/[\t\r\n ]+/, ' ')
      .gsub(/\s+([,.;:!?])/,'\1')
end

BLOCK_NAMES = %w[h1 h2 h3 h4 h5 h6 p div center blockquote section table ul ol iframe].freeze

def markdown_inline(node)
  return normalize_text(node.text) if node.text?
  return '' unless node.element?

  name = node.name.downcase
  return '' if %w[script style input].include?(name)
  return "\n\n" if name == 'br'
  return "![#{node['alt'] || 'Image'}](#{node['src']})" if name == 'img'
  if name == 'iframe'
    src = node['src']
    return src ? %(<iframe width="#{node['width'] || 560}" height="#{node['height'] || 315}" src="#{src}" title="Embedded video" allowfullscreen></iframe>) : ''
  end
  return markdown_table(node) if name == 'table'
  return markdown_list(node, 0) if %w[ul ol].include?(name)
  return markdown_comparison(node) if name == 'center' && node.at_css('input#sliderControl')
  return markdown_nodes(node.children) if %w[font center div p blockquote section a].include?(name) && node.element_children.any? { |child| BLOCK_NAMES.include?(child.name.downcase) || child.at_css('table, ul, ol, iframe, input#sliderControl') }

  inner = node.children.map { |child| markdown_inline(child) }.join
  inner = inner.strip if %w[b strong i em].include?(name)
  case name
  when 'h1' then "# #{inner}\n\n"
  when 'h2' then "## #{inner}\n\n"
  when 'h3' then "### #{inner}\n\n"
  when 'h4', 'h5', 'h6' then "#### #{inner}\n\n"
  when 'b', 'strong' then "**#{inner}**"
  when 'i', 'em' then "*#{inner}*"
  when 'a'
    href = node['href']
    href && !href.empty? ? "[#{inner}](#{href})" : inner
  when 'font'
    color = node['color']
    color ? %(<span style="color: #{color};">#{inner}</span>) : inner
  when 'li' then inner.strip
  else inner
  end
end

def markdown_nodes(nodes)
  output = []
  inline_nodes = []
  flush_inline = lambda do
    unless inline_nodes.empty?
      text = inline_nodes.map { |node| markdown_inline(node) }.join
      text = text.gsub(/[\t\r\n ]+/, ' ').strip
      output << text unless text.empty?
      inline_nodes.clear
    end
  end

  nodes.each do |node|
    if node.element? && node.name.downcase == 'script'
      next
    elsif node.element? && node.name.downcase == 'br'
      flush_inline.call
    elsif node.element? && node.name.downcase == 'center' && node.at_css('input#sliderControl')
      flush_inline.call
      output << markdown_comparison(node)
    elsif node.element? && BLOCK_NAMES.include?(node.name.downcase)
      flush_inline.call
      rendered = case node.name.downcase
      when 'table' then markdown_table(node)
      when 'ul', 'ol' then markdown_list(node, 0)
      when 'center', 'div', 'p', 'blockquote', 'section' then markdown_nodes(node.children)
      when 'iframe' then markdown_inline(node)
      else markdown_inline(node)
      end
      output << rendered unless rendered.to_s.strip.empty?
    elsif node.element? && %w[font a].include?(node.name.downcase) && node.element_children.any? { |child| BLOCK_NAMES.include?(child.name.downcase) || child.at_css('table, ul, ol, iframe, input#sliderControl') }
      flush_inline.call
      output << markdown_nodes(node.children)
    else
      inline_nodes << node
    end
  end
  flush_inline.call
  output.join("\n\n").gsub(/[\t ]+\n/, "\n").gsub(/\n{3,}/, "\n\n").strip
end

def markdown_list(list, depth)
  list.element_children.select { |child| child.name.downcase == 'li' }.map do |item|
    nested = item.element_children.select { |child| %w[ul ol].include?(child.name.downcase) }
    nested.each(&:remove)
    content = markdown_nodes(item.children.reject { |child| nested.include?(child) }).strip
    prefix = '  ' * depth + (list.name.downcase == 'ol' ? '1. ' : '- ')
    rendered = "#{prefix}#{content.gsub("\n", "\n#{'  ' * depth}  ")}"
    nested.each { |child| rendered += "\n#{markdown_list(child, depth + 1)}" }
    rendered
  end.join("\n") + "\n\n"
end

def markdown_table(table)
  lines = []
  ordinary_rows = []
  flush = lambda do
    unless ordinary_rows.empty?
      count = ordinary_rows.map(&:length).max
      ordinary_rows.each { |row| row.concat(Array.new(count - row.length, '')) }
      lines << '| ' + ordinary_rows.first.join(' | ') + ' |'
      lines << '| ' + Array.new(count, '---').join(' | ') + ' |'
      ordinary_rows.drop(1).each { |row| lines << '| ' + row.join(' | ') + ' |' }
      ordinary_rows.clear
    end
  end

  table.css('tr').each do |row|
    cells = row.css('th, td').reject { |cell| cell.ancestors('table').first != table }
    next if cells.empty?
    if cells.any? { |cell| (cell['colspan'] || '1').to_i > 1 }
      flush.call
      heading_cell = cells.find { |cell| !cell.text.strip.empty? }
      heading_node = heading_cell&.at_css('h1, h2, h3, h4, h5, h6')
      if heading_node
        heading = markdown_nodes(heading_node.children).strip
        lines << "## #{heading}" unless heading.empty?
      else
        heading = cells.map { |cell| markdown_nodes(cell.children).strip }.reject(&:empty?).join(' ')
        lines << "**#{heading.gsub(/\*\*/, '')}**" unless heading.empty?
      end
    else
      ordinary_rows << cells.map { |cell| markdown_inline(cell).strip.gsub(/\s*\n\s*/, ' ') }
    end
  end
  flush.call
  "\n\n#{lines.join("\n")}\n\n"
end

def markdown_comparison(container)
  images = container.css('img').map { |image| [image['src'], image['alt']] }
  india = images.find { |src, alt| src.match?(/_IN_/) || alt.to_s.match?(/India/i) }
  other = images.find { |src, alt| src.match?(/_EU_/) || alt.to_s.match?(/Euro|UK/i) }
  return '' unless india && other

  caption = container.at_css('font')&.text.to_s.gsub(/\s+/, ' ').strip
  caption = caption.sub(/\ASLIDE TO COMPARE:\s*/i, 'Comparison: ')
  "\n\n| India-spec | International-spec |\n| --- | --- |\n| ![#{india[1]}](#{india[0]}) | ![#{other[1]}](#{other[0]}) |\n\n#{caption.empty? ? '' : "*#{caption}*\n\n"}"
end

def article_content(html_path)
  doc = Nokogiri::HTML(File.read(html_path, encoding: 'UTF-8'))
  body = doc.at_css('body')
  category = body.at_css('h3')
  title_node = doc.at_css('body h1')
  raise "Missing category/title in #{html_path}" unless category && title_node

  title = title_node.text.gsub(/[\t\r\n ]+/, ' ').strip
  date_node = title_node.xpath('following-sibling::b[1]').first
  date = date_node&.text.to_s.strip
  content = ["---\nlayout: default\ntitle: #{title.to_json}\n---", '', "# #{markdown_inline(title_node).strip.sub(/^#\s*/, '')}"]
  content << "**#{date}**" unless date.empty?

  banner = doc.at_css('body img[src="banner.png"]')
  content << "![Banner](banner.png)" if banner

  stop_link = body.css('a').find { |link| link['href'] == '../index.html' && link.text.strip.include?('articles') }
  article_root = title_node.ancestors('font').find { |font| font.parent == body }
  raise "Missing article body container in #{html_path}" unless article_root
  body_nodes = []
  start_node = banner || date_node
  if start_node.parent == article_root
    body_nodes.concat(start_node.xpath('following-sibling::node()').to_a)
  else
    body_nodes.concat(article_root.children.drop_while { |child| child != start_node }.drop(1))
  end
  sibling = article_root.next_sibling
  while sibling
    break if sibling == stop_link
    body_nodes << sibling
    sibling = sibling.next_sibling
  end
  body_nodes.reject! { |node| node == stop_link || node == category || node == title_node || node == date_node || node == banner }
  content << markdown_nodes(body_nodes)

  body = content.join("\n\n")
  body = body.gsub(/[ \t]+\n/, "\n").gsub(/\n{3,}/, "\n\n").strip
  body + "\n\n[click to go back to articles](../index.html)\n"
end

def page_paths
  ARTICLE_DIRS.flat_map do |directory|
    html = File.join(directory, 'index.html')
    File.file?(html) ? [html] : []
  end
end

paths = page_paths
abort 'No article index.html pages found.' if paths.empty?

if ARGV.first == '--preview'
  target = ARGV[1] || paths.first
  puts article_content(target)
elsif ARGV.first == '--check'
  paths.each { |path| article_content(path) }
  puts "Parsed #{paths.length} article pages successfully."
else
  outputs = paths.to_h { |path| [path, article_content(path)] }
  destinations = paths.flat_map do |path|
    directory = File.dirname(path)
    [File.join(directory, 'index.md'), File.join(directory, 'indexy.html')]
  end
  collisions = destinations.select { |path| File.exist?(path) }
  abort "Refusing to overwrite existing destinations:\n#{collisions.join("\n")}" unless collisions.empty?

  outputs.each do |html, markdown|
    File.write(File.join(File.dirname(html), 'index.md'), markdown, encoding: 'UTF-8')
  end
  paths.each do |html|
    File.rename(html, File.join(File.dirname(html), 'indexy.html'))
  end
  puts "Converted and renamed #{paths.length} article pages."
end