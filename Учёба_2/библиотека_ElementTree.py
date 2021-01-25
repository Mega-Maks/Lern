from xml.etree import ElementTree

count_dict = {'red': 0, "green": 0, 'blue': 0}

with open('XML.xml', 'w') as xml:
    xml.write(input())
tree = ElementTree.parse('XML.xml')
root = tree.getroot()

def counter(var, root):
    if root.findall('cube') == []:
        count_dict[root.attrib['color']] += var
    else:
        count_dict[root.attrib['color']] += var
        for i in root.findall('cube'):
            list = root.findall('cube')
            counter(var + 1, i)

counter(1, root)

for key in count_dict:
    print(count_dict[key], end=' ')
