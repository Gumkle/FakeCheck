from django import forms
from django.forms import CharField, TextInput, Textarea

from . import models


class ExpertForm(forms.ModelForm):
    class Meta:
        model = models.Expert
        fields = [
            "profile_pic",
            "about",
            "user",
            "categories",
        ]


class RedactorForm(forms.ModelForm):
    class Meta:
        model = models.Redactor
        fields = [
            "phone_number",
            "user",
        ]


class QuestionCollectionForm(forms.ModelForm):
    class Meta:
        model = models.QuestionCollection
        fields = [
            "name",
            "questions_from_user",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "justification",
            "is_info_fake",
            "sources",
            "question_for_expert",
            "expert",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question

        fields = [
            "title",
            "content",
            "sources",
            "categories",
        ]


class QuestionFromUserForm(forms.ModelForm):
    class Meta:
        model = models.QuestionFromUser
        fields = [
            "is_read",
        ]


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
            'sources': "Źródła",
            'categories': "Kategorie",
        }
        widgets = {
            'sources': Textarea(attrs={'rows': 4, 'style': 'resize:none;'})
        }
