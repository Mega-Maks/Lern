import requests as r
import re
Start = r.get(input())
Start = Start.text
Start = re.findall(r'".+"', Start)[0]
print('Start = ', Start)
End = input()
Second = r.get(Start[1:-1])
Second = Second.text
Second = re.findall(r'".+"', Second, )[0]
Second = r.get(Second[1:-1])
Second = Second.text
Second = re.findall(r'".+"', Second)[0]
print('Second = ', Second)
print('End = ', End)
if Second[1:-1] == End:
    print('Yes')
else:
    print('No')
