import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r'z...z', line)) >= 1:
        print(line)