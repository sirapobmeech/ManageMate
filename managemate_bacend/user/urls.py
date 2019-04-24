from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginAuthtoken.as_view()),
    path('logout/', Logout.as_view()),
    path('register/', User_register.as_view())
]