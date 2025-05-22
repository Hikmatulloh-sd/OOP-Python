class User:
    country = 'Uzbekistan'  # атрибут класса

    def __init__(self, name, age):
        self.name = name    # атрибут экземпляра
        self.age = age

    def __del__(self):  # финализатор
        print(f"Объект {self} удалён!")

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

    def set_info(self, name, age):
        self.name = name
        self.age = age


# Создание объекта
user_1 = User('hikmatulloh', 17)
user_1.say_hello()

# Атрибут класса через объект и через класс
print(user_1.country)       # Uzbekistan
print(User.country)         # Uzbekistan

# Изменим атрибут ТОЛЬКО у объекта
user_1.country = 'Kyrgyzstan'
print(user_1.country)       # Kyrgyzstan
print(User.country)         # Uzbekistan

# Второй объект
user_2 = User('zakariya', 21)
user_2.say_hello()
print(user_2.country)       # Uzbekistan — не изменился

# Вызов метода set_info
user_2.set_info('umar', 30)
user_2.say_hello()

# __dict__ объекта
print("Объект user_1:", user_1.__dict__)
print("Объект user_2:", user_2.__dict__)

# __dict__ класса
print("Класс User:", User.__dict__)

del user_1
