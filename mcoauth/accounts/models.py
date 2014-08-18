from .managers import UserManager
from .abstract_models import AbstractUser


class User(AbstractUser):
    objects = UserManager()

    @property
    def username(self):
        return 'user%d' % self.pk

    def get_api_dict(self, base_url):
        minecraft_account = self.minecraft_accounts.primary()
        minecraft_account_data = minecraft_account.get_api_dict(base_url)

        data = {}
        data['primary_profile'] = minecraft_account_data
        data['email'] = self.email

        return data
