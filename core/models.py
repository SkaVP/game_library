from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    GENRE_CHOICES = [
        ('RPG', 'RPG'),
        ('Shooter', 'Шутер'),
        ('Strategy', 'Стратегия'),
        ('Adventure', 'Приключения'),
        ('Puzzle', 'Головоломка'),
        ('Sports', 'Спорт'),
        ('Simulation', 'Симулятор'),
        ('Other', 'Другое'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    rating = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class GameRating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ('game', 'user')
