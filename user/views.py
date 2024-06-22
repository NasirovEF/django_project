from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy, reverse

from config.settings import EMAIL_HOST_USER
from user.forms import (
    UserLoginViewForm,
    UserRegisterForm,
    UserUpdateForm,
    UserPasswordResetForm,
    UserSetPasswordForm,
)
from user.models import User
from django.views.generic import CreateView, DetailView, UpdateView
import secrets


class UserLoginView(LoginView):
    model = User
    form_class = UserLoginViewForm


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(15)
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        url = f"https//{host}/user/account-activate/{token}"
        send_mail(
            subject="Подтверждение аккаунта",
            message=f"Для подтверждения аккаунта перейдите по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def account_activate(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return render(
        request,
        "user/login.html",
    )


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse("user:account-detail", args=[self.object.pk])


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    success_url = reverse_lazy("user:reset_done")


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    success_url = reverse_lazy("user:reset-completed")
