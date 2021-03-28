from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # C
    path('create/', views.create_review, name="create_review"),
    # R
    path('', views.index, name="index"),
    path('detail/<int:detail_pk>', views.review_detail, name="review_detail"),

    path('detail/<int:detail_pk>/comment_create/', views.comment_create, name='comment_create'),
    
]
