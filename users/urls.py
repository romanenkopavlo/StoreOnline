from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, UserLoginView, UserProfileView,
                         UserRegistrationView)

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="log_in"),
    path("logout/", LogoutView.as_view(), name="log_out"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("verify/<str:email>/<uuid:code>/", EmailVerificationView.as_view(), name="email_verification"),
]
