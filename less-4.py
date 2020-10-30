#1

from sys import argv

vyrabotka_v_chasah, chasovaya_stavka, premiya = argv

print(vyrabotka_v_chasah * chasovaya_stavka + premiya)

#2

arr_i = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

arr_o = [arr_i[ind] for ind in range(1, len(arr_i)) if arr_i[ind]>arr_i[ind-1]]

print(arr_o)

#3

print([elem for elem in range(20, 241) if elem % 21 == 0 or elem % 20 == 0])

#4

arr_i = [2, 4, 2, 6, 3, 6]
arr_o = [elem for elem in arr_i if arr_i.count(elem) == 1] 
print(arr_o)

#5
from functools import reduce

def f(pred_elem, tek_elem):
    return pred_elem * tek_elem

print(reduce(f, range(100, 1001, 1)))
