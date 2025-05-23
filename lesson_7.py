# Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__ 
# __setattr__(self, key, value)__ - автоматически вызываеться при изменении свойства key класса
# __getattribute__(self, item) - автоматический вызываеться при получении свойства класса с именем item
# __getattr__(self, item) - автоматичеки вызываеться при получении  несуществуюшего свойства item класса 
# __delattr__(self, item) - автоматически вызываеться при удалении свойства item (не важно: сущетвует оно или нет)


class Point:
    # Атрибуты класса обшие для всех экзепмляров 
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coord(self, x, y):
        self.x = x
        self.y = y 

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left
    
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ запещен')
        # print('__getattribute__')
        else:
            return object.__getattribute__(self, item)
    
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('не допустимое имяя атрибута')
        # print('__setattr__')
        else:
            object.__setattr__(self, key, value)
            # self.__dict__[key] = value # чтобы не вызвать рекурсию 
        
    def __getattribute__(self, item):
        # print('__getattr__: ' + item )
        return False 

    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.yy)
del pt1.x
print(pt1.__dict__)