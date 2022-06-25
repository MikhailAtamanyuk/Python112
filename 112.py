import random
import time

w = int(input("Размерность массива: "))
m = [[random.randint(0, 100) for x in range(w)] for y in range(w)]
print("Массив из случайных чисел от 0 до 100: ")
for row in m:
    for col in row:
        print(col, end="\t")
    print()
m1 = []
i = 0
for row in m:
    for col in row:
        m1.append(row[i])
        break
    i += 1
print("Минимальный элемент массива: ", min(m1))
print("Максимальный элемент массива: ", max(m1))
# _________________________________________________________
w = 6
m = [[random.randint(0, 10) for x in range(w)] for y in range(w)]
m1 = [random.randint(0, 10) for i in range(w)]
for row in m:
    for col in row:
        print(col, end="\t")
    print()
print(m1)
print()
i = 0
while i < len(m):
    m.pop(i)
    m.insert(i, m1)
    i += 2
for row in m:
    for col in row:
        print(col, end="\t")
    print()
# _________________________________________________________
import locale

# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня: %B %d, %Y", time.localtime()))

print("Hello, World!")
# _________________________________________________________
shapes = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))


def rectangle(height, width):
    return print("Площадь прямоугольника: ", height*width)


def triangle(height, width):
    return print("Площадь треугольника: ", (height*width)/2)


def circle(height):
    return print("Площадь круга: ", pi*height**2)


if shapes == 1:
    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    rectangle(a, b)
elif shapes == 2:
    a = int(input("Введите первый катет: "))
    b = int(input("Введите второй катет: "))
    triangle(a, b)
elif shapes == 3:
    a = int(input("Введите радиус круга: "))
    circle(a)
else:
    print("Введите от 1 до 3")
print()
# _________________________________________________________
s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))
s1 = set("Python")
s2 = set("Programming language")
s3 = s1 - s2
print("Искомыми буквами являются: ")
for i in s3:
    print(i, end=" ")
# _________________________________________________________
s=input("Введите строку: ")
s = "Привет, мир!"
vowels = "аяоёуюыиэе"
def count_vowels(st):
    return sum([1 for x in s.lower() if x in vowels])

print("Количество гласных равно:", count_vowels(s))
# _________________________________________________________
s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))
s1 = set("test")
s2 = set("string")
s3 = s1 | s2
print("Искомыми буквами являются: ")
for i in s3:
    print(i, end=" ")
# _________________________________________________________
s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))
s1 = set("hello")
s2 = set("world")
s3 = s1 ^ s2
print("Искомыми буквами являются: ")
for i in s3:
    print(i, end=" ")
# _________________________________________________________
ls = [3, 6, 8, 9, 1, 2]
print(list(map(lambda x: ls.index(x) ** 2 * ls.index(x) * x, ls)))
print()
# _________________________________________________________
a = 5
print(type(a))
print(type(int))
# _________________________________________________________
import requests
from bs4 import BeautifulSoup
import csv

url = "https://yandex.ru/news"

quotes = []
page = 1

while True:
    r = requests.get(url.format(page))
    print(r.url)
    soup = BeautifulSoup(r.content, 'html5lib')

    if not soup.select_one("#all_quotes .text-center > a"):break
    for row in soup.select("#all_quotes .text-center"):
        quote = {}
        try:
            quote['quote'] = row.select_one('a img.shadow').get("alt")
        except AttributeError:
            quote['quote'] = ""
        try:
            quote['url'] = row.select_one('a').get('href')
        except AttributeError:
            quote['url'] = ""
        try:
            quote['img'] = row.select_one('a img.shadow').get('src')
        except AttributeError:
            quote['img'] = ""
        quotes.append(quote)

    page += 1

with open('yandex.csv', 'w', newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, ['quote', 'url', 'img'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)


if __name__ == '__main__':
    main()
# _________________________________________________________
class Controller:
    def __init__(self):
        self.article_model = FilmModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.user_interface.add_film()
            self.article_model.add_film(film)
        elif answer == "2":
            films = self.article_model.get_cat_films()
            self.user_interface.show_cat_films(films)
        elif answer == "3":
            film_name = self.user_interface.get_user_film()
            try:
                film = self.article_model.get_single_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_film_name_error(film_name)
            else:
                self.user_interface.show_single_film(film)
        elif answer == "4":
            film_name = self.user_interface.get_user_film()
            try:
                film = self.article_model.remove_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_film_name_error(film_name)
            else:
                self.user_interface.remove_single_film(film)
        elif answer == "q":
            self.article_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)



# _______________________________________________________________________________________________

import pickle
import os.path


class Film:
    def __init__(self, name, genre, reg, year, time, prod, actors):
        self.name = name
        self.genre = genre
        self.reg = reg
        self.year = year
        self.time = time
        self.prod = prod
        self.actors = actors

    def __str__(self):
        return f"{self.name} режиссер {self.reg}"


class FilmModel:
    def __init__(self):
        self.db_name = "db_name.txt"
        self.films = self.load_data()

    def add_film(self, dict_films):
        film = Film(*dict_films.values())
        self.films[film.name] = film

    def get_cat_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_films = {"название фильма": film.name,
                      "жанр": film.genre,
                      "режиссер": film.reg,
                      "год выпуска": film.year,
                      "длительность": film.time,
                      "студия": film.prod,
                      "актеры": film.actors}
        return dict_films

    def remove_film(self, film_name):
        return self.films.pop(film_name)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as file:
            pickle.dump(self.films, file)



# _______________________________________________________________________________________________



def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        print("Действия с фильмами: ")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добаление фильма")
    def add_film(self):
        dict_films = {"название фильма": None,
                      "жанр": None,
                      "режиссер": None,
                      "год выпуска": None,
                      "длительность": None,
                      "студия": None,
                      "актеры": None}
        for key in dict_films:
            dict_films[key] = input(f"Введите {key} фильма: ")
        return dict_films

    @add_title("Каталог фильмов:")
    def show_cat_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @add_title("Ввод названия фильма: ")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма: ")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Ошибка: ")
    def show_incorrect_film_name_error(self, film_name):
        print(f"Фильм с названием '{film_name}' не существует")

    @add_title("Удаление фильма: ")
    def remove_single_film(self, film):
        print(f"Фильм с названием '{film}' удален")

    @add_title("Ошибка: ")
    def show_incorrect_answer_error(self, answer):
        print(f"Вариант с названием '{answer}' не существует")



# _______________________________________________________________________________________________



def main():
    app = Controller()
    app.run()


if __name__ == "__main__":
    main()

# _______________________________________________________________________________________________
import sqlite3 as sq


with sq.connect('cars.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)

    cur.execute("")

# con.commit()
# con.closer()


