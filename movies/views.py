from django.shortcuts import render
from . import models

# Create your views here.
def show(request, fID):
    listMovies = models.Movies.objects.get(filmId=fID)
    premierFilm = listMovies

    return render(request, "movies/show.html", {
        "titre": premierFilm.titre,
        "description": premierFilm.description,
        "autor": premierFilm.autor,
        "release": premierFilm.release,
        "nextId": int(fID) + 1,
    })

    

def index(request) :
    listeTousFilms = models.Movies.objects.all()

    return render(request, "movies/index.html", {
        "premiersFilms": listeTousFilms,
    })

def login(request) :
    return render(request, "movies/login.html", {})

def create(request) :
    return render(request, "movies/create.html", {})

def random(request) :
    return render(request, "movies/random.html", {})