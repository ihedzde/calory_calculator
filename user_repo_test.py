import unittest

from repositories.user_repository import UserRepository


class UserRepoTest(unittest.TestCase):
    def test_get_all_user(self):
        repo = UserRepository()
        self.assertEquals(repo.get_all_user(),[], 'My message')

if __name__ == '__main__':
    unittest.main()
