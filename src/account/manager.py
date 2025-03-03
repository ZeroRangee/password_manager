from django.contrib.auth.models import UserManager

class UserManager(UserManager):
    
    def create_user(self, email=None,**extra_fields):
        if not email:
            raise ValueError('Электронная почта не заполнена')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user
    