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
        <title>Home | The Yawning Chihuahua</title>
        <center>
            <img src="../theyawninchihua.png" width="45"><br>
            <b>The Yawning Chihuahua</b><br>
            <a href="https://theyawninchihua.github.io/theyawninchihua">Home</a> | <a href="https://theyawninchihua.github.io/theyawninchihua/sbr">Seat belt reminder evaluation</a> | <a href="https://x.com/theyawninchihua">Twitter</a> | <a href="https://instagram.com/theyawninchihua">Instagram</a> | <a href="https://youtube.com/@theyawninchihua">YouTube</a> | <a href="https://gobarncrap.wixsite.com/gobar-ncrap/blog">Legacy website</a>
        </center>
    </head>
    <body>
        <b>Seat Belt Reminder Evaluations</b><br><br>
        {list_html}<br><br>

        <a href="../index.html">click to go back home</a>
    </body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Generated index.html")

if __name__ == "__main__":
    main()