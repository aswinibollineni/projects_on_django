from django.urls import path
from .views import home, add_question, login_page, logout_page, register_page

urlpatterns = [
    path('', home, name='home'),
    path('add_question/', add_question, name='add_question'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]
