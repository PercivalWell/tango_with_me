from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name="index"),
    path('base/', views.base, name="base"),
    path('categories/', views.categories, name="categories"),
    path('profile/', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('add-category', views.addCategory, name="addCategory"),
]