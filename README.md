# ToDo List
### Install Python
[Download python](https://www.python.org/downloads/)
and follow installing statements
### Install Django
pip install django
### Get Start with Django
1. django admin startproject todo
   1. (note) dont name your project todo
2. cd project folder
3. python manage.py startapp  todolist
4. cd todo
5. open setting.py
6. add todolist in INSTALLED_APPS
   1. dont messing , at the and of list
7. open urls.py
8. import include from django.conf.urls
9. add ligne in urlpatterns
   1. url(r'^', include('todolist.urls'),
10. cd ..
11. cd todolist
12. create new file name urls.py
13. add the following code to urls.py

```python
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        ]
```

14. save change
15. add template todo-template to todolist\templates\todolist
16. open views.py
17. add this function

```python
from django.shortcuts import render

def index(request):
	return render(request,'todolist/index.html')

```
18. cd ..
19. python manage.py runserver
20. open browser link 127.0.0.1:8000
### Result
![Alt text](/image/image1.png)

