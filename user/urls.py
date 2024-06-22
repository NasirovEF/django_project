from django.urls import path
from user.apps import UserConfig
from user.views import (
    UserLoginView,
    UserRegistrationView,
    account_activate,
    UserDetailView,
    UserUpdateView,
    UserPasswordResetView,
    UserPasswordResetConfirmView,
)
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
)

app_name = UserConfig.name

urlpatterns = [
    path(
        "login/", UserLoginView.as_view(template_name="user/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("account-activate/<str:token>", account_activate, name="account-activate"),
    path("account-detail/<int:pk>", UserDetailView.as_view(), name="account-detail"),
    path("account-update/<int:pk>", UserUpdateView.as_view(), name="account-update"),
    path(
        "reset-password/",
        UserPasswordResetView.as_view(
            template_name="user/reset_pass.html",
            email_template_name="user/password_reset_email.html",
        ),
        name="reset-password",
    ),
    path(
        "reset-dan",
        PasswordResetDoneView.as_view(template_name="user/reset_done.html"),
        name="reset_done",
    ),
    path(
        "reset-confirm/<str:uidb64>,<str:token>",
        UserPasswordResetConfirmView.as_view(template_name="user/pass_set.html"),
        name="reset-confirm",
    ),
    path(
        "reset-completed/",
        PasswordResetCompleteView.as_view(template_name="user/reset_complete.html"),
        name="reset-completed",
    ),
]
