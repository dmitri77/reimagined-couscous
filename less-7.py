#1

class Matrix:
    def __init__(self, spisok_spiskov):
        self.matrix = []
        for spisok in spisok_spiskov:
            self.matrix.extend([spisok])
    def __str__(self):
        outp = ""
        for elem_vert in self.matrix:
            for elem_horiz in elem_vert:
                outp += "  " + str(elem_horiz)
            outp += "\n"
        return outp
    def __add__(self, other):
        res = []
        width = len(self.matrix[0])
        height = len(self.matrix)
        for ind_vert in range(height):
            row = []
            for ind_horiz in range(width):
                row.append(self.matrix[ind_vert][ind_horiz]
                           + other.matrix[ind_vert][ind_horiz])
            res.extend([row])
        return Matrix(res)

spisok_spiskov1 = [[1, 2, 3], [4, 5, 6]]
spisok_spiskov2= [[2, 3, 4], [5, 6, 7]]
obj1 = Matrix(spisok_spiskov1);
print(obj1.matrix)
print(obj1)
obj2 = Matrix(spisok_spiskov2);
obj3 = obj1 + obj2
print(obj3)

#2

from abc import ABC, abstractmethod

class Odezhda(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def rashod():
        pass

class Palto(Odezhda):
    def __init__(self, name, razmer):
        super().__init__(name)
        self.razmer = razmer
    @property        
    def rashod(self):
        return self.razmer / 6.5 + 0.5
        
class Rost(Odezhda):
    def __init__(self, name, rost):
        super().__init__(name)
        self.rost = rost
    @property
    def rashod(self):
        return 2 * self.rost + 0.3

palto1 = Palto("Firmennoye", 50)
print(palto1.rashod)

#3
        
class Kletka:
    def __init__(self, kol):
        self.kol = kol 

    def __add__(self, other):
        return Kletka(self.kol + other.kol)

    def __sub__(self, other):
        if self.kol - other.kol > 0:
            return Kletka(self.kol - other.kol)
        else:
            print("sub ress less than zero. exit with error")
            return None

    def __mul__(self, other):
        return Kletka(self.kol * other.kol)
    
    def __truediv__(self, other):
         return Kletka(self.kol % other.kol)

    def make_order(self, row_len):
        rem = self.kol % row_len
        if rem != 0:
            rem_bool = 1
        else:
            rem_bool = 0

        for row in range(self.kol // row_len + rem_bool):
            for col in range(row_len):
                if col == self.kol % row_len and row == self.kol // row_len + rem_bool - 1:
                    break
                print("*", end="")
            print("")

k1 = Kletka(4)
k2 = Kletka(5)
k3 = k1 + k2

k3.make_order(4)
