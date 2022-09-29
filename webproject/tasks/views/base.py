from django.shortcuts import render
from tasks.models import Task

def index_view(request):
    tasks = Task.objects.all().order_by('id').reverse
    choices = Task.CHOICES
    context = {
        'tasks': tasks,
        'choices': choices
    }
    return render(request, 'index.html', context)