from django.http import HttpResponse
from django.shortcuts import redirect, render

from todoapp.forms import TodoForm
from todoapp.models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    try:
        todos = Todo.objects.filter(user = request.user)
    except:
        todos = []
    context = {
        'todos' : todos
    }
    return render(request, 'todoapp/index.html', context)

@login_required(login_url='login')
def create(request):
    form = TodoForm()
    if request.method == 'POST':
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            if request.user.is_authenticated:
                todo.user = request.user
                form.save()
                return redirect('home')
            else:
                return HttpResponse('You must be logged in to create your Todo')
    return render(request,'todoapp/create.html',{'form':form})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username,
                                 password=password,
                                 email=email)
        return redirect('home')
    return render(request,'todoapp/register.html',{})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,
                            password=password)
        print("User:", user)
        if user is not None:
            login(request,user)
            return redirect ('home')
    return render(request,'todoapp/login.html',{})

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def update(request,id):
    todo = Todo.objects.get(id=id)
    if todo.user != request.user:
        return redirect('home')
    form = TodoForm(instance = todo)
    if request.method == 'POST':
        print(request.POST)
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form':form
    }
    return render(request,'todoapp/update.html',context)

def delete(request,id):

    return render(request,'todoapp/delete.html',{})

def details(request,id):

    return render(request,'todoapp/details.html',{})

# def search(request):
#     search_query = request.GET.get('search_query')
#     if search_query:
#         todo = Todo.objects.filter(title__icontains=search_query)
#     else:
#         todo = None
#     return render(request,'index.html',{'todo':todo})


