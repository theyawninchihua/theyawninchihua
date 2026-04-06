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
        In the Rear Seatbelt Reminder Evaluations a best-effort desktop assessment is made to estimate how the rear seatbelt reminder would behave in 4 scenarios. After interpreting this information a PASS/FAIL result is awarded to the system. The necessary and sufficient conditions to be awarded a <font face="Courier New" color="green"><b>PASS</b></font> are:<br><br>
        <font face="Courier New" color="green">
            +------------------------------------------------------------------------------+<br>
            | <b>PASS</b> requirements in TYC Seatbelt Reminder Evaluations---------------------- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
            | 2nd row outboard seatbelt reminder----------- | audio signal | visual signal |<br>
            | (second level warning only)------------------ | ------------ | ------------- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
            | belt is not fastened on an empty seat-------- | ----<font color="green"><b>-NO</b></font>----- | -----<font color="green"><b>-NO</b></font>----- |<br>
            | belt changes to unfastened on an empty seat-- | ----<font color="green"><b>-NO</b></font>----- | -----<font color="green"><b>-NO</b></font>----- |<br>
            | belt is not fastened on an occupied seat----- | ----<font color="green"><b>YES</b></font>----- | -----<font color="green"><b>YES</b></font>----- |<br>
            | belt changes to unfastened on occupied seat-- | ----<font color="green"><b>YES</b></font>----- | -----<font color="green"><b>YES</b></font>----- |<br>
            +-----------------------------------------------+--------------+---------------+<br><br>
            <font color="black">.....................................v/s........................................</font><br><br>
        </font>

        <font face="Courier New" color="red">
            +------------------------------------------------------------------------------+<br>
            | Behaviour requirement in forthcoming government regulation AIS-145 Amd 6---- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
            | All fixed rear seats' belt reminders--------- | audio signal | visual signal |<br>
            | (second level warning)----------------------- | ------------ | ------------- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
            | belt is not fastened on an empty seat-------- | ----<font color="red"><b>ANY</b></font>----- | -----<font color="red"><b>ANY</b></font>----- |<br>
            | belt changes to unfastened on an empty seat-- | ----<font color="red"><b>ANY</b></font>----- | -----<font color="red"><b>ANY</b></font>----- |<br>
            | belt is not fastened on an occupied seat----- | ----<font color="red"><b>ANY</b></font>----- | -----<font color="green"><b>YES</b></font>----- |<br>
            | belt changes to unfastened on occupied seat-- | ----<font color="green"><b>YES</b></font>----- | -----<font color="green"><b>YES</b></font>----- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
        </font><br>

        It is important to note that occupant detection sensors are necessary but not sufficient in order to be awarded a <font face="Courier New" color="green"><b>PASS</b></font>. Also note the Rear Seatbelt Reminder Evaluation is <b>not</b> assessing the volume, duration, period or position of the rear seatbelt reminder.

        <h3>For Journalists and Media</h3>
        If you're a journalist looking to report on these evaluations, you are more than welcome to do so! A few requests:
        <ul>
            <li> please link to the relevant evaluation page and/or notice if possible
            <li> please mention that this is an <b>independent, desktop assessment</b> of rear seatbelt reminder behaviour, not comparable with accredited safety ratings
            <li> please consider sharing a copy of relevant publications with the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a>. This way, you can be notified in case a correction is needed in the future (see: "Error Policy" section)
        </ul>

        <h3>Vehicle Selection</h3>
        A vehicle will only be evaluated under the 2026 Rear Seatbelt Reminder Evaluatons if it meets <b>AT LEAST ONE</b> of the following criteria:<br>
        <ul>
            <li> the vehicle manufacturer has requested evaluation<br><b>OR</b>
            <li> the vehicle has never been assessed under the <a href="https://bit.ly/gobargrades2025">2025 Gobar Grades</a> from the page administrator's defunct project Gobar NCRAP<br><b>OR</b>
            <li> the vehicle has been significantly updated since last evaluated (including in the 2025 Gobar Grades). Updates considered significant include, but are not limited to: facelifts, generation changes, and changes in seatbelt reminder behaviour in any variant<br><b>OR</b>
            <li> it is discovered that an error was made when the vehicle was last evaluated (including in the 2025 Gobar Grades)
        </ul>

        <h3>Error Policy</h3>
        Every effort is made to present the most accurate information possible; however, this being a desktop assessment, errors are bound to happen from time to time. The page administrator does not accept responsibility for any damages resulting from use of information on this page, including but not limited to loss of property or life.<br><br>
        <b>Prevention: </b>To improve information quality and accountability, the page administrator is adopting a policy of <b>only evaluating vehicles based on official material on the manufacturer's India website (documentation or communications)</b>, which are specified on the evaluation pages. Unlike the 2025 Gobar Grades, foreign-market documentation, PR communications, real-world test drives, corporate twin/partner model based extensions, and inferences based on reviews will no longer be accepted.<br><br>
        <b>Redressal: </b>Please report errors <a href="mailto:theyawningchihuahua@gmail.com">via email</a>. Results may be deleted, updated or re-published without notice.
        
        <h3>For Manufacturers</h3>
        Manufacturers wishing to request a vehicle evaluation are requested to contact the page administrator <a href="mailto:theyawningchihuahua@gmail.com">via email</a> through a PR team or otherwise. Please note that, while requests are very welcome, the following are prerequisites for nominatting a vehicle for evaluation:
        <ul>
            <li> the vehicle must be fully homologated for sale in India under the M1 or N1 category
            <li> a user manual (containing required information) and variant list for the vehicle must be available on the manufacturer's India website<br>
        </ul>
        While nominating a vehicle might allow publication on an agreed-upon schedule, and courtesy previews of results/notices, please note that editorial control will remain with the page administrator at all times.<br>
        Manufacturers requesting a correction are requested to see the "Error Policy" section.<br><br>

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