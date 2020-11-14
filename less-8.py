#1

import re

class _Date():
    def __init__(self, str):
        self.input = str
    @classmethod
    def extracter(cls, str):
        _list = str.split("-")
        return [int(elem) for elem in _list]
    @staticmethod
    def check(_list):
        print(_list)
        for ind in range(3):
            pattern = re.compile("\d[0-30-1]-\d[0-10-9]\d[0-90-90-90-9]")
            if pattern.match(str(_list[ind])) == None:
                print("Не все являются числами. Ошибка.")
                break
        
obj = _Date("32-12-2020")
_list = _Date.extracter(obj.input)
_Date.check(_list)

#2

class _Error(Exception):
    def __init__(self, txt):
        self.txt = txt
        print("Error!")

a = 5
b = 0

try:
    a/b
except Exception as e:
    if str(e) == "division by zero":
        err = _Error(ZeroDivisionError)

#3

class IntChecker(ValueError):
    def __init__(self, txt):
        self.txt = txt

spis = []
print("Введите список чисел: ")
while True:
    inp = input()
    if inp == "stop":
        break
    try:
        try:
            test = int(inp)
        except ValueError as e:
            raise IntChecker("Только числа")
    except IntChecker as e:
        print(e)
    else:
        spis.append(inp)
        print("добавлено")        
       
print(spis)

#4, 5, 6

class SkladOrgtehniki():
    def __init__(self, kol_mest):
        self.kol_mest = kol_mest
        self.shelves = {elem : "" for elem in range(kol_mest)}

    def prinyat_na_sklad(self, arr):
        for elem in arr:
            for ind in range(elem.get("quantity")):
                self.__prinyat(elem.get("tehnika"))
                
    def __prinyat(self, item):
        key = ""
        for elem in self.shelves:
            if self.shelves.get(elem) == "":
                key = elem
                break
        if key == "":
            print("Нет места!")
            return False
        self.shelves.update({key: item})
        return True
  
    def peredat_v_podrazdeleniye(self, nazvaniye_orgtehniki):
        for elem in self.shelves:
            if self.shelves.get(elem).__class__.__name__ == nazvaniye_orgtehniki:
                ret = self.shelves.get(elem)
                self.shelves.update({elem: ""})
                return ret
        print("Больше нет!")
        return None

class Orgtehnikа:
    def __init__(self, tip):
        self.tip = tip

class Printer(Orgtehnikа):
    def __init__(self, tip, manufacturer, model, laser):
        super().__init__(tip)
        self.manufacturer = manufacturer
        self.model = model
        self.laser = laser
        
class Scanner(Orgtehnikа):
    def __init__(self, tip, manufacturer, model, speed):
        super().__init__(tip)
        self.manufacturer = manufacturer
        self.model = model
        self.speed = speed
        
class Photocopyer(Orgtehnikа):
    def __init__(self, tip, manufacturer, model, size):
        super().__init__(tip)
        self.manufacturer = manufacturer
        self.model = model
        self.size = size
        
obj = SkladOrgtehniki(5)

spis = [{"tehnika": Printer("Комп. техника", "Verizon", "ZX-1100", "true"), "quantity": 2},
{"tehnika": Scanner("Комп. техника", "Cadillac", "RTX-1000", "very fast"), "quantity": 1},
{"tehnika": Photocopyer("Офисная техника", "Xerox", "GR-900", "large"), "quantity": 1}];    

obj.prinyat_na_sklad(spis)
print(obj.shelves)
obj.peredat_v_podrazdeleniye("Printer")
print(obj.shelves)

#7

class ComplNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}j"
        if self.b < 0:
            return f"{self.a} - {-self.b}j"

    def __mul__(self, other):
        return ComplNum(self.a*other.a - self.b*other.b, self.b*other.a + self.a*other.b)

cn1 = ComplNum(2,4)
cn2 = ComplNum(0,-200)

print(cn1)
print(cn1*cn2)

