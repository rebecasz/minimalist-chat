from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from .models import  Room,Message,User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib import messages
@login_required(login_url='/accounts/login/')
def home(request):
    return  render(request,'home.html')

@login_required(login_url='/accounts/login/')
def room(request, room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    return  render(request,'room.html',{
        'username':username,
        'room':room,
        'room_details':room_details,
    })

def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']

    #verific daca camera exista
    if Room.objects.filter(name=room).exists():
        #daca camera exista
        #atunci redirectionam la acea camera
        return redirect('/'+room+'/?username='+username)
    else:
     new_room=Room.objects.create(name=room)
     new_room.save()
     return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()


def getMesseges(request, room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

@login_required(login_url='login/')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def logout_view(request):
	logout(request)
	return redirect('login')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('http://localhost:8000')
    context['form']=form
    return render(request, 'registration/sign_up.html', context)

