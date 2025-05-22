class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @staticmethod
    def is_square(length, width):
        return length == width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def info(self):
        return f"Прямоугольник: длина={self.length}, ширина={self.width}, площадь={self.area()}, периметр={self.perimeter()}"


class RectangleAnalyzer:
    rectangles = []

    @classmethod
    def add_rectangle(cls, rectangle):
        cls.rectangles.append(rectangle)

    @classmethod
    def count_squares(cls):
        return sum(1 for rect in cls.rectangles if Rectangle.is_square(rect.length, rect.width))

    @classmethod
    def average_area(cls):
        if not cls.rectangles:
            return 0
        total_area = sum(rect.area() for rect in cls.rectangles)
        return total_area / len(cls.rectangles)

    @classmethod
    def print_all(cls):
        for rect in cls.rectangles:
            print(rect.info())


class Logger:
    log_level = 'INFO'

    @classmethod
    def change_level(cls, level):
        cls.log_level = level

    def log(self, msg):
        print(f"{self.log_level}: {msg}")


# --- Тестирование ---

# Создаём прямоугольники
r1 = Rectangle(4, 4)    # квадрат
r2 = Rectangle(3, 5)
r3 = Rectangle(6, 6)    # квадрат
r4 = Rectangle(2, 7)

# Добавляем их в анализатор
RectangleAnalyzer.add_rectangle(r1)
RectangleAnalyzer.add_rectangle(r2)
RectangleAnalyzer.add_rectangle(r3)
RectangleAnalyzer.add_rectangle(r4)

# Используем логгер
logger = Logger()
logger.log("Добавлены 4 прямоугольника.")

# Меняем уровень логгирования
Logger.change_level("DEBUG")
logger.log("Печатаем информацию по каждому прямоугольнику:")

# Выводим информацию о всех прямоугольниках
RectangleAnalyzer.print_all()

# Выводим статистику
print("Количество квадратов:", RectangleAnalyzer.count_squares())
print("Средняя площадь всех фигур:", RectangleAnalyzer.average_area())
