from django.shortcuts import render, redirect

# Create your views here.
from .commons import weather_color
from .models import Todo
import geocoder
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):

    """
        Will return the db objects after injecting weather and temperature values.
        Also get the user current location using geocoder.
    """

    current_location = geocoder.ip('me')
    query = Todo.objects.all()
    data = weather_color(query)
    context = {"data": data, "current_location": current_location}
    return render(request, 'todoapp/index.html', context)


@require_http_methods(["POST"])
def add(request):

    """
        Will create the Todo object.
    """

    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    Todo.objects.create(title=title, description=description, location=location)
    print(request.POST.get('location'))
    return redirect('/')


def show(request, id):

    """
        Will show the Todo object.
    """

    current_location = geocoder.ip('me')
    obj = Todo.objects.get(id=id)
    return render(request, 'todoapp/edit.html', context={"obj": obj, "current_location": current_location})


def update(request):

    """
        Will update the Todo object.
    """

    id = request.GET.get('id')
    title = request.GET.get('title')
    description = request.GET.get('description')
    location = request.GET.get('location')
    is_completed = request.GET.get('iscompleted')
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


def delete(request, id):

    """
        Will delete the Todo object.
    """

    Todo.objects.get(id=id).delete()
    return redirect('/')
