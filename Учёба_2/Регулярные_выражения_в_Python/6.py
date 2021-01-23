import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r"\ba+\b", "argh", line, flags=re.IGNORECASE, count=1)
    print('\n', line)
