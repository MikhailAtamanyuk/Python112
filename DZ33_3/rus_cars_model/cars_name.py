from sqlalchemy import Column, ForeignKey, Integer, String

from rus_cars_model.database_car import Base


class CarsName(Base):
    __tablename__ = 'list_name'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('price.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Название автомобиля: {self.id} - {self.name}'