from django.contrib import admin
from .models import Album, Publisher

admin.site.register(Album)
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Listener)
admin.site.register(Favorite)