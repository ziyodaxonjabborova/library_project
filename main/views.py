from django.shortcuts import render,redirect
from .models import Todo

#home page
def home(request):
    
    if request.method=="POST":
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        status=request.POST.get("status")
        
        Todo.objects.create(
            title=title,
            desc=desc,
            status=status
            
        )
    
    data={
        'todos':Todo.objects.all()
    }
    return render(request,'todo.html',context=data)

#batafsil page
def single_todo_view(request,id):
    todo=Todo.objects.get(id=id)
    return render(request,"single_todo.html",context={"todo":todo})

#delete page
def delete_todo(request,id):
    try:
        todo=Todo.objects.get(id=id)
    except:
        return render(request,"delete.html",context={"message":"Bunday topshiriq topilmadi!"})
    
    if request.method=="POST":
        todo.delete()
        return redirect("/")
    
    return render(request,"delete.html",context={'todo':todo})

#update page

def edit_todo(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        status = request.POST.get("status")

        todo.title = title
        todo.desc = desc
        todo.status = status
        todo.save()

        return redirect("/")

    return render(request, "edit.html", context={"todo": todo})

        

    

