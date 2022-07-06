from faker import Faker
from db.database import Session, create_db
from db.product import Product


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    vegetable_names = ["Картофель", "Морковь", "Огурец", "Помидор", "Кабачок", "Капуста",
                   "Баклажан", "Редис", "Лук", "Чеснок", "Свекла", "Редька"]

    faker = Faker('ru-Ru')

    for _ in range(20):
        name_product = faker.random.choice(vegetable_names)
        price = faker.random.randint(100, 1000)
        count = faker.random.randint(1, 20)
        product = Product(name_product, price, count)
        session.add(product)

    session.commit()
    session.close()
