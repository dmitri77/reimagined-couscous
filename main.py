####1

def func(a, b):
    try:
        c = a/b
        print (c)
    except:
        print("Деление на ноль")

a, b = input("Введите два числа через пробел: ").split(" ")

func(a, b)

##2

def func(name="Не зап.", surn="Не зап.", yob="Не зап.", city ="Не зап.", email="Не зап.", tel="Не зап."):
    print(f"Введенные данные: Имя: {name} | Фамилия: {surn} | Год рождения: {yob}| Город проживания: {city}| Email: {email}| Телефон: {tel}")

name = input("Введите имя: ")
surn = input("Введите фамилию: ")
yob = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
tel = input("Введите телефон: ")

func(name, surn, yob=, city, email, tel)

##3

def my_func(a, b, c):
    d = max(list(a, b, c))
    return d

print(my_func(5, 3, 8))

##4

def my_func1(a, b):
    c = a ** b
    return c

def my_func2(a, b):
    ind = 1
    c = 1
    while ind <= -b:
        c = c * a
        ind += 1
    return 1/c

print(my_func1(5, -3))

print(my_func2(5, -3))

####5

def posledniye_dva_vvoda_byli_chislami(arr):
    m = len(arr) - 1
    ok = true
    while ind >= m:
        if is_integer(arr[ind]) != true:
            ok = false
        m += -1
    return ok

s = 0
arr = []
while (1 == 1):
    arr = input("Вводите числа через пробел (введите # и нажмите enter для выхода после как минимум 2-х чисел через пробел): ").split(" ")
    if arr[len(arr) - 1] == "#" & posledniye_dva_vvoda_byli_chislami(arr):
        s = s + sum([ int(chis_str) for chis_str in arr[1:len(arr)-1] ])
        print (s)
        break
    elif arr[len(arr) - 1] != "#":
        s = s + sum([ int(chis_str) for chis_str in arr[1:len(arr)-1] ])
        print(s)   

##6

def int_func(str):
    return str.capitalize()

arr = input("Введите несколько слов латинскими буквами: ").split(" ")
arr = map(lambda elem: int_func(elem) + "", arr)
print(" ".join(arr))




