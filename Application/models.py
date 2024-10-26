from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, null=True, unique=True)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=30)
    password = models.CharField(max_length=128, null=True)
    address = models.TextField()
    zipcode = models.CharField(max_length=30)
    role = models.IntegerField()
    type = models.IntegerField()
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)  # new field
    gender = models.CharField(max_length=10, null=True, blank=True)  # new field
    experience_level = models.CharField(max_length=20, null=True, blank=True)  # new field
    languages_spoken = models.CharField(max_length=255, null=True, blank=True)  # new field
    linkedin_profile = models.URLField(null=True, blank=True)  # new field
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # new field
    skill_category = models.CharField(max_length=30, null=True, blank=True)  # new field
    qualification = models.CharField(max_length=30, null=True, blank=True)  # new field
    availability = models.CharField(max_length=20, null=True, blank=True)  # new field
    willing_to_relocate = models.BooleanField(default=False)  # new field

    class Meta:
        db_table = 'User'


    # def save(self, *args, **kwargs):
    #     if self.pk is None:  # Only hash the password if creating a new user
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)
