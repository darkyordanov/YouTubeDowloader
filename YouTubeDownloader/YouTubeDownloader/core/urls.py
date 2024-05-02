from django.urls import path, include
from YouTubeDownloader.core.views import core

urlpatterns = [    
    path('', core, name='core')
]
