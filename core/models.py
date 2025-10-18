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

    def __str__(self):
        return self.title
