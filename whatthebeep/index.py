import os
import sys
import re
from datetime import datetime

def extract_between(text, start, end):
    try:
        return text.split(start)[1].split(end)[0]
    except:
        return ""

def parse_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Legacy: this function is no longer used for parsing HTML files.
    # Keep it for backward compatibility but return empty dict.
    return {}

def result_html(result):
    if result == "PASS":
        return '<font face="Courier New" color="green"><b>PASS</b></font>'
    else:
        return '<font face="Courier New" color="red"><b>FAIL</b></font>'

def main():
    if len(sys.argv) < 2:
        print("Usage: python index.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    entries = []

    # Look for result directories instead of HTML files. Valid name:
    # YYYY-MM-DD-model-variant
    NAME_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2})-(.+)$')

    def read_metadata(meta_path):
        data = {}
        # Try PyYAML first
        try:
            import yaml  # type: ignore
            with open(meta_path, 'r', encoding='utf-8') as fh:
                loaded = yaml.safe_load(fh)
                if isinstance(loaded, dict):
                    for k, v in loaded.items():
                        data[k.lower()] = v
                    return data
        except Exception:
            pass

        # Fallback simple parser: look for 'title:' and 'result:'
        try:
            with open(meta_path, 'r', encoding='utf-8') as fh:
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

    for name in sorted(os.listdir(directory)):
        full = os.path.join(directory, name)
        if not os.path.isdir(full):
            # skip non-directories
            print(f"Skipping '{name}': not a directory")
            continue

        m = NAME_RE.match(name)
        if not m:
            print(f"Skipping '{name}': name does not match YYYY-MM-DD-model-variant")
            continue

        yyyy, mm, dd, rest = m.group(1), m.group(2), m.group(3), m.group(4)
        # Validate date
        try:
            dt = datetime(int(yyyy), int(mm), int(dd))
        except Exception:
            print(f"Skipping '{name}': invalid date in name")
            continue

        meta_path = os.path.join(full, 'metadata.yaml')
        if not os.path.isfile(meta_path):
            print(f"Skipping '{name}': missing metadata.yaml")
            continue

        meta = read_metadata(meta_path)
        title = meta.get('title')
        result = meta.get('result')
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

        display_date = dt.strftime("%d.%m.%y")

        entries.append({
            'dirname': name,
            'title': str(title),
            'result': result_norm,
            'date': dt,
            'display_date': display_date,
        })

    # Sort by date descending (newest first)
    entries.sort(key=lambda x: (x['date'], x['dirname']), reverse=True)

    # Build list HTML sections: in-person and desktop
    in_person_lines = []
    desktop_lines = []
    for e in entries:
        # detect marker '(*)' at end of title and remove for display
        title_raw = e.get('title', '')
        if re.search(r"\(\*\)\s*$", title_raw):
            title_display = re.sub(r"\s*\(\*\)\s*$", "", title_raw).strip()
            in_person_lines.append(f"{e['display_date']} [{result_html(e['result'])}] <a href=\"{e['dirname']}/index.html\">{title_display}</a><br>")
        else:
            desktop_lines.append(f"{e['display_date']} [{result_html(e['result'])}] <a href=\"{e['dirname']}/index.html\">{title_raw}</a><br>")

    in_person_html = "\n        ".join(in_person_lines)
    desktop_html = "\n        ".join(desktop_lines)

    # Final HTML
    html = f"""<!DOCTYPE html>
<html>
    <head>
    <link rel="icon" type="image/x-icon" href="https://theyawninchihua.github.io/theyawninchihua/theyawninchihua.png">
    <!-- The type of card. "summary_large_image" shows a big image preview -->
    <meta name="twitter:card" content="summary_large_image">
    <!-- Your site's X handle (optional) -->
    <meta name="twitter:site" content="@theyawninchihua">
    <!-- The title of your page (max 70 characters) -->
    <meta name="twitter:title" content="What The Beep? | The Yawning Chihuahua">
    <!-- A brief summary of your content (max 200 characters) -->
    <meta name="twitter:description" content="Evaluation of rear seat belt reminders of Indian vehicles.">
    <!-- The FULL URL to the image you want to show (must be absolute, not relative) -->
    <meta name="twitter:image" content="https://theyawninchihua.github.io/theyawninchihua/whatthebeep/banner.png">
    <font face="Verdana">
        <title>What The Beep? | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/articles">Articles</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/whatthebeep">What The Beep?</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a>
        </center>
    </font>
    </head>
    <body>
    <font face="Verdana">
        <h1>What The Beep?</h1>
        <h3>In-Person Evaluations</h3>
        These are vehicles evaluated based on seatbelt reminder tests that the page administrator has had the opportunity to conduct in person.<br><br>
        {in_person_html}

        <h3>Desktop Evaluations</h3>
        Due to limited resources for in-person testing, some models (new, recently updated, or otherwise of interest) are evaluated based on publicly available official documentation until they can be evaluated based on in-person testing.<br><br>
        {desktop_html}

        <br><marquee scrollamount="20"><font color="green"><b>NEXT RESULTS: COMING SOON</b></font></marquee><br>

        <h3>Vehicle Selection</h3>
        Selection of vehicle models for evaluation is at the sole discretion of the page administrator. In general principle, in order to be evaluated, the vehicle must be classified as M1/N1, and on sale in the Indian market. Local homologation is <b>not</b> a requirement for selection. <b>Anyone can request that a specific vehicle model be <i>considered</i> for evaluation by contacting the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a> or <a href="https://x.com/theyawninchihua">on Twitter</a> with the vehicle model name.</b><br>

        <h3>Evaluation Protocol</h3>
        First, information is gathered about the behaviour of the selected vehicle's rear seat belt reminder from one of the following sources:
        <ul>
            <li> <b>in-person testing: </b>a physical test ride by the page administrator, with four testcases filmed under sufficient conditions to trigger the secondary signal, registration or VIN recorded, and with sufficient evidence that the vehicle is representative of recent production. An evaluation based on in-person testing is called an <b>in-person evaluation</b>.</li>
            <li> <b>documentation: </b>official documentation from the vehicle manufacturer describing the vehicle's rear seatbelt reminder, either on the India website or implied to be intended for the Indian market. An evaluation based on documentation is called a <b>desktop evaluation</b>.</li>
        </ul>
        In case both sources are available, the resulting in-person evaluation holds precedence. A desktop evaluation may be replaced by an in-person evaluation if the opportunity for in-person testing arises.<br><br>

        Then, based on this information, a <font face="Courier New"><font color="green"><b>PASS</b></font></font>/<font face="Courier New"><font color="red"><b>FAIL</b></font></font> result is awarded to the vehicle. The necessary and sufficient conditions to be awarded a <font face="Courier New" color="green"><b>PASS</b></font> are:<br><br>
        <font face="Courier New">
            <table border="1">
            <tr>
                <th colspan="5"><font color="green">PASS criteria for What The Beep?</font></th>
            </tr>
            <tr>
                <th colspan="5">Behaviour requirements for second-level warning in the 2nd-row outboard seats</th>
            </tr>
            <tr>
                <th>Testcase</th>
                <th>Description</th>
                <th>Acoustic signal</th>
                <th>Visual signal</th>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_1.png" width="60"></td>
                <td align="center">occupant does not fasten seatbelt</td>
                <td align="center"><font color="green"><b>YES</b></font></td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_2.png" width="60"></td>
                <td align="center">occupant takes off seatbelt</td>
                <td align="center"><font color="green"><b>YES</b></font></td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_3.png" width="60"></td>
                <td align="center">seatbelt not fastened on an empty seat</td>
                <td align="center"><font color="green"><b>NO</b></font></td>
                <td align="center"><font color="green"><b>NO</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_4.png" width="60"></td>
                <td align="center">seatbelt taken off on an empty seat</td>
                <td align="center"><font color="green"><b>NO</b></font></td>
                <td align="center"><font color="green"><b>NO</b></font></td>
            </tr>
            </table>
        </font><br>

        In comparison, the requirements of upcoming government legislation are explained below:<br><br>

        <font face="Courier New">
            <table border="1">
            <tr>
                <th colspan="5">Forthcoming MoRTH regulation AIS-145 Amd. 6</th>
            </tr>
            <tr>
                <th colspan="5">Behaviour requirements for second-level warning in all fixed rear seats (as interpreted by page administrator)</th>
            </tr>
            <tr>
                <th>Testcase</th>
                <th>Description</th>
                <th>Acoustic signal</th>
                <th>Visual signal</th>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_1.png" width="60"></td>
                <td align="center">occupant does not fasten seatbelt</td>
                <td align="center"><font color="black"><b>-</b></font></td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_2.png" width="60"></td>
                <td align="center">occupant takes off seatbelt</td>
                <td align="center"><font color="green"><b>YES</b></font></td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            </table>
        </font><br>

        <h3>For Journalists and Media</h3>
        If you're a journalist looking to report on these evaluations, you are more than welcome to do so! A few requests:
        <ul>
            <li> please mention that this is an <b>independent, informal assessment</b> of rear seatbelt reminder behaviour, which in no way substitutes safety regulations or ratings
            <li> after publication, could you please share a copy with the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a>?
        </ul>
        
        <h3>Error Policy</h3>
        Every effort is made to present the most accurate information possible; however, this being a desktop assessment, errors are bound to happen from time to time. The page administrator does not accept responsibility for any damages resulting from use of information on this page, including but not limited to loss of property or life. The page administrator reserves the right to make changes to this page and/or result pages without notice.<br><br>
        Please report errors to the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a>.<br><br>

        <a href="../index.html">click to go back home</a>
    </font>
    </body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Generated index.html")

if __name__ == "__main__":
    main()