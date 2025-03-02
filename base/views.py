from django.shortcuts import render
from .models import Note
# from django.http import HttpResponse

# Create your views here.
def home(request):
    note_objs = Note.objects.all()
    return render(request,'index.html',context={'notes':note_objs})
