''''
Task_1______________________________________________________________________________________________________


with open('file_1.txt', 'w', encoding='utf-8') as f_1:
    while True:
        line = input('Ввод новой строки:     ')
        if not line:
            break

        print(line, file=f_1)




Task_2______________________________________________________________________________________________________



with open('File_2.txt', encoding='utf-8') as f_2:
    x_line = f_2.readlines()
    for index, value in enumerate(x_line, 1):
        n_slov = len(value.split())
        print(f'В строке номер {index} имеется {n_slov} слов')

Task 4
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Fife': 'Пять', 'Six': 'Шесть'}
with open('file_123456', 'w', encoding='utf-8') as file_1:
  with open('file_88', encoding='utf-8') as file_2:
    file_1.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in file_2])


 Task 5
from random import randint

with open('a_1.text', 'w', encoding='utf-8') as file_2:
  list = [randint,(1, 100) for i in range(100)]
  file_2.write(''.join(map(str, list)))
print(f'Сумма равна - {sum(list)})


Task_6

with open('task_6.txt', 'encoding=utf-8') as u_file:
  x = u_file.readlines()
  for b in x:
    str_1 = ''.join((i if i in '0123456789' else ' ' for i in b))
    str_2 = [int(i) for i in str_1.split()]
    print(f'{b.split()[0]} {sum(str_2)}')



Task_7

import json


with open('L_7.json', 'w', encoding='utf-8') as write.f:
  with open ('l_7.txt', encoding='utf-8') as a_obj:
    dop = {line.split()[0]:  int(line.split()[2] - int(line.split()[3]) for line in a_obj}
    res = [dop, {'s_dop': round(sum([int(i) for i in dop.values() if int(i) > 0] / len([int(i) for i in dop.values() if int(i) > 0]))}]
  json.dump(res, write.f, ensure_ascii=False, indent=4)
'''












