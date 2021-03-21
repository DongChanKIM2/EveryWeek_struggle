from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movies = form.save()
            return redirect('movies:detail', movies.pk)
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/form.html', context)

@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

@require_GET
def detail(request, movies_pk):
    movie = get_object_or_404(Movie, pk = movies_pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)

@require_http_methods(['POST', 'GET'])
def update(request, movies_pk):
    movie = get_object_or_404(Movie, pk = movies_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form':form}
    return render(request, 'movies/form.html', context)
    

@require_POST
def delete(request, movies_pk):
    # movie = get_object_or_404(Movie, pk = movies.pk)
    movie = Movie.objects.get(pk = movies_pk)
    movie.delete()
    return redirect('movies:index')