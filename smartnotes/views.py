from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Note

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('smartnotes:index')
        else:
            # keep messages for framework compatibility but also return as context
            error_message = "Invalid credentials"
            messages.error(request, error_message)
    return render(request, 'smartnotes/login.html', {'error_message': error_message})


def register(request):
    """Simple registration view using Django's built-in UserCreationForm.

    After a successful POST the new user is automatically authenticated and
    logged in, then redirected to the index page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the new user in immediately
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            return redirect('smartnotes:index')
    else:
        form = UserCreationForm()
    return render(request, 'smartnotes/register.html', {'form': form})


@login_required
def index(request):
    notes = Note.objects.order_by('-created')[:20]
    context = {
        'notes': notes,
    }
    return render(request, 'smartnotes/index.html', context)


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'smartnotes/detail.html', {'note': note})


def results(request, note_id):
    return HttpResponse("Results placeholder for note %s." % note_id)


def vote(request, note_id):
    return HttpResponse("Vote placeholder for note %s." % note_id)
