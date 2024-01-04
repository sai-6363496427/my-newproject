from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class media(models.Model):
#    image  = models.ImageField(upload_to="user_image/",blank=True)


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)



