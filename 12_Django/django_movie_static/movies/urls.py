from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # C
    path('create/', views.create, name='create'),

    # R
    path('', views.index, name='index'),
    path('<int:movies_pk>/', views.detail, name='detail'),

    # U
    path('<int:movies_pk>/update/', views.update, name='update'),

    # D
    path('<int:movies_pk>/delete/', views.delete, name='delete'),
]
