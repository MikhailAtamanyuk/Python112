class Book:
    name = ""
    year = ""
    publisher = ""
    genre = ""
    author = ""
    price = ""

    def input_book(self):
        self.name = input("Название книги: ")
        self.year = input("Год выпуска: ")
        self.publisher = input("Издатель: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = input("Цена: ")

    def read_book(self):
        print()
        print("Вывод")
        print("Название книги:", self.name)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def name_book(self):
        print()
        self.name = input("Название книги: ")
        print("Название книги:", self.name)

    def year_book(self):
        print()
        self.year = input("Год выпуска: ")
        print("Год выпуска:", self.year)

    def publisher_book(self):
        print()
        self.publisher = input("Издатель: ")
        print("Издатель:", self.publisher)

    def genre_book(self):
        print()
        self.genre = input("Жанр: ")
        print("Жанр:", self.genre)

    def author_book(self):
        print()
        self.author = input("Автор: ")
        print("Автор:", self.author)

    def price_book(self):
        print()
        self.price = input("Цена: ")
        print("Цена:", self.price)


b1 = Book()
b1.input_book()
b1.read_book()
b1.price_book()