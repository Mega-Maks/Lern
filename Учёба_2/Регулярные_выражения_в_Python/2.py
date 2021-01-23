import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'\bcat\b', line)) >= 1:
        print(line)