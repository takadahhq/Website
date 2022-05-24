from dataclasses import fields
from platform import release
from django import forms
from stories.models import Chapters, Stories, Tag, Characters
from django.forms.widgets import NumberInput


# class Inline(InlineFormSetFactory):
#     model = Contact
#    fields = ['name', 'email']


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
     
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M", attrs={'class': 'textinput bg-white px-4 rounded-lg py-2 block border w-full text-gray-700 leading-normal focus:outline-none appearance-none border-gray-300'})

class StoryForm(forms.ModelForm):
    released_at = DateTimeLocalField()

    class Meta:
        model = Stories
        fields = ('title','abbreviation', 'summary', 'cover', 'story_type', 'tags', 'language','genre','rating', 'released_at','status',)



class ChapterForm(forms.ModelForm):
    #released_at = forms.DateTimeField(widget=NumberInput(attrs={'type': 'datetime-local'}), input_formats=['%d/%m/%Y %H:%M'])
    released_at = DateTimeLocalField()

    class Meta:
        model = Chapters
        fields = ('title','position', 'text', 'authors_note', 'status', 'released_at', )