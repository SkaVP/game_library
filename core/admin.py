from django.contrib import admin
from .models import Game

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'owner')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'release_date')