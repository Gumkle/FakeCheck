from django.contrib import admin
from django import forms

from . import models


class ExpertAdminForm(forms.ModelForm):

    class Meta:
        model = models.Expert
        fields = "__all__"


class ExpertAdmin(admin.ModelAdmin):
    form = ExpertAdminForm
    list_display = [
        "last_updated",
        "profile_pic",
        "about",
        "created",
    ]


class RedactorAdminForm(forms.ModelForm):

    class Meta:
        model = models.Redactor
        fields = "__all__"


class RedactorAdmin(admin.ModelAdmin):
    form = RedactorAdminForm
    list_display = [
        "phone_number",
        "created",
    ]


class QuestionCollectionAdminForm(forms.ModelForm):

    class Meta:
        model = models.QuestionCollection
        fields = "__all__"


class QuestionCollectionAdmin(admin.ModelAdmin):
    form = QuestionCollectionAdminForm
    list_display = [
        "name",
        "created",
    ]


class ReviewAdminForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = "__all__"


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = [
        "last_updated",
        "justification",
        "is_info_fake",
        "created",
        "sources",
    ]


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "name",
    ]


class QuestionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = [
        "content",
        "created",
        "sources",
    ]


class QuestionFromUserAdminForm(forms.ModelForm):

    class Meta:
        model = models.QuestionFromUser
        fields = "__all__"


class QuestionFromUserAdmin(admin.ModelAdmin):
    form = QuestionFromUserAdminForm
    list_display = [
        "is_read",
    ]


class QuestionForExpertAdminForm(forms.ModelForm):

    class Meta:
        model = models.QuestionForExpert
        fields = "__all__"


class QuestionForExpertAdmin(admin.ModelAdmin):
    form = QuestionForExpertAdminForm
    list_display = [
        'title'
    ]


admin.site.register(models.Expert, ExpertAdmin)
admin.site.register(models.Redactor, RedactorAdmin)
admin.site.register(models.QuestionCollection, QuestionCollectionAdmin)
admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.QuestionFromUser, QuestionFromUserAdmin)
admin.site.register(models.QuestionForExpert, QuestionForExpertAdmin)
