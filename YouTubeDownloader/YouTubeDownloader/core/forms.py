from django import forms

class VideoDownloadForm(forms.Form):
    video_url = forms.URLField(label='Enter YouTube Video URL:')
    save_location = forms.FileField(label='Select Save Location:', widget=forms.ClearableFileInput(
        attrs={
            'webkitdirectory': True,
            'directory': True}
        ))