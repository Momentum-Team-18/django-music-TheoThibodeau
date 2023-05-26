from django.contrib import admin
from .models import Album, Label, Listener, Favorite, Team, Cover

admin.site.register(Album)
# Register your models here.
admin.site.register(Label)
admin.site.register(Listener)
admin.site.register(Favorite)
admin.site.register(Team)
admin.site.register(Cover)