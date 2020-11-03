#1

file = open("text.txt", "w")

while str != "":
    str = input("Введите строку ")
    if str != "":
        file.write(str)
        
#2

file = open("text.txt", "r")

try:
    contents = file.readlines()
    print(f"В файле {len(contents)} строк")
    c = 1
    for str in contents:
        print(f"В строке {c} {len(str.split(' '))} слов")
        c += 1
except:
    print("Ошибка")
finally:
    file.close()

#3

import re

with open("text.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()
_sum = 0
_max = 0
_name = ""
for _str in contents:
    str_arr = _str.split(' ')
    str_arr[1] = re.sub("[^0-9]", "", str_arr[1])
    if int(str_arr[1]) > _max:
        _max = int(str_arr[1])
        _name = str_arr[0]
        _sum += int(str_arr[1])
print(f"Макс. зарплата = {_max} у {_name}, средняя зарплата = {_sum / len(contents)}")       
   
#4


with open("text.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()

sootv = {"Оne": "Один", "Two": "Два", "Three": "Три"}

for _str in contents:
    str_arr = _str.split(' — ')
    str_arr[0] = sootv.get(str_arr[0])
    _str = " — ".join(str_arr)

with open("text.txt", "w", encoding='utf-8') as file:
    file.writelines(contents)   

#5

from random import random

arr = []
with open("text.txt", "w", encoding='utf-8') as file:
    for ind in range(10):
        arr.append(str(random()) + " ")
        arr = arr[1:len(arr)-1] + "\n"
    file.writelines(arr)
        
with open("text.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()

int_arr = contents[0].split(" ")

sum = 0
for elem in int_arr:
    sum = sum + int(elem)

print(f"Сумма:{sum}")

              
              
