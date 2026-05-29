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

    # Extract model (from <h1>)
    model = extract_between(content, "<h1>", "</h1>").strip()

    # Extract result (PASS/FAIL)
    if "Result: <font face=\"Courier New\"><font color=\"green\"><b>PASS" in content:
        result = "PASS"
    else:
        result = "FAIL"

    # Extract publication date (DD.MM.YYYY)
    date_str = extract_between(content, "<b>PUBLICATION DATE: </b>", "<br>").strip()

    # Convert to datetime for sorting
    try:
        dt = datetime.strptime(date_str, "%d.%m.%Y")
    except:
        dt = datetime.min

    # Format display date → DD.MM.YY
    display_date = dt.strftime("%d.%m.%y") if dt != datetime.min else date_str

    return {
        "model": model,
        "result": result,
        "date": dt,
        "display_date": display_date,
        "filename": os.path.basename(filepath)
    }

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

    for file in os.listdir(directory):
        if file.endswith(".html"):
            path = os.path.join(directory, file)
            entries.append(parse_file(path))

    # Sort by date descending (newest first)
    entries.sort(key=lambda x: (x["date"], x["filename"]), reverse=True)

    # Build list HTML
    lines = []
    for e in entries:
        line = f'{e["display_date"]} [{result_html(e["result"])}] <a href="evaluations/{e["filename"]}">{e["model"]}</a><br>'
        lines.append(line)

    list_html = "\n        ".join(lines)

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
    <meta name="twitter:title" content="2026 Rear Seatbelt Reminder Evaluations | The Yawning Chihuahua">
    <!-- A brief summary of your content (max 200 characters) -->
    <meta name="twitter:description" content="TYC's 2026 rear seat belt reminder evaluations.">
    <!-- The FULL URL to the image you want to show (must be absolute, not relative) -->
    <meta name="twitter:image" content="https://theyawninchihua.github.io/theyawninchihua/sbr/banner.png">
    <font face="Verdana">
        <title>2026 Rear Seatbelt Reminder Evaluations | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/articles">Articles</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/sbr">Seatbelt reminder evaluation</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a> | <a href="https://gobarncrap.wixsite.com/gobar-ncrap/blog">Legacy website</a>
        </center>
    </font>
    </head>
    <body>
    <font face="Verdana">
        <h2>2026 Rear Seatbelt Reminder Evaluations</h2>
        {list_html}<br>
        <marquee scrollamount="20"><font color="green"><b>NEXT RESULTS: COMING SOON</b></font></marquee><br><br>

        <h3>Vehicle Selection</h3>
        Selection of vehicle models for evaluation is at the sole discretion of the page administrator. In general principle, in order to be evaluated, the vehicle must be classified as M1/N1, and on sale in the Indian market. Local homologation is <b>not</b> a requirement for selection. <b>Anyone can request that a specific vehicle model be <i>considered</i> for evaluation by contacting the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a> or <a href="https://x.com/theyawninchihua">on Twitter</a> with the vehicle model name.</b><br>

        <h3>Evaluation Protocol</h3>
        First, information is gathered about the behaviour of the selected vehicle's rear seat belt reminder from one of the following sources:
        <ul>
            <li> official documentation on the vehicle manufacturer's website, either on the India website or implied to be intended for the Indian market<br><b>OR</b>
            <li> a physical test ride by the page administrator, under sufficient conditions to trigger the secondary signal (a film of the test with the four test cases will be made available on the evaluation page)<br>
        </ul>

        Then, based on this information, a <font face="Courier New"><font color="green"><b>PASS</b></font></font>/<font face="Courier New"><font color="red"><b>FAIL</b></font></font> result is awarded to the vehicle. The necessary and sufficient conditions to be awarded a <font face="Courier New" color="green"><b>PASS</b></font> are:<br><br>
        <font face="Courier New">
            <table border="1">
            <tr>
                <th colspan="5"><font color="green">TYC's 2026 Rear Seatbelt Reminder Evaluation</font></th>
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
                <th colspan="5"><font color="red">Forthcoming MoRTH regulation AIS-145 Amd. 6</font></th>
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
            <li> please mention that this is an <b>independent, informal desktop assessment</b> of rear seatbelt reminder behaviour, which in no way substitutes safety regulations or ratings
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