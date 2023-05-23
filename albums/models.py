from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    song_list = models.TextField()
    published_date = models.CharField(max_length=200)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.album_title