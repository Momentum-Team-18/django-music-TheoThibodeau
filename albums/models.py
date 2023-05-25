from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    song_list = models.TextField()
    published_date = models.CharField(max_length=200)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.album_title
    
class Publisher(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'companies'

        def __str__(self):
            return self.name
        
class Listener(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(to='Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Favorite(models.Model):
    listener = models.ForeignKey(to='Listener', on_delete=models.CASCADE)
    album = models.ForeignKey(to='Album', on_delete=models.CASCADE)

class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name