# Инициализатор __init__ и финализатор __del__ .


class Point:
    color = 'red'
    circle = 2 

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __del__(self):
        print("Удаление эгземпляра" + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y 

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1, 2)
print(pt.__dict__)


# __имя магического метода__

# __init__(self) - инициализатор объекта класса 
# __del__(self) - финализатор класса 

# Когда на какой-то объект введет хотябы одна внешная сылка - он считаеться нужным 
# Как только проподает все внешные сылки, сборшик мусора автоматический удаляет объект. 
# Перед удаление этого объекта будет вызван магический метод __del__