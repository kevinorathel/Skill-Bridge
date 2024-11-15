# forms.py
from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerSignUp(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    address = forms.CharField(max_length=45, required=True)
    zipcode = forms.CharField(max_length=15, required=True)
    profile_picture = forms.ImageField(required=False)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password'],
            phone_no=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            zipcode=self.cleaned_data['zipcode'],
            profile_picture=self.cleaned_data.get('profile_picture'),
            role =1,
            type=1
        )

        if commit:
            user.save()

        # user.set_password(self.cleaned_data['password'])  # Use set_password to hash
        user.save()
        return user

class SpecialistSignUp(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    address = forms.CharField(max_length=45, required=True)
    zipcode = forms.CharField(max_length=15, required=True)
    profile_picture = forms.ImageField(required=False)
    dob = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True)
    experience = forms.ChoiceField(choices=[('entry', 'Entry Level'), ('mid', 'Mid Level'), ('senior', 'Senior Level')], required=True)
    languages = forms.CharField(max_length=100, required=True)
    linkedin = forms.URLField(required=True)
    resume = forms.FileField(required=False)
    skill_category = forms.ChoiceField(choices=[('plumber', 'Plumber'), ('driver', 'Driver'), ('painter', 'Painter'), ('electrician', 'Electrician'), ('carpenter', 'Carpenter')], required=True)
    qualification = forms.ChoiceField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('bachelors', 'Bachelors'), ('masters', 'Masters')], required=True)
    availability = forms.ChoiceField(choices=[('immediate', 'Immediate'), ('1week', 'In 1 Week'), ('2weeks', 'In 2 Weeks'), ('1month', 'In 1 Month')], required=True)
    willing_to_relocate = forms.BooleanField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password'],
            phone_no=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            zipcode=self.cleaned_data['zipcode'],
            profile_picture=self.cleaned_data.get('profile_picture'),
            date_of_birth=self.cleaned_data['dob'],
            gender=self.cleaned_data['gender'],
            experience_level=self.cleaned_data['experience'],
            languages_spoken=self.cleaned_data['languages'],
            linkedin_profile=self.cleaned_data.get('linkedin'),
            skill_category=self.cleaned_data['skill_category'],
            qualification=self.cleaned_data['qualification'],
            availability=self.cleaned_data['availability'],
            willing_to_relocate=self.cleaned_data.get('willing_to_relocate', False),
            role=1,
            type=2
        )
        # user.set_password(self.cleaned_data['password'])  # Use set_password to hash
        user.save()

        # Handle resume upload if provided
        if self.cleaned_data.get('resume'):
            user.resume = self.cleaned_data['resume']
            user.save()

        return user


