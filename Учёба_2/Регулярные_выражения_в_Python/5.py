import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'\b((\w+)\2)\b', line)) >= 1:
        print('\n', line)
