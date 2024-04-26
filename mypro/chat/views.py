from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

# md5 encode
import hashlib

#
# class RoomRegister(View):
#     def post(self):


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    # room_name = hashlib.md5(room_name.encode()).hexdigest()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })
