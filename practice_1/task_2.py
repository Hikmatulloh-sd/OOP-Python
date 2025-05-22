class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

book_1 = Book("Приступление и Наказание", "Федр Достаевский")

print(getattr(book_1, 'title'))
setattr(book_1, 'author', 'Fedr Dostaevskiy')
print(book_1.author)
delattr(book_1, 'author')
print(hasattr(book_1, 'author'))
