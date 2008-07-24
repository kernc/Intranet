from django import forms

from intranet.org.models import TipSodelovanja, Person, Event, Sodelovanje
from intranet.org.models import Bug



class EventForm(forms.ModelForm):
    author1 = forms.CharField()
    tip1 = forms.ModelChoiceField(TipSodelovanja.objects.all())
    
    class Meta:
        model = Event

class FilterBug(forms.ModelForm):
    class Meta:
        model = Bug
    

class CommentBug(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class SodelovanjeFilter(forms.ModelForm):
    ##override the person in 'Sodelovanje', as there is required
    person = forms.ModelChoiceField(Person.objects.all(), required=False)
    c = [('', '---------'), ('txt', 'txt'), ('pdf', 'pdf')]
    export = forms.ChoiceField(choices=c, required=False)

    class Meta:
        model = Sodelovanje
