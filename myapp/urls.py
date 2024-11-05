from django.urls import path
from myapp import views
from django.conf.urls.static import static
from car_market import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('cars/', views.cars, name="cars"),
    path('search/', views.search_cars, name='search_cars'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)