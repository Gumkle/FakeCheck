from django.shortcuts import render, redirect

from .security import IsRedactorMixin
from django.views import generic, View
from . import models
from . import forms


class ExpertListView(generic.ListView):
    model = models.Expert
    form_class = forms.ExpertForm


class ExpertCreateView(generic.CreateView):
    model = models.Expert
    form_class = forms.ExpertForm


class ExpertDetailView(generic.DetailView):
    model = models.Expert
    form_class = forms.ExpertForm


class ExpertUpdateView(generic.UpdateView):
    model = models.Expert
    form_class = forms.ExpertForm
    pk_url_kwarg = "pk"


class RedactorListView(generic.ListView):
    model = models.Redactor
    form_class = forms.RedactorForm


class RedactorCreateView(generic.CreateView):
    model = models.Redactor
    form_class = forms.RedactorForm


class RedactorDetailView(generic.DetailView):
    model = models.Redactor
    form_class = forms.RedactorForm


class RedactorUpdateView(generic.UpdateView):
    model = models.Redactor
    form_class = forms.RedactorForm
    pk_url_kwarg = "pk"


class QuestionCollectionListView(generic.ListView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fake-checker/question_collection_list.html'


class QuestionCollectionCreateView(generic.CreateView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fake-checker/question_collection_form.html'


class QuestionCollectionDetailView(generic.DetailView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fake-checker/question_collection_detail.html'


class QuestionCollectionUpdateView(generic.UpdateView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fake-checker/question_collection_form.html'
    pk_url_kwarg = "pk"


class ReviewListView(generic.ListView):
    model = models.Review
    form_class = forms.ReviewForm


class ReviewCreateView(generic.CreateView):
    model = models.Review
    form_class = forms.ReviewForm


class ReviewDetailView(generic.DetailView):
    model = models.Review
    form_class = forms.ReviewForm


class ReviewUpdateView(generic.UpdateView):
    model = models.Review
    form_class = forms.ReviewForm
    pk_url_kwarg = "pk"


class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    pk_url_kwarg = "pk"


class QuestionListView(generic.ListView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionCreateView(generic.CreateView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionDetailView(generic.DetailView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionUpdateView(generic.UpdateView):
    model = models.Question
    form_class = forms.QuestionForm
    pk_url_kwarg = "pk"


class QuestionFromUserListView(generic.ListView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fake-checker/question_from_user_list.html'


class QuestionFromUserCreateView(generic.CreateView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fake-checker/question_from_user_form.html'


class QuestionFromUserDetailView(generic.DetailView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fake-checker/question_from_user_detail.html'


class QuestionFromUserUpdateView(generic.UpdateView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fake-checker/question_from_user_form.html'
    pk_url_kwarg = "pk"


class QuestionForExpertListView(generic.ListView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm
    template_name = 'fake-checker/question_for_expert_list.html'


class QuestionForExpertCreateView(IsRedactorMixin, View):

    def get(self, request):
        return render(request, 'fake-checker/question_for_expert_form.html', {
            'question_form': forms.QuestionForm,
            'question_for_expert_form': forms.QuestionForExpertForm,
        })

    def post(self, request):
        expert_question = models.QuestionForExpert(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            sources=request.POST.get('sources'),
            redactor=request.user.redactor
        )
        expert_question.save()
        return redirect("fake-checker_QuestionForExpert_list")


class QuestionForExpertDetailView(generic.DetailView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm
    template_name = 'fake-checker/question_for_expert_detail.html'


class QuestionForExpertUpdateView(IsRedactorMixin,
                                  IsRedactorQuestionsAuthorMixin,
                                  IsNumberOfReviewsExceededMixin,
                                  View):

    def get(self, request):
        return render(request, 'fake-checker/question_for_expert_form.html', {
            'question_form': forms.QuestionForm,
            'question_for_expert_form': forms.QuestionForExpertForm,
        })

    def post(self, request):
        pass

    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm
    pk_url_kwarg = "pk"
    template_name =
