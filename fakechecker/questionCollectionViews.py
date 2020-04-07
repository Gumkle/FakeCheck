from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import generic, View
from . import forms
from . import models
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from .security import IsRedactorMixin, IsRedactorQuestionsAuthorMixin, IsNumberOfReviewsExceededMixin, \
    HasExpertAddedReviewMixin, IsExpertMixin, IsRedactorQuestionCollectionAuthorJSON
from django.forms.models import model_to_dict


class QuestionCollectionListView(LoginRequiredMixin,
                                IsRedactorMixin,
                                generic.ListView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_list.html'

    def get_queryset(self):
        return models.QuestionCollection.objects.filter(redactor=self.request.user.redactor)


class QuestionCollectionCreateView(LoginRequiredMixin,
                                   IsRedactorMixin,
                                   View):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            question_collection = form.save(commit=False)
            question_collection.redactor = request.user.redactor
            question_collection.save()
            return JsonResponse({'message': 'success', 'collection_id':question_collection.pk})
        else:
            return JsonResponse({'error':'please provide valid qyestion collection name'},status=500)



class QuestionCollectionDetailView(LoginRequiredMixin,
                                   IsRedactorMixin,
                                   generic.DetailView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_detail.html'

class QuestionCollectionViewQuestion(IsRedactorMixin,
                                     IsRedactorQuestionCollectionAuthorJSON,
                                     View):

    def get_data_from_url(self,request,collection_id,question_id):
        self.question_collection = get_object_or_404(models.QuestionCollection,id=collection_id)
        self.question = get_object_or_404(models.QuestionFromUser,id=question_id)

    def post(self, request, *args, **kwargs):
        self.get_data_from_url(request,kwargs['pk'],kwargs['question_id'])
        self.question_collection.questions_from_user.add(self.question)
        return JsonResponse({'message' : 'success'})

    def delete(self, request, *args, **kwargs):
        self.get_data_from_url(request, kwargs['pk'], kwargs['question_id'])
        self.question_collection.questions_from_user.remove(self.question)
        return JsonResponse({'message' : 'success'})
