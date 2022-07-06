import os

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    print(session.query(Lesson).all())
