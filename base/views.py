from django.shortcuts import render
from .models import Note, NoteType
# from django.http import HttpResponse

# Create your views here.
def home(request):
    note_objs = Note.objects.all()
    return render(request,'index.html',context={'notes':note_objs})

def create_note(request):
    note_type_objs = NoteType.objects.all()
    return render(request,'create_note.html',context={'note_types':note_type_objs})
