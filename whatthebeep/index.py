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

    within_day_order = {
        '2026-08-28-RUMION-SCNG': 0,
        '2026-08-28-ERTIGA-VXiOSCNG': 1,
        '2026-06-05-CRETAELECTRIC-Executive42kWh': 0,
        '2026-06-05-CITYiVTEC-SV15iVTEC': 1,
        '2026-06-01-URBANCRUISEREBELLA-E361kWhFWD': 0,
        '2026-06-01-FRONX-SigmaSCNG': 1,
        '2026-06-01-SCORPIOCLASSIC-S': 2,
        '2026-06-01-CITYeHEV-ZXPlus15iMMD': 3,
        '2026-06-01-BOLERONEO-N4': 4,
        '2026-06-01-BOLEROCLASSIC-B4': 5,
        '2026-05-24-WAGONR-TourH3SCNG': 0,
        '2026-05-24-DZIRE-TourSSCNG': 1,
        '2026-04-10-XUV3XOEV-AX539kWh': 0,
        '2026-04-10-PUNCHEV-Smart30kWh': 1,
        '2026-04-04-THAR-AXTRWD3door': 0,
        '2026-04-04-SELTOS-HTESmartstreamG15': 1,
        '2026-04-04-GRAVITE-Visia10B4D': 2,
        '2026-04-03-XUV7XO-AX': 0,
        '2026-04-03-VERNA-HX515MPI': 1,
        '2026-04-03-EXTER-HX212Kappa2': 2,
        '2026-04-03-DUSTER-authentic-TCe100': 3,
    }

    entries.sort(key=lambda x: (-x['date'].timestamp(), within_day_order.get(x['dirname'], 999), x['dirname']))

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
    <body bgcolor="beige">
    <font face="Verdana">
        <h1>What The Beep?</h1>
        The Yawning Chihuahua independently evaluates the rear seatbelt reminders of Indian cars.

        <h3>All Rear Seatbelt Reminder Evaluations</h3>
        {list_html}

        <br><b>(*) desktop evaluation:</b> due to limited resources for in-person testing, some models (new, follower-requested, recently updated, or otherwise of interest) are evaluated based on publicly available official documentation until they can be evaluated based on in-person testing. <br><br>

        <marquee scrollamount="20"><font color="green"><b>NEXT RESULTS: COMING SOON</b></font></marquee><br><br>

        <h3>About What The Beep?</h3>
        To put it simply: to earn a <font face="Courier New" color="green"><b>PASS</b></font>, the car's rear seatbelt reminder <b>must alert audibly</b> when there is an unbelted rear occupant, and <b>must not alert</b> otherwise (see rigorous definition below).<br><br>

        Despite the simple criteria, {fail_pct:.2f}% of Indian cars evaluated so far ({fail_count} of {total_count}) have received <font face="Courier New" color="red"><b>FAIL</b></font>. Investigation by <i>The Yawning Chihuahua</i> has also revealed multiple cases of identical vehicle models having inferior rear seatbelt reminders for India than overseas, sometimes even if the overseas model is built in India.<br><br>

        Common reasons to be awarded <font face="Courier New" color="red"><b>FAIL</b></font> are:
        <ul>
            <li>the system does not beep until a seatbelt is buckled and then unbuckled, even if the seat is occupied</li>
            <li>the system beeps from the start when a rear seatbelt is not fastened, even if the seat is not occupied</li>
            <li>the vehicle does not have a rear seatbelt reminder yet</li>
        </ul>
        
        Please note that the intention is to evaluate the <i>behaviour</i> of the seatbelt reminder and not the underlying technology; e.g., while necessary, <b>the presence of occupant detection sensors does not imply a <font face="Courier New" color="green"><b>PASS</b></font> result</b>.<br><br>

        <center><i>A short demonstration of the consequences of not wearing rear seatbelts:</i></center>
        <center><iframe width="560" height="315" src="https://www.youtube.com/embed/yYrKh6DYGqM?si=hDqEIFWFfPrtC6sG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

        <h3>Vehicle Selection</h3>
        Selection of vehicle models for evaluation is at the sole discretion of the page administrator of <i>The Yawning Chihuahua</i>. In general principle, in order to be evaluated, the vehicle must be classified as M1/N1, be on sale in the Indian market, and have a second row of seats. Local homologation is <b>not</b> a requirement for selection. <b>Anyone can request that a specific vehicle model be <i>considered</i> for evaluation by contacting <i>The Yawning Chihuahua</i> <a href="mailto:theyawningchihuahua@gmail.com">via email</a> or <a href="https://x.com/theyawninchihua">on Twitter</a> with the vehicle model name.</b><br>

        <h3>Evaluation Protocol</h3>
        First, information is gathered about the behaviour of the selected vehicle's rear seat belt reminder from one of the following sources:
        <ul>
            <li> <b>in-person testing: </b>a physical test ride by the page administrator of <i>The Yawning Chihuahua</i>, with four testcases filmed under sufficient conditions to trigger the secondary signal, registration or VIN recorded, and with sufficient evidence that the vehicle is representative of recent production. An evaluation based on in-person testing is called an <b>in-person evaluation</b>.</li>
            <li> <b>documentation: </b>official documentation from the vehicle manufacturer describing the vehicle's rear seatbelt reminder, either on the India website or implied to be intended for the Indian market. An evaluation based on documentation is called a <b>desktop evaluation</b>.</li>
        </ul>
        In case both sources are available, the resulting in-person evaluation holds precedence. A desktop evaluation may be replaced by an in-person evaluation if the opportunity for in-person testing arises.<br><br>

        Then, based on this information, a <font face="Courier New"><font color="green"><b>PASS</b></font></font>/<font face="Courier New"><font color="red"><b>FAIL</b></font></font> result is awarded to the vehicle. The necessary and sufficient conditions to be awarded a <font face="Courier New" color="green"><b>PASS</b></font> are:<br><br>
        <font face="Courier New">
            <table border="1">
            <tr>
                <th colspan="3"><font color="green">PASS criteria for What The Beep?</font></th>
            </tr>
            <tr>
                <th colspan="3">Behaviour requirements for second-level warning in the 2nd-row outboard seats</th>
            </tr>
            <tr>
                <th>Testcase</th>
                <th>Description</th>
                <th>Audible warning</th>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_1.png" width="60"></td>
                <td align="center">occupant does not fasten seatbelt</td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_2.png" width="60"></td>
                <td align="center">occupant takes off seatbelt</td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_3.png" width="60"></td>
                <td align="center">seatbelt not fastened on an empty seat</td>
                <td align="center"><font color="green"><b>NO</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_4.png" width="60"></td>
                <td align="center">seatbelt taken off on an empty seat</td>
                <td align="center"><font color="green"><b>NO</b></font></td>
            </tr>
            </table>
        </font><br>

        In comparison, the narrower requirements of upcoming government legislation are explained below:<br><br>

        <font face="Courier New">
            <table border="1">
            <tr>
                <th colspan="5">Forthcoming MoRTH regulation AIS-145 Amd. 6</th>
            </tr>
            <tr>
                <th colspan="5">Behaviour requirements for second-level warning in all fixed rear seats (as interpreted by <i>The Yawning Chihuahua</i>)</th>
            </tr>
            <tr>
                <th>Testcase</th>
                <th>Description</th>
                <th>Audible warning</th>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_2.png" width="60"></td>
                <td align="center">occupant takes off seatbelt</td>
                <td align="center"><font color="green"><b>YES</b></font></td>
            </tr>
            </table>
        </font><br>

        <h3>For Journalists and Media</h3>
        If you're a journalist looking to report on <i>What The Beep?</i> evaluations, you are more than welcome to do so! A few requests:
        <ul>
            <li> please consider mentioning that <i>What The Beep?</i> is an <b>independent, informal assessment</b> of rear seatbelt reminder behaviour</li>
            <li> kindly avoiding using language that suggests <i>What The Beep?</i> is intended to:
            <ul>
                <li>replace safety regulations</li>
                <li>replace consumer tests/safety ratings</li>
                <li>assess the overall safety level of the vehicle</li>
            </ul></li>
            <li> it would be much appreciated if, after publication, you could share a copy with <i>The Yawning Chihuahua</i> <a href="mailto:theyawningchihuahua@gmail.com">via email</a> for bookkeeping purposes</li>
        </ul>
        
        <h3>Error Policy</h3>
        Every effort is made to present the most accurate information possible; however, this being a desktop assessment, errors are bound to happen from time to time. The page administrator of <i>The Yawning Chihuahua</i> does not accept responsibility for any damages resulting from use of information on this page, including but not limited to loss of property or life. The page administrator of <i>The Yawning Chihuahua</i> reserves the right to make changes to this page and/or result pages without notice.<br><br>
        Please report errors to <i>The Yawning Chihuahua</i> <a href="mailto:theyawningchihuahua@gmail.com">via email</a>.<br><br>

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