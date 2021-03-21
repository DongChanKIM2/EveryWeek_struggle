from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        movie = Movie()
        movie.title = request.POST.get('title')
        movie.overview = request.POST.get('overview')
        movie.poster_path = request.POST.get('poster_path')
        movie.save()
        return redirect('detail', pk=movie.pk)
    return redirect('new')

