from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FriendForm

# Create your views here.
def index(request):
    friends = Friend.objects.all()
    print(friends)

    if request.method == "POST":
        try:
            friend = Friend(name=request.POST['fname'], major=request.POST['major'], year=request.POST['year'])
            friend.save()
        except:
            pass

    return render(request, 'index.html', {'friends': friends})

def edit(request, id):
    friend = Friend.objects.get(id=id)
    return render(request, 'edit.html', {'friend': friend, 'id': id})

def delete(request, id):
    friend = Friend.objects.get(id=id)
    friend.delete()
    return HttpResponseRedirect('/polls')

def save(request):
    friend = Friend.objects.get(id=int(request.POST['id']))
    friend.name = request.POST['fname']
    friend.major = request.POST['major']
    friend.year = request.POST['year']
    friend.save()
    return HttpResponseRedirect('/polls')
