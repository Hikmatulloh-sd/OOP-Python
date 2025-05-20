# Методы классов. Параметр self.

# метод - действие, именно поэтому в названиех методов использует глаголы 
# имена свойств - существительное 


class Point:
    color = 'red'
    circle = 2 

    def set_coords(self, x, y):
        self.x = x
        self.y = y 

    def get_coords(self):
        return (self.x, self.y)
        

pt = Point()
pt.set_coords(1, 2)
# print(pt.__dict__)
print(pt.get_coords())

f = getattr(pt, 'get_coords')
print(f())