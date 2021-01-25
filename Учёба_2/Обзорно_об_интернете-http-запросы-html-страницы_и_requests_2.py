import re

link ='''
<a href="aaa.123.ru"> двойные кавычки </a> 1
<a href='aaa.456.ru'> одинарные кавычки </a> 2
<a href="bbb_bbb.jp"> символ '_' </a> 3
<a href="ccc-ccc.info"> символ '-' </a> 4
<a  href  =  "ddd.dddeee.eee.org"  > лишние пробелы </a> 5
<a target="blank" href="eee.eee.com" id="xyz" > доп.атрибуты </a> 6
<a href="https://fff.fff.ru"> протоколы http, https, ftp и др. </a> 7
<a href="http://ggg_gg.ru/info/res/index.html"> /ресурсы/ </a> 8
<a href="http://hhh.hhh.ru:1234"> :порт </a> 9
<a href="http://iii.iii.ru?par=abc+efg_"> ?параметр= </a> 10
<!--    Не нужно:    -->
<a href="../skip_relative_links.html"> ../относительная ссылка </a>
<link rel="image" href="link.org/files/pict.png">
'''

List = re.findall(r'(<a(.+)href( *)=( *)((\')|(\")|( ))([^\"\s]+)((\')|(\")|( ))( *)>)', link)
#r'(<a(.*)href( *)=((\")|(\'))(.+)((\"){1}?|(\'){1}?)( *)>)+?'
#<a  href  =  "ddd.dddeee.eee.org"  > лишние пробелы </a> 5

m = 1
for i in List:
    print(i)