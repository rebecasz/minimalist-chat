from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from .models import  Room,Message
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth import login, authenticate #add this

def home(request):
    return  render(request,'home.html')

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


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


