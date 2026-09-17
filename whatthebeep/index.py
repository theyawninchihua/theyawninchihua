import os
import sys
import re
from datetime import datetime


def result_html(result):
    if result == "PASS":
        return '<font face="Courier New" color="green"><b>PASS</b></font>'
    return '<font face="Courier New" color="red"><b>FAIL</b></font>'


def read_metadata(meta_path):
    data = {}
    try:
        import yaml  # type: ignore
        with open(meta_path, 'r', encoding='utf-8') as fh:
            loaded = yaml.safe_load(fh)
            if isinstance(loaded, dict):
                for key, value in loaded.items():
                    data[str(key).strip().lower()] = value
                return data
    except Exception:
        pass

    try:
        with open(meta_path, 'r', encoding='utf-8') as fh:
            for line in fh:
                m = re.match(r'^\s*([A-Za-z_\-]+)\s*:\s*(.+)$', line)
                if m:
                    key = m.group(1).strip().lower()
                    value = m.group(2).strip()
                    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]
                    data[key] = value
    except Exception:
        pass

    return data


def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.path.dirname(os.path.abspath(__file__))

    entries = []
    name_re = re.compile(r'^(\d{4})-(\d{2})-(\d{2})-(.+)$')

    for name in sorted(os.listdir(directory)):
        full_path = os.path.join(directory, name)
        if not os.path.isdir(full_path):
            continue

        m = name_re.match(name)
        if not m:
            continue

        yyyy, mm, dd = m.group(1), m.group(2), m.group(3)
        try:
            dt = datetime(int(yyyy), int(mm), int(dd))
        except ValueError:
            continue

        meta_path = os.path.join(full_path, 'metadata.yaml')
        if not os.path.isfile(meta_path):
            continue

        meta = read_metadata(meta_path)
        title = meta.get('title')
        result = meta.get('result')
        if title is None or result is None:
            continue

        result_norm = str(result).strip().upper()
        if result_norm not in ('PASS', 'FAIL'):
            continue

        entries.append({
            'dirname': name,
            'title': str(title),
            'result': result_norm,
            'date': dt,
            'display_date': dt.strftime('%d.%m.%y'),
        })

    entries.sort(key=lambda x: (x['date'], x['result'], x['title']), reverse=True)

    list_lines = []
    for e in entries:
        list_lines.append(f"{e['display_date']} [{result_html(e['result'])}] <a href=\"{e['dirname']}/index.html\">{e['title']}</a><br>")

    list_html = "\n        ".join(list_lines)
    fail_count = sum(1 for e in entries if e['result'] == 'FAIL')
    total_count = len(entries)
    fail_pct = (fail_count / total_count * 100) if total_count else 0.0

    html = f"""<!DOCTYPE html>
<html>
    <head>
    <link rel="icon" type="image/x-icon" href="https://theyawninchihua.github.io/theyawninchihua/theyawninchihua.png">
    <!-- The type of card. "summary_large_image" shows a big image preview -->
    <meta name="twitter:card" content="summary_large_image">
    <!-- Your site's X handle (optional) -->
    <meta name="twitter:site" content="@theyawninchihua">
    <!-- The title of your page (max 70 characters) -->
    <meta name="twitter:title" content="#WhatTheBeep | The Yawning Chihuahua">
    <!-- A brief summary of your content (max 200 characters) -->
    <meta name="twitter:description" content="Evaluation of rear seat belt reminders of Indian vehicles.">
    <!-- The FULL URL to the image you want to show (must be absolute, not relative) -->
    <meta name="twitter:image" content="https://theyawninchihua.github.io/theyawninchihua/whatthebeep/banner.png">
    <font face="Verdana">
        <title>#WhatTheBeep | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/articles">Articles</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/whatthebeep">#WhatTheBeep</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a>
        </center>
    </font>
    </head>
    <body bgcolor="beige">
    <font face="Verdana">
        <h1>#WhatTheBeep</h1>
        The Yawning Chihuahua independently evaluates the rear seatbelt reminders of Indian cars.

        <h2>All Rear Seatbelt Reminder Evaluations</h2>
        {list_html}

        <br><b>(*)</b> evaluation based on desktop research<br><br>

        <marquee scrollamount="20"><font color="green"><b>NEXT RESULTS: COMING SOON</b></font></marquee><br><br>

        <h2>FAQs</h2>
        <h3>What is the problem being targeted by #WhatTheBeep?</h3>

        By design, the rear seatbelt reminders of many Indian <b>cars don't beep when they should, or beep when they shouldn't.</b> Current regulations and Indian consumer tests only consider the scenario when a rear occupant's seatbelt <i>becomes</i> unfastened while driving.

        <h3>What is required for a car to receive <font face="Courier New" color="green">PASS</font> in #WhatTheBeep?</h3>
        Simply put, with respect to an unbelted occupant in the rear outboard seats, the car should <b>beep <a href="https://en.wikipedia.org/wiki/If_and_only_if">if and only if</a> an occupant is sitting in the seat and is not belted.</b><br><br>
        
        The criteria are formally defined in the <a href="protocol.html">#WhatTheBeep protocol</a>. 
        
        <h3>I would like to report on #WhatTheBeep, should I know anything?</h3>
        Thank you for your interest! You may include the following blurb or equivalent: <i>#WhatTheBeep is an <b>informal, independent</b> consumer information project focusing on the behaviour of rear seatbelt reminders in Indian cars.</i><br><br>
        
        Kindly avoiding reporting using language that suggests #WhatTheBeep is intended to replace safety regulations/consumer tests, or assess the overall safety level of the vehicle. It would also be much appreciated if, after publication, you could share a copy with <i>The Yawning Chihuahua</i> <a href="mailto:theyawningchihuahua@gmail.com">via email</a> for bookkeeping purposes.<br><br>

        -TYC<br><br>

        <a href="../index.html">click to go back home</a>
    </font>
    </body>
</html>
"""

    output_path = os.path.join(directory, 'index.html')
    with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)

    print(f'Generated {output_path}')


if __name__ == '__main__':
    main()