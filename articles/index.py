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

ARTICLES_PER_ROW = 2

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
    # Build a grid/table layout matching index_new_test.html
    # chunk items into rows of 3
    def chunk(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i+n]

    # Exact template from index_new_test.html (do not change characters outside the variable parts)
    html = """<!DOCTYPE html>
<html>
    <head>
    <link rel="icon" type="image/x-icon" href="https://theyawninchihua.github.io/theyawninchihua/theyawninchihua.png">
    <font face="Verdana">
        <title>Home | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/articles">Articles</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/whatthebeep">What The Beep?</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a> | <a href="https://gobarncrap.wixsite.com/gobar-ncrap/blog">Legacy website</a>
        </center>
    </font>
    </head>
    <body>
    <font face="Verdana">
        <h2>Articles</h2>
        <table>
"""

    for row in chunk(items, ARTICLES_PER_ROW):
        html += "            <tr>\n"
        for e in row:
            y, m, d = e['date']
            dd = f"{d:02d}"
            mm = f"{m:02d}"
            formatted_date = f"{dd}.{mm}.{y}"
            label = ARTICLE_TYPES.get(e['letters'], e['letters'])

            # Check for banner.png in the article directory
            banner_path = os.path.join(path, e['name'], 'banner.png')
            has_banner = os.path.isfile(banner_path)

            html += f"                <td valign=\"top\" width=\"{int(100/ARTICLES_PER_ROW)}%\">\n"
            html += "                    <figure>\n"
            if has_banner:
                # Anchor points to <name>/index.html, image src is <name>/banner.png
                html += f'                        <a href="{e["name"]}/index.html"><img src="{e["name"]}/banner.png" width="100%" border="1"></a>\n'
                html += f'                        <figcaption>{formatted_date} <b>[{label}]</b> <a href="{e["name"]}/index.html">{e["title"]}</a></figcaption>\n'
            else:
                html += f'                        <figcaption>{formatted_date} <b>[{label}]</b> <a href="{e["name"]}/index.html">{e["title"]}</a></figcaption>\n'
            html += "                    </figure>\n"
            html += "                    <br>\n"
            html += "                </td>\n"

        html += "            </tr>\n\n"

    html += "        </table>\n"
    html += "    <a href=\"../../index.html\">click to go back home</a>\n\n"
    html += "    </font>\n    </body>\n</html>\n"

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
