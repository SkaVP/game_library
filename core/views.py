from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Game
from .forms import RegisterForm, GameForm, ProfileForm
# регистрация

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

# Главная

def home_view(request):
    games = Game.objects.all()
    return render(request, 'core/home.html', {'games': games})

# добавление игры

@login_required
def add_game_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.owner = request.user
            game.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'core/add_game.html', {'form': form})

# редактирование игры

@login_required
def edit_game_view(request, game_id):
    game = Game.objects.get(id=game_id, owner=request.user)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/edit_game.html', {'form': form})

# профиль

@login_required
def profile_view(request):
    user = request.user
    games = Game.objects.filter(owner=user)
    return render(request, 'core/profile.html', {'user': user, 'games': games})


# редактирование профиля

@login_required
def edit_profile_view(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/edit_profile.html', {'form': form})