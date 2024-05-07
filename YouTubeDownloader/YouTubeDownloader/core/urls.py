from django.urls import path
from YouTubeDownloader.core.views import DownloadVideoView, DownloadSuccessView

urlpatterns = [    
    # path('', home, name='home'),
    
    path('', DownloadVideoView.as_view(), name='download'),
    path('download/success/', DownloadSuccessView.as_view(), name='download_success'),
]

