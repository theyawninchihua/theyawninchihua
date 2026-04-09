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
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/sbr">Seatbelt reminder evaluation</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a> | <a href="https://gobarncrap.wixsite.com/gobar-ncrap/blog">Legacy website</a>
        </center>
    </font>
    </head>
    <body>
    <font face="Verdana">
        <h2>2026 Rear Seatbelt Reminder Evaluations</h2>
        {list_html}<br>
        <marquee scrollamount="20"><font color="green"><b>NEXT RESULTS: COMING SOON</b></font></marquee><br><br>

        <h3>About the Rear Seatbelt Reminder Evaluations</h3>
        In the Rear Seatbelt Reminder Evaluations a best-effort desktop assessment is made to estimate how a vehicle's rear seatbelt reminder would behave in 4 scenarios. After interpreting this information a <font face="Courier New"><font color="green"><b>PASS</b></font></font>/<font face="Courier New"><font color="red"><b>FAIL</b></font></font> result is awarded to the system. The necessary and sufficient conditions to be awarded a <font face="Courier New" color="green"><b>PASS</b></font> are:<br><br>
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
                <th>Audio signal</th>
                <th>Visual signal</th>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_1.png" width="60"></td>
                <td align="center">occupant does not fasten seatbelt</td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_2.png" width="60"></td>
                <td align="center">occupant takes off seatbelt</td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_3.png" width="60"></td>
                <td align="center">seatbelt not fastened on an empty seat</td>
                <td align="center"><font color="green"><b>NOT PERMITTED</b></font></td>
                <td align="center"><font color="green"><b>NOT PERMITTED</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_4.png" width="60"></td>
                <td align="center">seatbelt taken off on an empty seat</td>
                <td align="center"><font color="green"><b>NOT PERMITTED</b></font></td>
                <td align="center"><font color="green"><b>NOT PERMITTED</b></font></td>
            </tr>
            </table>
        </font><br>

        ......................v/s......................<br><br>

        <font face="Courier New">
            <table border="1">
            <tr>
                <th colspan="5"><font color="red">Forthcoming MoRTH regulation AIS-145 Amd. 6</font></th>
            </tr>
            <tr>
                <th colspan="5">Interpreted behaviour requirements for second-level warning in all fixed rear seats</th>
            </tr>
            <tr>
                <th>Testcase</th>
                <th>Description</th>
                <th>Audio signal</th>
                <th>Visual signal</th>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_1.png" width="60"></td>
                <td align="center">occupant does not fasten seatbelt</td>
                <td align="center"><font color="red"><b>NOT REQUIRED</b></font></td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_2.png" width="60"></td>
                <td align="center">occupant takes off seatbelt</td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
                <td align="center"><font color="green"><b>REQUIRED</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_3.png" width="60"></td>
                <td align="center">seatbelt not fastened on an empty seat</td>
                <td align="center"><font color="red"><b>PERMITTED</b></font></td>
                <td align="center"><font color="red"><b>PERMITTED</b></font></td>
            </tr>
            <tr>
                <td align="center"><img src="./testcase_4.png" width="60"></td>
                <td align="center">seatbelt taken off on an empty seat</td>
                <td align="center"><font color="red"><b>PERMITTED</b></font></td>
                <td align="center"><font color="red"><b>PERMITTED</b></font></td>
            </tr>
            </table><br>
        </font><br>

        It is important to note that occupant detection sensors are necessary but not sufficient in order to be awarded a <font face="Courier New" color="green"><b>PASS</b></font>. Also note the Rear Seatbelt Reminder Evaluation is <b>not</b> assessing the volume, duration, period or position of the rear seatbelt reminder.

        <h3>Want to nominate a vehicle?</h3>
        If you are an individual or organisation who wishes to nominate a vehicle model for evaluation, you are welcome to do so by contacting the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a> with the following details:
        <ul>
            <li> brand and model name of the vehicle you want to recommend for evaluation
            <li> a link to a user manual for the model on the manufacturer's India website
            <li> a link to a variant-wise spec sheet for the model on the manufacturer's India website
        </ul>
        No reason is required for nominating the model. However, please note that all editorial control, including the final decision to select the vehicle, rests with the page administrator.

        <h3>For Journalists and Media</h3>
        If you're a journalist looking to report on these evaluations, you are more than welcome to do so! A few requests:
        <ul>
            <li> please mention that this is an <b>independent, informal desktop assessment</b> of rear seatbelt reminder behaviour, which in no way substitutes safety regulations or ratings
            <li> please consider sharing a copy of relevant publications with the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a>. This way, you can be notified in case a correction is needed in the future (see: "Error Policy")
        </ul>

        <h3>Vehicle Selection</h3>
        A vehicle model will only be evaluated under the 2026 Rear Seatbelt Reminder Evaluatons if it is fully homologated as M1/N1 and meets <b>AT LEAST ONE</b> of the following criteria:<br>
        <ul>
            <li> someone has nominated the model for evaluation (see: "Want to nominate a vehicle?")<br><b>OR</b>
            <li> the model has never been assessed under the <i><a href="https://bit.ly/gobargrades2025">2025 Gobar Grades</a></i> from the page administrator's defunct project <i><a href="https://bit.ly/gobarncrap">Gobar NCRAP</a></i><br><b>OR</b>
            <li> the model has been significantly updated since last evaluated (including in the <i>2025 Gobar Grades</i>). Updates considered significant include, but are not limited to: facelifts, generation changes, and changes in seatbelt reminder behaviour in any variant<br><b>OR</b>
            <li> it is discovered that an error was made when the model was last evaluated
        </ul>
        
        <h3>Error Policy</h3>
        Every effort is made to present the most accurate information possible; however, this being a desktop assessment, errors are bound to happen from time to time. The page administrator does not accept responsibility for any damages resulting from use of information on this page, including but not limited to loss of property or life.<br><br>
        <b>Prevention: </b>To improve information quality and accountability, the page administrator is adopting a policy of <b>only evaluating vehicles based on official documentation on the manufacturer's India website</b>, which are specified on the evaluation pages. Unlike the 2025 Gobar Grades, foreign-market documentation, PR communications, real-world test drives, corporate twin/partner model based extensions, and inferences based on reviews will no longer be accepted.<br><br>
        <b>Redressal: </b>Please report errors to the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a>. Results may be deleted, updated or re-published without notice.<br><br>

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