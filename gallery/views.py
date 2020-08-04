from django.shortcuts import render,redirect
import datetime as dt

# from django.http import HttpResponse, Http404
# import datetime as dt
from .models import Image, Category, Location

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'gallery.html', locals())

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def filter_by_location(request,image_location_id):
    images = Image.objects.filter(id=image_location_id)

    return render(request, 'location.html', {"images": images})
    