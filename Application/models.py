from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
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
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    experience_level = models.CharField(max_length=20, null=True, blank=True)
    languages_spoken = models.CharField(max_length=255, null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skill_category = models.CharField(max_length=30, null=True, blank=True)
    qualification = models.CharField(max_length=30, null=True, blank=True)
    availability = models.CharField(max_length=20, null=True, blank=True)
    willing_to_relocate = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'


    # def save(self, *args, **kwargs):
    #     if self.pk is None:  # Only hash the password if creating a new user
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"
