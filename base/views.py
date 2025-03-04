from django.shortcuts import render
from .models import Note, NoteType
# from django.http import HttpResponse

# Create your views here.
def home(request):
    note_objs = Note.objects.all()
    return render(request,'index.html',context={'notes':note_objs})

def create_note(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        file = request.POST.get('file')
        type = request.POST.get('type')
        deadline_at = request.POST.get('deadline_at')
        note_type_obj = NoteType.objects.get(id=type)
        Note.objects.create(name=name,description=description,file=file,type=note_type_obj,deadline_at=deadline_at)
    note_type_objs = NoteType.objects.all()
    return render(request,'create_note.html',context={'note_types':note_type_objs})
