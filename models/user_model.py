import hashlib
import os

from sqlalchemy import Column, Integer, String


from database.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f'<User: id:{self.id}, fullname:{self.fullname}, login:{self.login}.'



# TODO put hashing and verefications in services
# TODO add authentification service
# def _verify(self, salt, key, password):
#     new_key = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt, 100000)
#     if new_key == key:
#         return True
#     else:
#         return False
# def _hash_password_with_salt(self, password):
#     salt = os.urandom(32)
#     key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 100000, dklen=128)
#     return {'key': key, 'salt': salt}
