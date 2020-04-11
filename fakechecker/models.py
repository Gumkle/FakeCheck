from django.db import models
from django.urls import reverse
from django.db.models import F
from model_utils.managers import InheritanceManager


class Expert(models.Model):
    # Relationships
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    categories = models.ManyToManyField("fakechecker.Category")

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    profile_pic = models.URLField()
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("Expert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Expert_update", args=(self.pk,))


class Redactor(models.Model):
    # Relationships
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    # Fields
    phone_number = models.TextField(max_length=12)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("Redactor_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Redactor_update", args=(self.pk,))


class QuestionCollection(models.Model):
    # Relationships
    questions_from_user = models.ManyToManyField("fakechecker.QuestionFromUser", blank=True)
    redactor = models.ForeignKey("fakechecker.Redactor", on_delete=models.CASCADE)

    # Fields
    name = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def questions_from_user_list(self):
        return ", ".join([question.title for question in self.questions_from_user.all()])

    def get_absolute_url(self):
        return reverse("QuestionCollection_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("QuestionCollection_update", args=(self.pk,))


BOOL_CHOICES = ((True, 'Tak'), (False, 'Nie'))


class Review(models.Model):
    # Relationships
    question_for_expert = models.ForeignKey("fakechecker.QuestionForExpert", on_delete=models.CASCADE)
    expert = models.ForeignKey("fakechecker.Expert", related_name="reviews", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    justification = models.TextField()
    is_info_fake = models.BooleanField(choices=BOOL_CHOICES, default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sources = models.TextField()

    DELIMITER = "\n"

    class Meta:
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("QuestionForExpert_detail", args=(self.question_for_expert.id,))

    def get_update_url(self):
        return reverse("Review_update", args=(self.pk,))

    def list_of_sources(self):
        return self.sources.split(self.DELIMITER)


class Category(models.Model):
    # Fields
    name = models.TextField(max_length=100, primary_key=True)
    fa_icon_class = models.TextField(max_length=64, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Category_detail", args=(self.name,))

    def get_update_url(self):
        return reverse("Category_update", args=(self.name,))


class Question(models.Model):
    # Relationships
    categories = models.ManyToManyField("fakechecker.Category", related_name="questions", blank=False)
    objects = InheritanceManager()
    # Fields
    title = models.CharField(max_length=180)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sources = models.TextField(blank=True)

    # Constant
    DELIMITER = "\n"

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def categories_list(self):
        return ", ".join([category.name for category in self.categories.all()])

    def list_of_sources(self):
        return self.sources.split(self.DELIMITER)


class QuestionFromUser(Question):
    # Fields
    is_read = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("QuestionFromUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("QuestionFromUser_update", args=(self.pk,))

    def is_for_expert(self):
        return True


class QuestionForExpert(Question):
    # Fields
    views = models.BigIntegerField(default=0)

    # Relationships
    redactor = models.ForeignKey("fakechecker.Redactor", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("QuestionForExpert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("QuestionForExpert_update", args=(self.pk,))

    def get_fake_number(self):
        return self.review_set.filter(is_info_fake=True).count()

    def get_real_number(self):
        return self.review_set.filter(is_info_fake=False).count()

    def get_fake_percentage(self):
        if self.review_set.count() != 0:
            return round(self.get_fake_number() / self.review_set.count() * 100)
        return 0

    def get_real_percentage(self):
        return 100 - self.get_fake_percentage()

    def increment_view(self):
        QuestionForExpert.objects.filter(id=self.id).update(views=F('views') + 1)

    def is_for_expert(self):
        return True
