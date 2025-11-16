from django.urls import path
from .views import home,single_todo_view

urlpatterns=[
    path("",home),
    path("batafsil/<int:id>/",single_todo_view)
    
]