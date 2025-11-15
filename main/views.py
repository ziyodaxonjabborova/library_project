from django.shortcuts import render
from .models import Todo

def home(request):
    data={
        'todos':Todo.objects.all()
    }
    return render(request,'todo.html',context=data)
