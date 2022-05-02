from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
# from django.forms import modelform_factory

from meetings.models import Meeting, Room,Record
from .forms import MeetingForm
from django.contrib import messages

from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render


# get the detail meeting ids
def detail(request, id):
    '''
        this view is using for get the metting with particular id
    '''
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html',{'meeting':meeting})


# get the all room details
def rooms_list(request):
    '''
        this meeting rooms are get the room available data
        get all records from room data
    '''
    num_rooms = Room.objects.count()
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms_list.html', {'num_rooms':num_rooms,'rooms':rooms})



# Approach 2
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new_meeting.html", {"form": form})


# create room details for get the data create room name with particular number
def create_room(request):
    if request.method == "POST":
        roomname = request.POST.get('roomname')
        floor_number = request.POST.get('floor_number')
        room_number = request.POST.get('room_number')
        Room(name=roomname,floor_number=floor_number,room_number=room_number).save()
        return redirect('welcome')
    else:
        return render(request, "meetings/create_room.html")


# create video records and store into db
def record(request):
    if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        language = request.POST.get("language")
        record = Record.objects.create(language=language, voice_record=audio_file)
        record.save()
        messages.success(request, "Audio recording successfully added!")
        return JsonResponse(
            {
                "success": True,
            }
        )
    context = {"page_title": "Record audio"}
    return render(request, "meetings/record.html", context)


# get all record from video records table
def get_records(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "meetings/record_list.html", context)