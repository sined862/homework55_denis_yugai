from django.shortcuts import render
from tasks.models import Task
from tasks.forms import TaskForm
from django.shortcuts import redirect , get_object_or_404


def add_view(request):
    form = TaskForm()
    if request.method == 'GET':
        choices = Task.CHOICES
        return render(request,'task_create.html',context={
            'choices': choices,
            'form': form
        })
    form = TaskForm(request.POST)
    if not form.is_valid():
        return render(request,'task_create.html',context={
            'form': form
        }) 
    task = Task.objects.create(**form.cleaned_data)
    return redirect('task_detail', pk=task.pk)


def edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'description': task.description,
            'detail_description': task.detail_description,
            'status': task.status,
            'date_deadline': task.date_deadline
        })
        return render(request, 'task_edit.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.detail_description = form.cleaned_data['detail_description']
            task.status = form.cleaned_data['status']
            task.date_deadline = form.cleaned_data['date_deadline']
            task.save()
            return redirect('task_detail', pk=task.pk)
        else:
            return render(request, 'task_edit.html', context={'form': form, 'task': task})
            

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    choices = Task.CHOICES
    return render(request, 'task.html', context={'task': task, 'choices': choices})

def del_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context = {'task': task})

def del_confirm_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')

def tasks_del_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'tasks_del.html', context={'tasks': tasks})
    print(f'Посты - {request.POST}')

def tasks_del_confirm_view(request):
    ids = request.POST
    return render(request, 'tasks_del_confirm.html', context={'ids': ids})


    
