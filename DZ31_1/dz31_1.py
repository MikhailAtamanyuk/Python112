import sqlite3 as sq

goods = [
    (1, 'Творог', 80),
    (1, 'Масло сливочное', 100),
    (1, 'Сметана', 90),
    (1, 'Йогурт', 85),
    (2, 'Сок', 95),
    (2, 'Газировка', 50),
    (2, 'Вода', 40),
    (3, 'Бумага туалетная', 110),
    (3, 'Влажные салфетки', 90),
    (3, 'Мыло', 120)
]
sellers = [
    (1, 'Молочные продукты'),
    (2, 'Напитки'),
    (3, 'Товары 1-ой необходимости')
]

with sq.connect("orders.db") as con:
    cur = con.cursor()
    cur.executescript(
        """CREATE TABLE IF NOT EXISTS prod(
        kod_sale INTEGER,
        product TEXT,
        price INTEGER,
        FOREIGN KEY (kod_sale)  REFERENCES sellers(id));
        CREATE TABLE IF NOT EXISTS sellers(
        id INTEGER PRIMARY KEY,
        seller TEXT,
        FOREIGN KEY (id)  REFERENCES prod(kod_sale))
        """)
    cur.executemany("INSERT INTO prod VALUES(?, ?, ?)", goods)
    cur.executemany("INSERT INTO sellers VALUES(?, ?)", sellers)
