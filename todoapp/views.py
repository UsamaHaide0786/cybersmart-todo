from django.shortcuts import render, redirect

# Create your views here.
from .models import Todo
import geocoder
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    current_location = geocoder.ip('me')
    data = Todo.objects.all()
    context = {"data": data, "current_location": current_location}
    return render(request, 'todoapp/index.html', context)


@require_http_methods(["POST"])
def add(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    Todo.objects.create(title=title, description=description, location=location)
    print(request.POST.get('location'))
    return redirect('/')


@require_http_methods(["GET"])
def show(request, id):
    obj = Todo.objects.get(id=id)
    return render(request, 'todoapp/edit.html', context={"obj": obj})


@require_http_methods(["GET"])
def update(request):
    id = request.GET.get('id')
    title = request.GET.get('title')
    description = request.GET.get('description')
    location = request.GET.get('location')
    is_completed = request.GET.get('iscompleted')
    print(is_completed)
    obj = Todo.objects.get(id=id)
    obj.title = title
    obj.description = description
    obj.location = location
    if is_completed == "on":
        obj.is_completed = True
    else:
        obj.is_completed = False

    obj.save()
    return redirect('/')


@require_http_methods(["GET"])
def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')
