
class AuthenticationService:
    def __init__(self, user_repo):
        self.user_repo = user_repo()
    def authentication(self, user):
        self.user_repo.get_all_users().filter()