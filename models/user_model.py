from sqlalchemy import Column, Integer, String


from database.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f'User: id:{self.id}, fullname:{self.fullname}, login:{self.login}.'
