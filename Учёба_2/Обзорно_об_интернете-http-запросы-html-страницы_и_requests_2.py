import re
with open('file')as g:
    link = g.read()
print(link)
List = re.findall(r'"/<a href="[^>]+">.+?<\/a>/"', link) #r'(<a(.*)href( *)=((\")|(\'))(.+)((\"){1}?|(\'){1}?)( *)>)+?'
m = 1
for i in List:
    print(i, m)
    m += 1
