from django.contrib.auth.base_user import BaseUserManager
from utils.messages import get_msg

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(get_msg('no_username'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save()

        return user
    
    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and saves a superuser with the give username and password.
        """
        user = self.create_user(
            username,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    def instance(self, user):
        # This method is called when `user` is request.user
        return self.get(username=user.username)

    def authenticate(self, user, password):
        return user.check_password(password)