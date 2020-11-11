from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy.orm import sessionmaker
SQLITE = 'sqlite'

USERS = 'users'
PHYSICAL_STATS = 'physical_stats'
FOOD = 'food'

class Database:
    DB_ENGINE={
        SQLITE: 'sqlite:///{DB}'
    }
    db_engine = None
    def create_db_tables(self):
        Base.metadata.create_all(self.db_engine)
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url, echo = True)#TODO remove echo in production
            self.session = sessionmaker(bind = self.db_engine)
            print(self.db_engine)
            self.create_db_tables()
        else:
            raise Exception("DBType is not found in DB_ENGINE.")

    # def create_db_tables(self):
    #     metadata = MetaData()
    #     self.users = Table(USERS, metadata,
    #                   Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    #                   Column('full_name', String),
    #                   Column('login', String, unique=True),
    #                   Column('password', String),
    #                   )
    #     self.physical_stats = Table(PHYSICAL_STATS, metadata,
    #                             Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    #                             Column('weight', Integer),
    #                             Column('height', Integer),
    #                             Column('age', Integer),
    #                             Column('gender', String),
    #                             Column('level_of_activity', String),
    #                             Column('user_id', None, ForeignKey('users.id'))
    #                            )
    #     self.foods = Table(FOOD, metadata,
    #                   Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
    #                   Column('name',String, unique= True),
    #                   Column('carbs', Float),
    #                   Column('fats', Float),
    #                   Column('proteins', Float)
    #                   )
    #     try:
    #         metadata.create_all(self.db_engine)
    #         print("Tables created.")
    #     except Exception as e:
    #         print("Error occurred during Table creations.")
    #         print(e)
