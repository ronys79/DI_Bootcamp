from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def add_film(request):
    if request.method == 'GET':
        form = AddFilmForm()
        return render(request, 'addpage.html', {'form': form})
    elif request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
        #     Film.objects.create(**form.cleaned_data)

        # elif request.method == "POST":
        #     form = AddFilmForm(request.POST)
        #     if form.is_valid():
        #         film = Film.objects.create(
        #             title=form.cleaned_data['title'], release_date=form.cleaned_data['release_date'], created_in_country=form.cleaned_data['created_in_country'])
        #         film.category.set(form.cleaned_data['category'])
        #         film.available_in_countries.set(
        #             form.cleaned_data['available_in_countries'])
        #         film.director.set(form.cleaned_data['director'])

        return redirect('homepage')


def add_director(request):
    if request.method == 'GET':
        form = AddDirector()
        return render(request, 'addpage.html', {'form': form})
    elif request.method == 'POST':
        form = AddDirector(request.POST)
        if form.is_valid():
            Director.objects.create(**form.cleaned_data)
        return redirect('homepage')
