from faker import Faker

from rus_cars_model.database_car import create_db, Session
from rus_cars_model.cars_name import CarsName
from rus_cars_model.price import Price


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    car_names = ['КамАЗ', 'УАЗ', 'ГАЗ', 'АвтоВАЗ', 'Лада', 'ЛиАЗ', 'УралАЗ']

    for key, it in enumerate(car_names):
        car = CarsName(name=it)
        session.add(car)

    faker = Faker('ru-Ru')
    session.commit()

    for _ in range(7):
        price = faker.random.randint(500000, 1000000)
        price_car = Price(price)
        session.add(price_car)

    session.commit()
    session.close()