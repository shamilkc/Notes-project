from multiprocessing import context
import re
from django.shortcuts import render,redirect
from .models import DataN
from .forms import upForm
from django.contrib import messages


# Create your views here.

def home(request):
    noteData =DataN.objects.all().order_by('-updated')
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
        return redirect('home')

    return render(request,'addnotes.html')


def deleteNote(request,pk):
    
    item =DataN.objects.get(id=pk)
    if request.method =="POST":
        item.delete()
        return redirect('home') 

    context ={'item':item}
    return render(request,'deleteN.html',context)


def updateMessege(request,pk):
    upmessege = DataN.objects.get(id=pk)
    form = upForm(instance=upmessege)
    if request.method =="POST":
        form = upForm(request.POST,instance=upmessege)
        if form.is_valid():
            
            form.save()
            return redirect('home')
        
            

    context = {
        'form':form
    }
    return render(request,'update.html',context)

