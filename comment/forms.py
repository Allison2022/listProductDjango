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
    name = forms.CharField(initial='Erik')