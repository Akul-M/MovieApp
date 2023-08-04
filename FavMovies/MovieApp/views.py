from django.shortcuts import render, redirect
from .models import Movies
from .forms import updateForm

def home(request):
    data = Movies.objects.all()
    context = {"movieList": data}
    return render(request, "Home.html", context)

def details(request, movieId):
    movieObj = Movies.objects.get(id=movieId)
    return render(request, "details.html", {'movie': movieObj})

def addMovie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movies(MovieName=name, MovieDescription=desc, MovieYear=year, MovieImg=img)
        movie.save()
    return render(request, "add.html")

def updateData(request, movieId):
    movieObj = Movies.objects.get(id=movieId)
    form = updateForm(request.POST or None, request.FILES, instance=movieObj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movieObj})

def deleteData(request, movieId):
    if request.method == 'POST':
        movieObj = Movies.objects.get(id=movieId)
        movieObj.delete()
        return redirect('/')
    return render(request, 'delete.html')

