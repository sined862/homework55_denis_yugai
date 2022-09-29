from django.urls import reverse
from django.shortcuts import render
from tasks.models import Task
from django.shortcuts import redirect , get_object_or_404


def add_view(request):
    if request.method == 'GET':
        choices = Task.CHOICES
        return render(request,'task_create.html',context={
            'choices': choices
        })
    task_data = {
        'description': request.POST.get('description'),
        'detail_description': request.POST.get('detail_description'),
        'status': request.POST.get('status'),
        'date_deadline': request.POST.get('date_deadline')
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def edit_view(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        choices = Task.CHOICES
        context = {
            "task": task,
            'choices': choices
        }
        return render(request, 'task_edit.html', context=context)
    task = Task.objects.get(pk=pk)
    task.description = request.POST.get('description')
    task.detail_description = request.POST.get('detail_description')
    task.status = request.POST.get('status')
    task.date_deadline = request.POST.get('date_deadline')
    task.save()
    return redirect('task_detail', pk=task.pk)

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    choices = Task.CHOICES
    return render(request, 'task.html', context={'task': task, 'choices': choices})

def del_view(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')



    
