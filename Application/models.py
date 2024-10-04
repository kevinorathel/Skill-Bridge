from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, null = True,unique=True)
    email = models.EmailField(unique=True)
    phone_no =  models.CharField(max_length=30)
    password = models.CharField(max_length=128, null = True)
    address = models.TextField()
    zipcode = models.CharField(max_length=30)
    role = models.IntegerField()
    type = models.IntegerField()
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        db_table = 'User'

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only hash the password if creating a new user
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
