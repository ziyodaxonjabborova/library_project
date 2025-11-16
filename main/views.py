from django.shortcuts import render
from .models import Todo

def home(request):
    data={
        'todos':Todo.objects.all()
    }
    return render(request,'todo.html',context=data)

def single_todo_view(request,id):
    todo=Todo.objects.get(id=id)
    return render(request,"single_todo.html",context={"todo":todo})
