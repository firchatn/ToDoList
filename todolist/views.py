from django.shortcuts import render, redirect
from .forms import taskForm
from .models import task
# Create your views here.
def index(request):
	if request.method == "POST":
			form = taskForm(request.POST)
			Task = task()
			if form.is_valid():
				Task.myTask = form.cleaned_data['myTask']
				Task.save()
				return redirect('todolist:index')
	else:
		form = taskForm()
	tasks = task.objects.all()
	tasks = tasks.reverse()
	nb = task.objects.count()
	return render(request,'todolist/index.html', {'form' : form, 'tasks' : tasks, 'nb' : nb })
