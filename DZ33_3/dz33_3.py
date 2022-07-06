import os
from sqlalchemy import and_, or_, not_, delete

from rus_cars_model.database_car import DATABASE_NAME, Session
import create_datebase_HW as db_creator

from rus_cars_model.cars_name import CarsName
from rus_cars_model.price import Price

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    print(session.query(Price).all())
    print(60*('*'))

    for it in session.query(CarsName):
        print(it)

    print(60 * ('*'))

    print(f'Всего {session.query(CarsName).count()} автомобилей')
    print(60 * ('*'))

    print(f'Первый в списке:\n {session.query(CarsName).first()}')
    print(60 * ('*'))

    print(f'Список цен которые дороже 500000')
    for i in session.query(Price).filter(Price.price > 500000):
        print(i)
    print(60 * ('*'))

    print('Список имен по ID >= 3 и начанается на "М"')
    for i in session.query(CarsName).filter(CarsName.id >= 3, CarsName.name.like('М%')):
        print(i)
    print(60 * ('*'))

    print('Список имен ID > 3 или начанается на "М"')
    for i in session.query(CarsName).filter(or_(CarsName.id > 3, CarsName.name.like('М%'))):
        print(i)
    print(60 * ('*'))

    print('Список имен ID не равен 3 и не начанается на "М"')
    for i in session.query(CarsName).filter(not_(CarsName.id == 3), not_(CarsName.name.like('М%'))):
        print(i)
    print(60 * ('*'))

    print('Список пустых колонок в таблице с именами')
    print(session.query(CarsName).filter(CarsName.name is None).all())
    print(60 * ('*'))

    print(f'Список имен : {session.query(CarsName).filter(CarsName.name.in_(["КамАЗ", "УАЗ"])).all()}')
    print(60 * ('*'))

    print(f'Список имен : {session.query(CarsName).filter(CarsName.id.between(4, 6)).all()}')
    print(60 * ('*'))

    session.query(CarsName).filter(CarsName.name.like('М%')).update({'name': 'Москвич'}, synchronize_session='fetch')
    session.commit()

    for i in session.query(CarsName):
        print(i)
    print(60 * ('*'))

    session.add(CarsName(name='КамАЗ'))
    session.commit()

    for i in session.query(CarsName):
        print(i)
    print(60 * ('*'))

    i = session.query(CarsName).filter(CarsName.name == 'КамАЗ').one()
    session.delete(i)
    session.commit()

    for i in session.query(CarsName):
        print(i)
    print(60 * ('*'))
