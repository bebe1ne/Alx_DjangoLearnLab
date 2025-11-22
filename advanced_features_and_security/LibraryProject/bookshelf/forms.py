from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth", "profile_photo")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth", "profile_photo")

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, required=True)
    another_field = forms.IntegerField(required=False)

    def clean_example_field(self):
        data = self.cleaned_data['example_field']
        # Perform some validation or transformation on example_field
        return data
