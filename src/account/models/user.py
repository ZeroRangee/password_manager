import uuid
from django.db import models
from account.manager import UserManager
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=False)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.username if self.username else str( _("noname"))

    class Meta:
        db_table = "user"
        ordering = ('email', )
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
