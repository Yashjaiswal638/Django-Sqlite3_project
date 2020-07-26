from django import forms

class VideoForm(forms.Form):
    videoname = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'id': 'inputname'
        }))
    videodesc = forms.CharField(max_length=30,
        widget=forms.Textarea({
        'class': 'form-control',
        'rows': '5',
        'id': 'comment',
        'placeholder': 'Name'
        }))