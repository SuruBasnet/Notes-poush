from django.shortcuts import render,redirect
from .models import Note, NoteType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password # function to encrypt normal password
from django.contrib.auth.decorators import login_required # decorator to check whether the requesting user is valid or not
# from django.http import HttpResponse

# Create your views here.
@login_required()
def home(request):
    note_objs = Note.objects.all()
    return render(request,'index.html',context={'notes':note_objs})
@login_required()
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
@login_required()
def edit_note(request,pk):
    note_objs = Note.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        file = request.POST.get('file')
        type = request.POST.get('type')
        deadline_at = request.POST.get('deadline_at')
        note_type_obj = NoteType.objects.get(id=type)
        note_objs.name = name
        note_objs.description  = description
        note_objs.file = file
        note_objs.type = note_type_obj
        note_objs.deadline_at = deadline_at
        note_objs.save()
    note_type_objs = NoteType.objects.all()
    return render(request,'edit_note.html',context={'note':note_objs,'note_types':note_type_objs})
@login_required()
def delete_note(request,pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        hash_password = make_password(password)
        User.objects.create(email=email,username=username,password=hash_password)
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user != None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')