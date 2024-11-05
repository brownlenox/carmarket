from django.shortcuts import render
from  . models import Cars
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    return render(request, 'index.html')

def cars(request):
    cars_list = Cars.objects.all().order_by('-created_at')
    
    # Set up pagination for 8 cars per page
    paginator = Paginator(cars_list, 8)  # Adjust number for items per page
    page = request.GET.get('page')

    try:
        cars = paginator.get_page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    return render(request, 'cars.html', {'cars': cars})

# Search cars view with pagination
def search_cars(request):
    query = request.GET.get('search_query', '')
    if query:
        cars_list = Cars.objects.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(car_type__icontains=query) |
            Q(about__icontains=query)
        ).order_by('-created_at')
    else:
        cars_list = Cars.objects.all().order_by('-created_at')

    # Pagination setup for search results
    paginator = Paginator(cars_list, 8)  # Adjust for desired items per page
    page = request.GET.get('page')

    try:
        cars = paginator.get_page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    return render(request, 'cars.html', {
        'cars': cars,
        'search_query': query,
    })