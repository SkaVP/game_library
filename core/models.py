from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
