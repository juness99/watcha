from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm, MovieModelForm
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request,"movie/list.html",{"movies":movies})

def detail(request,id):
    movie = Movie.objects.get(id=id)
    return render(request,"movie/detail.html",{"movie":movie})

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        title_en = request.POST.get("title_en")
        audience = request.POST.get("audience")
        open_date = request.POST.get("open_date")
        genre = request.POST.get("genre")
        watch_grade = request.POST.get("watch_grade")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        
        Movie.objects.create(
            title=title,title_en=title_en,
            audience=audience,open_date=open_date,
            genre=genre,watch_grade=watch_grade,
            score=score,poster_url=poster_url,
            description=description)
        return redirect("movies:list")
    else:
        return render(request,"movie/create.html")
    
def form_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            title_en = form.cleaned_data.get("title_en")
            audience = form.cleaned_data.get("audience")
            open_date = form.cleaned_data.get("open_date")
            genre = form.cleaned_data.get("genre")
            watch_grade = form.cleaned_data.get("watch_grade")
            score = form.cleaned_data.get("score")
            poster_url = form.cleaned_data.get("poster_url")
            description = form.cleaned_data.get("description")
            
            Movie.objects.create(
                        title=title,title_en=title_en,
                        audience=audience,open_date=open_date,
                        genre=genre,watch_grade=watch_grade,
                        score=score,poster_url=poster_url,
                        description=description)
            
            return redirect("movies:list")
    else:
        form = MovieForm()
    return render(request,"movie/form_create.html",{"form":form})
    
def form_update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            title_en = form.cleaned_data.get("title_en")
            audience = form.cleaned_data.get("audience")
            open_date = form.cleaned_data.get("open_date")
            genre = form.cleaned_data.get("genre")
            watch_grade = form.cleaned_data.get("watch_grade")
            score = form.cleaned_data.get("score")
            poster_url = form.cleaned_data.get("poster_url")
            description = form.cleaned_data.get("description")
            
            movie.title = title
            movie.title_en = title_en
            movie.audience = audience
            movie.open_date = open_date
            movie.genre = genre
            movie.watch_grade = watch_grade
            movie.score = score
            movie.poster_url = poster_url
            movie.description = description
            movie.save()
            
            return redirect("movies:list")
    else:
        data = {
            "title":movie.title,
            "title_en":movie.title_en,
            "audience":movie.audience,
            "open_date":movie.open_date,
            "genre":movie.genre,
            "watch_grade":movie.watch_grade,
            "score":movie.score,
            "poster_url":movie.poster_url,
            "description":movie.description
        }
        form = MovieForm(data)
        return render(request,"movie/form_update.html",{"form":form})
        
def model_form_create(request):
    if request.method == "POST":
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    else:
        form = MovieModelForm()
        return render(request,"movie/model_form_create.html",{"form":form})
        

def model_form_update(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:detail", id)
        
    else:
        form = MovieModelForm(instance=movie)
    return render(request,"movie/model_form_update.html",{"form":form})