"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from albums import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.album_list, name='home'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
    path('albums/new', views.create_album, name='new_album'),
    path('albums/<int:pk>/delete', views.delete_album, name='delete-album'),
    path('albums/<int:pk>/edit', views.edit_album, name='edit-album'),
    path('albums/<int:label_pk>/label', views.albums_by_label, name='album-label'),
    path('albums/<int:pk>/artists', views.artist_list, name='artist-list'),
    path('albums/newartist', views.create_artist, name='new-artist'),
    path('albums/<int:pk>/deets', views.artist_detail, name='deets'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)