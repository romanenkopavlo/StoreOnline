from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("index")
    title = "Authorization"


class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:log_in")
    success_message = "You have successfully signed up"
    title = "Registration"


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = "users/profile.html"
    form_class = UserProfileForm
    title = "Profile"

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    title = "Confirmation of email"
    template_name = "users/email_verification.html"

    def get(self, request, *args, **kwargs):
        code = kwargs["code"]
        user = User.objects.get(email=kwargs["email"])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("index"))
