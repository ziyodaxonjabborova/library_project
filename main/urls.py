from django.urls import path
from .views import home,single_todo_view,delete_todo,edit_todo

urlpatterns=[
    path("",home),
    path("batafsil/<int:id>/",single_todo_view),
    path("delete/<int:id>/",delete_todo),
    path("edit/<int:id>/",edit_todo)
   
    
]