from django.shortcuts import get_object_or_404, render
from django.shortcuts import render

from django.http import HttpResponse

from .models import Note

def login_view(request):
    return render(request, 'smartnotes/login.html')

    
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
