from django import forms
from .models import Language, EventSubscription

class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(queryset=Language.objects.all())

class EventSubscriptionForm(forms.ModelForm):
    class Meta:
        model = EventSubscription
        fields = ['name', 'email', 'comment']