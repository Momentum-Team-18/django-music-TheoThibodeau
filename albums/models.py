from django.db import models

class Album(models.Model):
    artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE, blank=True, null=True)
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
    name = models.CharField(max_length=200)
    album_list = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images/')

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.name
    
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
    



# class User(AbstractUser):
#     TEACHER = 'TE'
#     STUDENT = 'ST'

#     USER_TYPE_CHOICES = [
#         (TEACHER, "Teacher"),
#         (STUDENT, "Student"),
#     ]
#     location = models.CharField(max_length=30, blank=True, null=True)
#     birth_date = models.DateField(null=True, blank=True)
#     type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default=STUDENT)

    # then you migrate
    # then you need to say form.models import user in the admin! and complete
    # other admin requirements

# class Course(models.Model):
#     MONDAY = 'M'
#     TUESDAY = 'T'
#     WEDNESDAY = 'W'
#     THURSDAY = 'TH'

#     DAY_CHOICES = [
#         (MONDAY, "Monday"),
#         (TUESDAY, "Tuesday"),
#         (WEDNESDAY, "Wednesday"),
#         (THURSDAY, "Thursday"),
#     ]
#     title = models.CharField(max_length=100)
#     day = models.CharField(max_length=50, choices=DAY_CHOICES)
#     start_time = models.TimeField()
#     length_in_hours = models.FloatField(default=1.00)
#     teacher = models.ForeignKey(to=User, on_delete=models.CASCADE)

#     # foriegn key added, now migrate
#     # non-nullable field: select an option: 1
#     # type exit prompt: 1 - is the users primary key


#     def __str__(self):
#         return self.title

#     # migrate and add to admin
