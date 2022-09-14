from . import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('index/', views.index, name="index_view"),
    path('index1/', views.index_1, name="index1_view"),
    path('form/', views.form_view, name="form_view"),
    path('user/', views.user_view, name="user_view"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
]
