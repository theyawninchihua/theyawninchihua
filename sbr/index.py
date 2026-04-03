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
        <title>Seat Belt Reminder Evaluation | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/sbr">Seat belt reminder evaluation</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a> | <a href="https://gobarncrap.wixsite.com/gobar-ncrap/blog">Legacy website</a>
        </center>
    </head>
    <body>
        <b>Seat Belt Reminder Evaluations</b><br><br>
        {list_html}<br><br>

        <b>About the Seat Belt Reminder Evaluations</b><br>
        The guiding principle behind the evaluation is that an effective rear seat belt reminder should <b>never</b> activate when a seat is unoccupied, and <b>must</b> activate if an occupied seat's belt is not fastened. Neither of these is required by forthcoming legislation, which only requires that the reminder signals activate when a belt is fastened and then unfastened <i>at least</i> on occupied seats.<br><br>
        In the Seat Belt Reminder Evaluations I perform desktop assessment to estimate how the second-level audio and visual signals for the 2nd-row outboard seats would behave in 4 scenarios. The necessary and sufficient conditions to be awarded a <font face="Courier New" color="green"><b>PASS</b></font> are:<br><br>
        <font face="Courier New" color="green">
            +------------------------------------------------------------------------------+<br>
            | <b>PASS</b> requirements in TYC Seat Belt Reminder Evaluations--------------------- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
            | 2nd row outboard seat belt reminder---------- | audio signal | visual signal |<br>
            | (second level warning only)------------------ | ------------ | ------------- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
            | belt is not fastened on an empty seat-------- | ----<font color="green"><b>NO-</b></font>----- | -----<font color="green"><b>NO-</b></font>----- |<br>
            | belt changes to unfastened on an empty seat-- | ----<font color="green"><b>NO-</b></font>----- | -----<font color="green"><b>NO-</b></font>----- |<br>
            | belt is not fastened on an occupied seat----- | ----<font color="green"><b>YES</b></font>----- | -----<font color="green"><b>YES</b></font>----- |<br>
            | belt changes to unfastened on occupied seat-- | ----<font color="green"><b>YES</b></font>----- | -----<font color="green"><b>YES</b></font>----- |<br>
            +-----------------------------------------------+--------------+---------------+<br>
        </font><br>

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

        It is important to note that occupant detection sensors are necessary but not sufficient in order to be awarded a <font face="Courier New" color="green"><b>PASS</b></font>. Also note the Seat Belt Reminder Evaluation is also <b>not</b> assessing the volume, duration, period or position of the seat belt reminder.<br><br>

        <a href="../index.html">click to go back home</a>
    </body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Generated index.html")

if __name__ == "__main__":
    main()