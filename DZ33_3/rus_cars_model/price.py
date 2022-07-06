from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from rus_cars_model.cars_name import CarsName
from rus_cars_model.database_car import Base


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    carnames = relationship('CarsName')

    def __init__(self, price):
        self.price = price

    def __repr__(self):
        return f'Цена авто: {self.id} - {self.price}'