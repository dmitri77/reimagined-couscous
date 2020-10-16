
# 1

str1 = "test1\n";
str2 = "test2";
n1 = 1000;
n2 = 0.2032;

print(str1)
print(str2)
print("\n%d" % n1 )
print("\n%f" % n2 )

#2

#print(1 + 1*60 + 1*60*60)

#sec = int(input("\nВведите количество секунд: "))
sec = 100

hh = sec // (60*60)
hh_rem = sec % (60*60)

mm_rem = hh_rem % 60
mm = hh_rem // 60

print("\n%d:%d:%d" % (hh, mm, mm_rem) )

#3

#num1 = input("\nВведите число: ")
num1 = 3
num2 = num1 + num1
num3 = num1 + num1 + num1
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print(num1 + num2 + num3)

#4

#num = input("\nВведите число: ")
num = "123"
max = 0
for c in num:
    if max < int(c):
        max = int(c)
print("\nСамая большая цифра в числе: %d" %max)

#5:

#inc = input("\nВведите сумму выручки: ")
inc = "100"
#exp = input("\nВведите сумму затрат: ")
exp = "50"

if int(inc) > int(exp):
    print ("Прибыль: %d" %(int(inc) - int(exp)))
    sotr = input("\nВведите число сотрудников: ")
    print ("Прибыль на сотрудника: %d" %((int(inc) - int(exp)) / int(sotr)))
else:
    print ("Убыток: %d" %(-int(inc) + int(exp)))

#6:
a = int(input("\nВведите a: "))
b = int(input("\nВведите b: "))


tek = a
den = 0
while tek <= b:
    den = den + 1
    tek = tek + 0.1 * tek
print("За %d дня" % den )



