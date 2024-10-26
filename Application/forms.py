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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self):
        user = User(
            username=self.cleaned_data['username'],  # Use the correct username
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password'],
            phone_no=self.cleaned_data['phone_number'],  # Ensure this matches your model
            address=self.cleaned_data['address'],
            zipcode=self.cleaned_data['zipcode'],
            role=1,  # Set appropriate default values or handle them as needed
            type=1   # Set appropriate default values or handle them as needed
        )
        # user.set_password(self.cleaned_data['password'])  # Use set_password to hash
        user.save()  # This will call the save method in the User model
        return user

class SpecialistSignUp(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    address = forms.CharField(max_length=45, required=True)
    zipcode = forms.CharField(max_length=15, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self):
        user = User(
            username=self.cleaned_data['username'],  # Use the correct username
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password'],
            phone_no=self.cleaned_data['phone_number'],  # Ensure this matches your model
            address=self.cleaned_data['address'],
            zipcode=self.cleaned_data['zipcode'],
            role=1,  # Set appropriate default values or handle them as needed
            type=1   # Set appropriate default values or handle them as needed
        )
        # user.set_password(self.cleaned_data['password'])  # Use set_password to hash
        user.save()  # This will call the save method in the User model
        return user

