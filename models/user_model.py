import hashlib
import os
class User:
    def __init__(self, name, password, physical_stats_id):
        self.name = name
        self.physical_stats = physical_stats_id
        self.hashed_password = self._hash_password_with_salt(password)

    def _verify(self, salt, key, password):
        new_key = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt, 100000)
        if new_key == key:
            return True
        else:
            return False

    def _hash_password_with_salt(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 100000, dklen=128)
        return {'key': key, 'salt': salt}
