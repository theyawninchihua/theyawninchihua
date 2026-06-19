#!/usr/bin/env python3
"""
Generate the homepage index.html using the latest 4 articles and 4 SBR results.

Usage: python index.py <articles_dir> <sbr_dir>
Example: python index.py articles whatthebeep

Follows the same validation rules as the per-directory index scripts.
Only valid entries are shown; invalid folders are skipped with a message.
"""

import os
import re
import sys
from datetime import datetime

# Article type mapping (kept near top for configurability)
ARTICLE_TYPES = {
    'B': 'BLOG POST',
    'N': 'NOTICE',
}


def read_yaml_simple(path):
    data = {}
    try:
        import yaml  # type: ignore
        with open(path, 'r', encoding='utf-8') as fh:
            loaded = yaml.safe_load(fh)
            if isinstance(loaded, dict):
                for k, v in loaded.items():
                    data[k.lower()] = v
                return data
    except Exception:
        pass

    # fallback parser
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                m = re.match(r'^\s*([A-Za-z_\-]+)\s*:\s*(.+)$', line)
                if m:
                    key = m.group(1).strip().lower()
                    val = m.group(2).strip()
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    data[key] = val
    except Exception:
        pass

    return data


def gather_articles(path):
    NAME_RE = re.compile(r'^([A-Z]+)(\d{9})$')
    items = []
    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)
        if not os.path.isdir(full):
            continue

        m = NAME_RE.match(name)
        if not m:
            print(f"Skipping '{name}': name does not match article pattern")
            continue

        letters, digits = m.group(1), m.group(2)
        yyyy, mm, dd = digits[0:4], digits[4:6], digits[6:8]
        idx_digit = digits[8]

        # validate date
        try:
            dt = datetime(int(yyyy), int(mm), int(dd))
        except Exception:
            print(f"Skipping '{name}': invalid date in name")
            continue

        index_html = os.path.join(full, 'index.html')
        meta = os.path.join(full, 'metadata.yaml')
        if not os.path.isfile(index_html):
            print(f"Skipping '{name}': missing index.html")
            continue
        if not os.path.isfile(meta):
            print(f"Skipping '{name}': missing metadata.yaml")
            continue

        data = read_yaml_simple(meta)
        title = data.get('title')
        if not title:
            print(f"Skipping '{name}': metadata.yaml missing title")
            continue

        items.append({
            'name': name,
            'letters': letters,
            'date': dt,
            'index': int(idx_digit),
            'title': str(title),
        })

    # sort newest first by date then index
    items.sort(key=lambda e: (e['date'], e['index']), reverse=True)
    return items


def gather_sbr(path):
    NAME_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2})-(.+)$')
    items = []
    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)
        if not os.path.isdir(full):
            print(f"Skipping '{name}': not a directory")
            continue

        m = NAME_RE.match(name)
        if not m:
            print(f"Skipping '{name}': name does not match YYYY-MM-DD-model-variant")
            continue

        yyyy, mm, dd = m.group(1), m.group(2), m.group(3)
        try:
            dt = datetime(int(yyyy), int(mm), int(dd))
        except Exception:
            print(f"Skipping '{name}': invalid date in name")
            continue

        meta = os.path.join(full, 'metadata.yaml')
        if not os.path.isfile(meta):
            print(f"Skipping '{name}': missing metadata.yaml")
            continue

        data = read_yaml_simple(meta)
        title = data.get('title')
        result = data.get('result')
        if title is None:
            print(f"Skipping '{name}': metadata.yaml missing title")
            continue
        if result is None:
            print(f"Skipping '{name}': metadata.yaml missing result")
            continue

        result_norm = str(result).strip().upper()
        if result_norm not in ("PASS", "FAIL"):
            print(f"Skipping '{name}': metadata.yaml has invalid result '{result}'")
            continue

        items.append({
            'dirname': name,
            'title': str(title),
            'result': result_norm,
            'date': dt,
        })

    items.sort(key=lambda e: (e['date'], e['dirname']), reverse=True)
    return items


def result_html(result):
    if result == "PASS":
        return '<font face="Courier New" color="green"><b>PASS</b></font>'
    else:
        return '<font face="Courier New" color="red"><b>FAIL</b></font>'


