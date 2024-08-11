# films/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_films, name='home'),  # Перенаправление на страницу просмотра фильмов при заходе на главную страницу
    path('add/', views.add_film, name='add_film'),  # Страница для добавления фильма
    path('view/', views.view_films, name='view_films'),  # Страница для просмотра списка фильмов
]
