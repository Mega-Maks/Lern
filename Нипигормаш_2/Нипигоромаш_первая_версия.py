from docxtpl import DocxTemplate
import xlwt
import os
import shutil


def dict_writer(number, list):
    number1 = number
    day_dict = {number: []}
    for i in range(int(len(list) / 5)):
        day_dict[number1].append({number + 1: list[0:5]})
        list = list[5:]
        number += 1
    return day_dict, number


with open('', 'r') as g:
    g = g.read()
List = g.split('\n')
List2 = []
for i in List:
    List2.append(i.split('\t'))
dates_dict = dict()
for elem in List2:
    dates_dict[elem[0]] = elem[1:]
counter = int(input('введите номер акта '))
for date in dates_dict:
    dates_dict[date], counter = dict_writer(counter, dates_dict[date])
    counter += 1
for date in dates_dict:
    print(dates_dict[date])
print(dates_dict)
dox_file = DocxTemplate('Шаблон_dox.docx')
os.chdir('C:\\Users\\Ryzhk\\Desktop\\Новая папка (2)')
street_list = []
money = 0
act_val = int(input())
for date in dates_dict:
    print(date)
    for day in dates_dict[date]:
        print(day)
        for way in dates_dict[date][day]:
            print(way)
            for number in way:
                dox_file.save(str(number) + '  (' + way[number][0] + ' ' + way[number][1]
                              + ')  ' + way[number][2] + '  ' + way[number][4] + ' ' + 'т.' + '  ' + date + '  ' +
                              way[number][3] + '.docx')
                street_list = street_list + [way[number][0] + ' - ' + way[number][1]]
                money = money + int(way[number][3])
            file_name = '\\' + str(day) + '  Акт №' + str(act_val) + '  (' + '  '.join(street_list) + ')  ' +\
                        date + '  ' + str(money) + '  ' + str(int(money / 1300)) + '.xlsx'
            print(file_name)
        shutil.copyfile('C:\\Users\\Ryzhk\\PycharmProjects\\Нипигормаш\\Шаблон_exel.xlsx',
                        'C:\\Users\\Ryzhk\\Desktop\\Новая папка (2)' + file_name)
        act_val += 1
        street_list = []
        money = 0

