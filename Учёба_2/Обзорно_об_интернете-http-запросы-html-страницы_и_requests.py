import requests as r
import re


def getter(link_for_get):
    get_link = r.get(link_for_get)
    get_link = get_link.text
    get_link = re.findall(r'<a href=[\"\'](.+?)[\"\'](.*?)>', get_link)
    return get_link


def checker(start_link, end_link):
    link_from_first = getter(start_link)
    print(link_from_first)
    for link in link_from_first:
        print(link)
        link_from_second = getter(link[0])
        for link_2 in link_from_second:
            print(link_2)
            if link_2[0] == end_link:
                print('Yes')
            else:
                print('No')


checker(input(), input())
