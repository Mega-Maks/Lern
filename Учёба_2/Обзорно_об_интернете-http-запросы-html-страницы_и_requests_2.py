import re
import requests as r


html_link = input()
html_file = r.get(html_link)
links = html_file.text

find_list = re.findall(r'<a(.*?)href(.*?)=(.*?)[\"\']((http://)|(https://)|(ftp://)|[^.])(.*?)[?:/\"\'](.*?)', links)

answer_set = set()

for links_tuple in find_list:
    if links_tuple[-2] == ' ..':
        continue
    elif links_tuple[3][-1] != '/':
        answer_set.add(links_tuple[3] + links_tuple[7])
    else:
        answer_set.add(links_tuple[7])
for answer in answer_set:
    print(answer)
