from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    song_list = models.TextField()
    published_date = models.CharField(max_length=200)
    label = models.ForeignKey(to='Label', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media/images/')

    def publish(self):
        self.save()

    def __str__(self):
        return self.album_title
    
class Artist(models.Model):
    artist = models.CharField(max_length=200)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.artist
    
class Label(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'labels'

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

class Cover(models.Model):
    # title = models.CharField(max_length=200)
    # description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title