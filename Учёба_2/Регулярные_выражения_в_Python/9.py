import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    print(re.findall(r'((((00)*)1((00)*)1((00)*))+)', line))
'''
(1(0){1,999,2}1(0){1,999,2}1)
'''