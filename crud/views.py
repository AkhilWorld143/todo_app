from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def add(request):
	tasks = Task.objects.all()
	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request, 'crud/add.html', context)


def update(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'crud/update.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/')

    # if request.method == 'POST':
    #     item.delete()
    #     return redirect('/')
    #
    # context = {'item':item}
    # return render(request, 'tasks/delete.html', context)
