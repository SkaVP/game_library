from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    games = Game.objects.all().order_by('-release_date')
    return render(request, 'core/home.html', {'games': games})

# добавление игры


@login_required
def add_game_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.owner = request.user  # если есть поле owner
            game.save()
            messages.success(request, "✅ Игра успешно добавлена.")
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'core/add_game.html', {'form': form})

# редактирование игры

def edit_game_view(request, game_id):
    game = get_object_or_404(Game, id=game_id, owner=request.user)

    if request.method == 'POST':
        if 'delete_cover' in request.POST:
            game.cover.delete(save=False)
            game.cover = None
            game.save()
            messages.success(request, "🗑️ Обложка удалена.")
            return redirect('edit_game', game_id=game.id)

        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Игра успешно обновлена.")
            return redirect('home')
    else:
        form = GameForm(instance=game)

    return render(request, 'core/edit_game.html', {'form': form, 'game': game})

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