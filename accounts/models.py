from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


# Custom user model 
class User(AbstractUser):
    mobile_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)], blank=True)
    profile_pic = models.ImageField(upload_to="profile/", null=True)