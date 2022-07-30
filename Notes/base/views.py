from multiprocessing import context
from django.shortcuts import render
from .models import DataN

# Create your views here.

def home(request):
    noteData =DataN.objects.all().order_by('-created')
    context ={
        'noteData':noteData
    }
    return render(request,'main.html',context)


def addNotes(request):
    if request.method =="POST":
        name =request.POST['name']
        dataNote = request.POST['data']

        n = DataN(note_name=name,note_data=dataNote)
        n.save()

    return render(request,'addnotes.html')


def deleteNote(request):
    item =DataN.objects.get(note_n)
    if request.method =="POST":
        item.delete()

    return render(request,'deleteN.html')