def main():
    if len(sys.argv) < 3:
        print("Usage: python index.py <articles_dir> <sbr_dir>")
        sys.exit(1)

    articles_dir = sys.argv[1]
    sbr_dir = sys.argv[2]

    if not os.path.isdir(articles_dir):
        print(f"Error: articles_dir '{articles_dir}' is not a directory")
        sys.exit(2)
    if not os.path.isdir(sbr_dir):
        print(f"Error: sbr_dir '{sbr_dir}' is not a directory")
        sys.exit(2)

    articles = gather_articles(articles_dir)
    sbrs = gather_sbr(sbr_dir)

    # Take up to 4 latest
    top_articles = articles[:4]
    top_sbrs = sbrs[:4]

    # Prepare article HTML: first is featured, next three shown in table
    featured = top_articles[0] if len(top_articles) >= 1 else None
    others = top_articles[1:4]

    # Build SBR list lines
    sbr_lines = []
    for e in top_sbrs:
        display_date = e['date'].strftime("%d.%m.%y")
        line = f'{display_date} [{result_html(e["result"])}] <a href="whatthebeep/{e["dirname"]}/index.html">{e["title"]}</a><br>'
        sbr_lines.append(line)

    sbr_block = "\n                    ".join(sbr_lines)

    # Build featured article block and others block matching current index.html layout
    def article_fig(a):
        full_date = a['date'].strftime("%d.%m.%Y")
        label = ARTICLE_TYPES.get(a['letters'], a['letters'])
        return (f'                        <a href="articles/{a["name"]}/index.html"><img src="articles/{a["name"]}/banner.png" width="100%" border="1"></a>\n'
                f'                        <figcaption>{full_date} <b>[{label}]</b> <a href="articles/{a["name"]}/index.html">{a["title"]}</a></figcaption>')

    featured_block = ""
    if featured:
        featured_block = "                    <figure>\n" + article_fig(featured) + "\n                    </figure>\n"

    # build three small figures in nested table; if fewer than 3 provide empty cells
    small_cells = []
    for a in others:
        cell = ("                                <figure>\n"
                + article_fig(a) + "\n"
                + "                                </figure>\n                                <br>\n")
        small_cells.append(cell)

    # Ensure list of three cells (may be fewer)
    while len(small_cells) < 3:
        small_cells.append("                                <figure>\n                                </figure>\n                                <br>\n")

    # Compose full HTML exactly following current index.html structure
    html = f"""<!DOCTYPE html>
<html>
    <head>
    <link rel="icon" type="image/x-icon" href="https://theyawninchihua.github.io/theyawninchihua/theyawninchihua.png">
    <font face="Verdana">
        <title>Home | The Yawning Chihuahua</title>
        <center>
            <img src="theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/articles">Articles</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/whatthebeep">What The Beep?</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a>
        </center>
    </font>
    </head>
    <body>
    <font face="Verdana">
        <br>
        <table>
            <tr>
                <td rowspan="2" valign="top">
                    <h2>Latest Articles</h2>
                    {featured_block}                    <table>
                        <tr>
                            <td valign="top">
{small_cells[0]}                                <a href="articles/index.html">see more</a>
                            </td>
                            <td valign="top">
{small_cells[1]}                            </td>
                            <td valign="top">
{small_cells[2]}                            </td>
                        </tr>
                    </table>
                </td>
                <td valign="top">
                    <h2>What The Beep?</h2>
                    <marquee scrollamount="10"><font color="green"><b>NEXT RESULTS: COMING SOON</b></font></marquee><br><br>
                    <b>Latest results:</b><br>
                    {sbr_block}<br>
                    <a href="whatthebeep/index.html">see more</a><br><br>
                    (*) <i>in-person evaluation</i><br><br>
                </td>
            </tr>
            <tr>
                <td valign="top">
                    <h2>Latest Tweets</h2>
                    <a href="https://x.com/theyawninchihua?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-lang="en" data-show-count="false">Follow @theyawninchihua</a><script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>
                </td>
            </tr>
        </table>
    </font>
    </body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(html)

    print('Generated index.html')


if __name__ == '__main__':
    main()
