##1

list_ = [100, "test", None, 1==1, (1,1,2,3), {1,2,3},
         {'key1': set([1,1,2,3]), 'key2': dict(key0='val0')},
         bytes('test', encoding = 'utf-8')]
print(list_)

##2

list_ = []
print("Введите список значений:")
for x in range(4):
    elem = input(x)
    list_.append(elem)

l_ = [1, 5, 2, 6, 3, 7]

if len(l_) % 2 == 0:
    for x in range(len(l_) // 2):
        l_[x*2], l_[x*2 + 1] = l_[x*2 + 1], l_[x*2]
print(l_)

##3

months_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
months_dict = {'1':"Январь", '2':"Февраль", '3':"Март", '4':"Апрель", '5':"Май", '6':"Июнь", '7':"Июль", '8':"Август", '9':"Сентябрь", '10':"Октябрь", '11':"Ноябрь", '12':"Декабрь"}
nom = input("Введите номер месяца:")
print(months_list[int(nom) - 1])
print(months_dict[nom])

##4
str_ = input("Введите строку из слов и пробелов:")
arr = str_.split(" ")
for i, elem in enumerate(arr):
    if len(elem) > 10:
        print(i + 1, elem[0:10])
    else:
        print(i + 1, elem)

##5
l_ = [9, 7, 5, 5, 3]
n = input("Введите число: ")
l_.append(n)
l_.sort()
l_.reverse()
print(l_)
