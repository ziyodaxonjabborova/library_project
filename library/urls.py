
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.author_list, name='author-list'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]
