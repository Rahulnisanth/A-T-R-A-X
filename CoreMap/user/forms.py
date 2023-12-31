from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        custom_placeholders = {
            "username": "Username",
            "email": "Email",
            "password1": "Password",
            "password2": "Confirm password",
        }
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control item",
                    "placeholder": custom_placeholders.get(name),
                    "required": True,
                }
            )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "username",
            "batch",
            "department",
            "location",
            "role",
            "email",
            "contact",
            "short_intro",
            "bio",
            "website",
            "github",
            "linkedin",
            "twitter",
            "profile_picture",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control item"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control item", "required": True})
