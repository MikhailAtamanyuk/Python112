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