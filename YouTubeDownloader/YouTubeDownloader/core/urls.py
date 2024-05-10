from django.urls import path
from YouTubeDownloader.core.views import DownloadVideoView, DownloadSuccessView, youtube

urlpatterns = [    
    # path('', home, name='home'),
    
    
    path('', youtube, name='youtube'),
    path('download/success/', DownloadSuccessView.as_view(), name='download_success'),
]

