from django import forms
from django.contrib.auth.forms import UsernameField, AuthenticationForm

from . import models


class QuestionCollectionForm(forms.ModelForm):
    class Meta:
        model = models.QuestionCollection
        fields = [
            "name"
        ]
        labels = {
            "name": 'Nazwa',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "is_info_fake",
            "justification",
            "sources",
        ]
        widgets = {
            'is_info_fake': forms.RadioSelect
        }
        exclude = ['created', 'last_updated']
        labels = {
            'justification': 'Argumentacja',
            'is_info_fake': 'Czy informacja jest fałszywa?',
            'sources': 'Źródła (linki w oddzielnych liniach)',
        }

    def clean_sources(self):
        sources = self.cleaned_data.get('sources')
        if (sources.count(' /') > 0 or sources.count('/ ') > 0 or sources.count('i ') > 0 or sources.count(
                ' i') > 0) or (
                len(sources) > 0 and (sources.count('.') == 0 or (sources.count(' ') > 0 and sources.count(',') == 0))):
            raise forms.ValidationError('Zła forma wysłania linków.')
        else:
            return sources


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
            "fa_icon_class"
        ]

        labels = {
            'name': 'Nazwa',
            'fa_icon_class': 'Klasa ikony FA'
        }


class QuestionFromUserForm(forms.ModelForm):
    class Meta:
        model = models.QuestionFromUser
        fields = [
            "title",
            "content",
            "categories",
            "sources",
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 8,
                'style': 'resize: none;',
            }),
            'sources': forms.Textarea(attrs={
                'rows': 3,
                'style': 'resize: none;'
            }),
        }
        labels = {
            'title': 'Pytanie jednym zdaniem',
            'content': 'Rozwinięcie pytania',
            'categories': 'Kategorie',
            'sources': 'Źródła (linki w oddzielnych liniach)',
        }

    def clean_sources(self):
        sources = self.cleaned_data.get('sources')
        return sources.replace(" ","")


class QuestionForExpertForm(forms.ModelForm):
    class Meta:
        model = models.QuestionForExpert
        fields = [
            "title",
            "content",
            "sources",
            "categories",
        ]
        labels = {
            'title': "Tytuł",
            'content': "Treść",
            'sources': "Źródła (linki w oddzielnych liniach)",
            'categories': "Kategorie",
        }
        widgets = {
            'sources': forms.Textarea(attrs={'rows': 4, 'style': 'resize:none;'})
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Login',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput
    )

    error_messages = {
        'invalid_login': "Nazwa użytkownika lub hasło są nieprawidłowe. Pamiętaj że wielkość liter ma znaczenie!",
        'inactive': "To konto jest nieaktywne",
    }
