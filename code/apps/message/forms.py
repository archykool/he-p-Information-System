from django import forms
from .models import Msg


class MsgPostForm(forms.ModelForm):
    class Meta:
        model = Msg
        fields = ('title', 'content')