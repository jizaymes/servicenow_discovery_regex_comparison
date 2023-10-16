import re
from rich import print

input_string = ["machine1.testlab.domain.com", "machine44.sub.anything.com", "bleh4124-asfd.blah.sdd.st", "poop.sub.dom.net", "anotherdomain.lots.of.sub.domains.hos-abcv.net"]
pattern = r"^([a-zA-Z0-9.-]+)\.((?:[a-zA-Z0-9-]+)\.(?:[a-zA-Z0-9]+))$"

default_pattern = r"^([^.]+)\.((?:[^.]+\.)+[^.]+)$"

for each in input_string:
    print(f"Testing {each}")
    if match := re.match(pattern, each):
        group1 = match[1]
        group2 = match[2]
        print("- MY Match group 1:", group1)
        print("- MY Match group 2:", group2)
    else:
        print("- No match found.")

    if match2 := re.match(default_pattern, each):
        group12 = match2[1]
        group22 = match2[2]
        print("- DEF Match group 1:", group12)
        print("- DEF Match group 2:", group22)
    else:
        print("- No match found.")

    print()
