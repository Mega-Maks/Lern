import requests as r
import re
start_link = input()
end_link = input()

Start = r.get(start_link)
Start = Start.text
Start = re.findall(r'".+"', Start)[0]
link_from_first = Start[1:-1]

Second = r.get(link_from_first)
Second = Second.text
Second = re.findall(r'".+"', Second)[0]
link_from_second = Second[1:-1]

Second = r.get(link_from_second)
Second = Second.text
Second = re.findall(r'".+"', Second)[0]
link_from_third = Second[1:-1]

if link_from_second == end_link:
    print('Yes')
else:
    print('No')
