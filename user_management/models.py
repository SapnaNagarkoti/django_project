from email.policy import default

from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class customuser(AbstractUser):
    phone_number = models.CharField(default=None ,null=True)
    address = models.CharField(default=None,null=True)
    user_profile = models.ImageField(upload_to='image/',default=None,null=True)

    class Meta:
        db_table = 'auth_user'

