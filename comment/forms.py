from django.forms import ModelForm, Textarea, TextInput
from django import forms
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        # overriding html class attributes
        widgets = {
            "text": TextInput(attrs = {"class": 'form-input'}),
        }
        # another way
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].widget.attrs.update({"class": 'form-input'})

    def save(self, commit=True, text=""):
        instance = super(CommentForm, self).save(commit=commit)
        if(text == ""):
            instance.text = text #"No podras modificarme"
        if(commit):
            instance.save()

# form not related to a model
class ContactForm(forms.Form):
    # name = forms.CharField(label='Name', initial='Erik', disabled=False, help_text='your name...', max_length=10, min_length=2)
    name = forms.CharField(label='Name', max_length=10, min_length=2)
    surname = forms.CharField(label='Surname', required=False, max_length=10, min_length=2)
    phone = forms.RegexField(label='phone', regex="^\d{3}-\d{3}-\d{4}$", max_length=12, min_length=10)
    birth_date = forms.DateField(label='birth date')