from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name = 'MovieApp'

urlpatterns = [

    path('', views.home, name='home'),
    path('movie/<int:movieId>/', views.details, name='details'),
    path('add/', views.addMovie, name='addMovie'),
    path('update/<int:movieId>/', views.updateData, name='update'),
    path('delete/<int:movieId>/', views.deleteData, name='delete')
]

