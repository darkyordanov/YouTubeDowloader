from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class AccountUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
