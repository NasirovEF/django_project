from django import forms
from catalog.forms import StileFormMixin
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from user.models import User


class UserLoginViewForm(StileFormMixin, AuthenticationForm):
    model = User
    fields = ("email", "password")


class UserRegisterForm(StileFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserUpdateForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "avatar", "phone_number", "country")


class UserPasswordResetForm(StileFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)


class UserSetPasswordForm(StileFormMixin, SetPasswordForm):
    class Meta:
        model = User
        fields = (
            "new_password1",
            "new_password2",
        )
