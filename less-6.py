#1

import time

class Svetofor:
    __curr_index = 0;    
    color_durations = (("Red",2), ("Yellow",1), ("Green",2), ("Yellow",1))
    
    def switch_color(self):
        if self.__curr_index == 3:
            self.__curr_index = 0
        else:
            self.__curr_index += 1

    def startDelay(self):
        time.sleep(self.color_durations[self.__curr_index][1])

    def getColor(self):
        return self.color_durations[self.__curr_index][0]
    
ob = Svetofor()

for ind in range(10):
    print(ob.getColor())
    ob.startDelay()
    ob.switch_color()

#2

class Road:
    __length = 0;
    __width = 0;
    __factor = 25*5/1000
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def calcMass(self):
        return self.__width * self.__length * self.__factor
        
ob = Road(5000, 10)
print(ob.calcMass())

3

class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}
    def __init__(self, worker_init):
        self.name = worker_init["name"]
        self.surname = worker_init["surname"]
        self.position = worker_init["position"]
        self._income["wage"] = worker_init["wage"]
        self._income["bonus"] = worker_init["bonus"]

class Position(Worker):
    def __init__(self, worker_init):
        super().__init__(worker_init)
    def get_full_name(self):
        return self.name + " " + self.surname        
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]        

worker_dict = {"name": "John", "surname": "Smith", "position": "manager", "wage": 30000, "bonus": 5000}

pos_obj = Position(worker_dict)
print(pos_obj.get_full_name())
print(pos_obj.get_total_income())

#4

class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False
    in_motion = False
    direction = ""
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.in_motion = False
        self.direction = direction
    def go(self):
        self.in_motion = True     
    def turn(self, dir):
        self.dir = dir        
    def stop(self):
        self.in_motion = false
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, False, direction)
    def show_speed(self):
        if self.speed > 60:
            return "Speed exceeded"
        else:
            return self.speed

class SportCar(Car):
   def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, False, direction)

class WorkCar(Car):
    def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, False, direction)
    def show_speed(self):
        if self.speed > 40:
            return "Speed exceeded"
        else:
            return self.speed

class PoliceCar(Car):
   def __init__(self, speed, color, name, direction):
        super().__init__(speed, color, name, True, direction)

WorkCarObj = WorkCar(0, "Blue", "Chevralier", "NW")
WorkCarObj.go()
WorkCarObj.speed = 100
print(WorkCarObj.show_speed())

#5

class Stationery:
    title = ""
    def __init__(self, name):
        self.title = name
    def draw(self):
        return print("Запуск отрисовки")
    
class Pen(Stationery):
    def __init__(self, name):
        super().__init__(name)
    def draw(self):
        return print("Запуск отрисовки ручкой")   

class Pencil(Stationery):
    def __init__(self, name):
        super().__init__(name)
    def draw(self):
        return print("Запуск отрисовки караднашом")

class Handle(Stationery):
    def __init__(self, name):
        super().__init__(name)
    def draw(self):
        return print("Запуск отрисовки хэндлом")

pen_obj = Pen("Parker")
pen_obj.draw()
    

        

        
