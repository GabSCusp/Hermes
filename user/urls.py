from user.views import LoginPageView
from django.urls import path
urlpatterns = [path('', LoginPageView.as_view(), name = 'login'),]
