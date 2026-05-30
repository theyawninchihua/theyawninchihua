"""
Generate an articles index.html in the exact style of the existing manual file.

Usage: python index.py [articles_dir]
Example 1: python index.py .
Example 2: python articles/index.py articles

Scans the given directory for valid article directories named like
  <LETTERS><YYYY><MM><DD><N>
where <LETTERS> are uppercase letter(s) identifying the article type,
and the trailing 9 digits are YYYYMMDD and a single index digit (1-9).

Valid directories must contain `index.html` and `metadata.yaml` with a
`title` field. Directories that fail validation are skipped and a message
is printed explaining why.

The mapping from initial letters to human-readable labels is configurable
via the `ARTICLE_TYPES` dict below.
"""

import os
import re
import sys
from datetime import datetime

# Configurable mapping for article type letters -> label
ARTICLE_TYPES = {
    'B': 'BLOG POST',
    'N': 'NOTICE',
}

# Directory name must be: uppercase letters + 9 digits
NAME_RE = re.compile(r'^([A-Z]+)(\d{9})$')


def read_title_from_metadata(meta_path):
    # Try to use PyYAML if available, otherwise fall back to a simple parser
    try:
        import yaml  # type: ignore
        with open(meta_path, 'r', encoding='utf-8') as fh:
            data = yaml.safe_load(fh)
            if isinstance(data, dict) and 'title' in data:
                return str(data['title'])
    except Exception:
        pass

    # Simple fallback: find a line starting with 'title:'
    try:
        with open(meta_path, 'r', encoding='utf-8') as fh:
            for line in fh:
                m = re.match(r'^\s*title\s*:\s*(.+)$', line)
                if m:
                    val = m.group(1).strip()
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    return val
    except Exception:
        pass

    return None


def build_items(path):
    items = []
    for name in sorted(os.listdir(path)):
        fullname = os.path.join(path, name)
        if not os.path.isdir(fullname):
            continue
        if name.startswith('.'):
            continue

        m = NAME_RE.match(name)
        if not m:
            print(f"Skipping '{name}': name does not match article pattern")
            continue

        letters, digits = m.group(1), m.group(2)
        yyyy = digits[0:4]
        mm = digits[4:6]
        dd = digits[6:8]
        idx_digit = digits[8]

        # Validate date
        try:
            datetime(int(yyyy), int(mm), int(dd))
        except Exception:
            print(f"Skipping '{name}': invalid date in name")
            continue

        # Required files
        index_html = os.path.join(fullname, 'index.html')
        meta_yaml = os.path.join(fullname, 'metadata.yaml')
        if not os.path.isfile(index_html):
            print(f"Skipping '{name}': missing index.html")
            continue
        if not os.path.isfile(meta_yaml):
            print(f"Skipping '{name}': missing metadata.yaml")
            continue

        title = read_title_from_metadata(meta_yaml)
        if not title:
            print(f"Skipping '{name}': metadata.yaml missing title")
            continue

        items.append({
            'name': name,
            'letters': letters,
            'date': (int(yyyy), int(mm), int(dd)),
            'index': int(idx_digit),
            'title': title,
        })

    # Sort by date (YYYY,MM,DD) then index, newest first
    items.sort(key=lambda e: (e['date'][0], e['date'][1], e['date'][2], e['letters'], e['index']), reverse=True)
    return items


def render_index(path, items):
    # Build list item lines exactly matching spacing/format of current manual file
    list_lines = []
    for e in items:
        y, m, d = e['date']
        dd = f"{d:02d}"
        mm = f"{m:02d}"
        formatted_date = f"{dd}.{mm}.{y}"
        label = ARTICLE_TYPES.get(e['letters'], e['letters'])
        # Note: keep spacing and punctuation identical to existing file
        line = f'        <li>{formatted_date} <b>[{label}]</b> <a href="{e["name"]}/index.html">{e["title"]}</a><br><br></li>'
        list_lines.append(line)

    # Exact template from existing index.html (do not change any characters)
    html = """<!DOCTYPE html>
<html>
    <head>
    <link rel="icon" type="image/x-icon" href="https://theyawninchihua.github.io/theyawninchihua/theyawninchihua.png">
    <font face="Verdana">
        <title>Home | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/articles">Articles</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/sbr">Seatbelt reminder evaluation</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a> | <a href="https://gobarncrap.wixsite.com/gobar-ncrap/blog">Legacy website</a>
        </center>
    </font>
    </head>
    <body>
    <font face="Verdana">
        <h2>Articles</h2>
        <ul>
"""

    if list_lines:
        html += "\n".join(list_lines) + "\n"

    html += """        </ul>
    </font>
    </body>
</html>
"""

    outpath = os.path.join(path, 'index.html')
    with open(outpath, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(html)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    if not os.path.isdir(target):
        print(f"Error: target '{target}' is not a directory")
        sys.exit(2)

    items = build_items(target)
    render_index(target, items)


if __name__ == '__main__':
    main()
