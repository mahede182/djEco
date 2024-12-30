from django.contrib import admin
from django.urls import path, include
from accounts.views import Home, Signin, Signup, Logout, CustomPasswordChangeView

urlpatterns = [
    path("signin/", Signin.as_view(), name="signin"),
    path("signup/", Signup.as_view(), name="signup"),
    path("logout/", Logout.as_view(), name="logout"),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
]
