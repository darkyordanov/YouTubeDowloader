from django.shortcuts import render
from django.views import generic as view
from django.urls import reverse_lazy

from pytube import YouTube
import os

from YouTubeDownloader.core.forms import VideoDownloadForm


# def home(request):
#     return render(request, 'core/home.html')


class DownloadVideoView(view.FormView):
    template_name = 'core/download.html'
    form_class = VideoDownloadForm
    success_url = reverse_lazy('download_success')

    def form_valid(self, form):
        video_url = form.cleaned_data['video_url']
        save_location = self.request.FILES['save_location']  # Access file data from request.FILES
        
        try:
            yt = YouTube(video_url)
            streams = yt.streams.filter(
                progressive=True,
                file_extension='mp4',
            )
            highest_res_stream = streams.get_highest_resolution()
            file_path = os.path.join(save_location, f"{yt.title}.mp4")
            highest_res_stream.download(output_path=save_location, filename=yt.title)
            self.request.session['message'] = f"Video '{yt.title}' downloaded successfully!"
        except Exception as e:
            self.request.session['error_message'] = f"Error: {str(e)}"

        return super().form_valid(form)

    

class DownloadSuccessView(view.TemplateView):
    template_name = 'core/download_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.request.session.pop('message', None)
        context['error_message'] = self.request.session.pop('error_message', None)
        return context
    