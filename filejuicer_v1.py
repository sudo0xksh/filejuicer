import sys
import json
import re
import xml.etree.ElementTree as ET

print("=========================================")
print("Welcome to Filejuicer\n")

if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("Usage: python filejuicer.py <input> [-o <output>]")
    sys.exit()

input_file = sys.argv[1]
output_file = None

if len(sys.argv) == 4 and sys.argv[2] == "-o":
    output_file = sys.argv[3]

if input_file.endswith(".txt"):
    with open(input_file, "r") as f:
        data = f.read()

elif input_file.endswith(".json"):
    with open(input_file, "r") as f:
        data = json.load(f)

elif input_file.endswith(".xml"):
    with open(input_file, "r") as f:
        tree = ET.parse(input_file)
        root = tree.getroot()
        data = ET.tostring(root, encoding="unicode")
        
else:
    print("Invalid input format(.xml, .txt, .json)!")
    sys.exit()

pattern = r"""(
    [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} |
    https?://[a-zA-Z0-9./?&=_%-]+ |
    \b\d{1,3}(?:\.\d{1,3}){3}\b |
    \b\d{10}\b |
    \b(?:\d[ -]*?){13,16}\b |
    \b\d{4}\s\d{4}\s\d{4}\b |
    \b[A-Z]{5}[0-9]{4}[A-Z]\b |
    eyJ[a-zA-Z0-9_\-]+?\.[a-zA-Z0-9_\-]+?\.[a-zA-Z0-9_\-]+ |
    AKIA[0-9A-Z]{16} |
    (?i:secret|token|apikey|auth|bearer)\s*[:=]\s*[A-Za-z0-9_\-]+ |
    (?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}
)"""

info = re.findall(pattern, data, re.VERBOSE)

print("Here is the juice🍹:\n")
print(info)

if output_file:
    if output_file.endswith(".txt"):
        with open(output_file, "w") as f:
                f.write(str(info))

    elif output_file.endswith(".json"):
        with open(output_file, "w") as f:
            json.dump(info, f, indent=4)
    
    elif output_file.endswith(".xml"):
        xml_data = "<results>\n"
        for item in info:
            xml_data += f"  <item>{item}</item>\n"
        xml_data += "</results>"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xml_data)
    else:
        print("\nInvalid output format(.xml, .txt, .json)!")

print("\n=========================================")
print("Thanks for using Filejuicer")
print("Developed by sudo_0xksh")
