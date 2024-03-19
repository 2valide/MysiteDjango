from django.shortcuts import render

# Create your views here.
def show(request, titre_film):
    release = 2000 + 3
    
    return render(request, "movies/show.html", {
        "titre": titre_film,
        "release": release,
        "autor": "Auteur",
        "user" : {
            "username": "username",
            "email": "email",
        },
    })

def index(request , titre_film) :
    release = 2000 + 3

    return render(request, "movies/index.html", {
        "titre" : titre_film,
        "description" : "description_film",
        "autor" : "auteur",
        "release" : "release",
    })

def login(request) :
    return render(request, "movies/login.html", {})

def create(request) :
    return render(request, "movies/create.html", {})

def random(request) :
    return render(request, "movies/random.html", {})