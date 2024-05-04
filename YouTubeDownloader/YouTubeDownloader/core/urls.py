from django.urls import path
from YouTubeDownloader.core.views import core

urlpatterns = [    
    path('', core, name='core')
]
