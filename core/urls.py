from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add/', views.add_game_view, name='add_game'),
    path('edit/<int:game_id>/', views.edit_game_view, name='edit_game'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('game/<int:game_id>/', views.game_detail_view, name='game_detail'),
    path('games/', views.game_list_view, name='game_list'),
    path('my-games/', views.my_games_view, name='my_games'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
