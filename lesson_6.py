from accessify import private, protected

# Режимы доступа public, private, protected. Сеттеры и геттеры

# Маханизм инкапсуляции 
# attribute (без подчеркивании в начале) - публичное свойства (public)
# _attribute (с одним подчеркиванием) - режим доступа protected (служит для обращение вунтри класса и во всех его дочерных классах)
# __attribute (с двумя подчеркиванием) - режим доступа private (служит для обращение только внутри класса)

# Интерфейсные методы
# геттеры и сетторы - для изменение получение привятных атрибутов


class Point:
    def __init__(self, x=0, y=0):
        self.x = self.y = 0 
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
    
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y  
        else:
            raise ValueError('Кординаты должны быть числами')
    
    @private
    @classmethod    
    def __check_value(cls, x):
        return type(x) in (int, float)

    def get_coords(self):
        return self.__x, self.__y    
    

pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coords())
