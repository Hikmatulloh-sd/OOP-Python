# Методы класса (classmethod) и статические методы (staticmethod) 

# Статические методы - @staticmethod - не имеет доступ не к атрибутам класса, не к атрибутам экземпляра 
# Методы класса - @classmethod - работает исключительно с атрибутами класса

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod     
    def validate(cls, arg):   # cls - сылка на текущий класс Vector 
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    
    def __init__(self, x, y):
        self.x =  self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(5, 6))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y): 
        return x*x + y*y
    
    
v = Vector(1, 2)
# print(Vector.norm2(5, 6)) 
# res = v.get_coord()
# print(res)