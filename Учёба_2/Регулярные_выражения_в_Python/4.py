import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'\\', line)) >= 1:
        print(line)