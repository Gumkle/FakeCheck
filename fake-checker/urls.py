from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Expert", api.ExpertViewSet)
router.register("Redactor", api.RedactorViewSet)
router.register("QuestionCollection", api.QuestionCollectionViewSet)
router.register("Review", api.ReviewViewSet)
router.register("Category", api.CategoryViewSet)
router.register("Question", api.QuestionViewSet)
router.register("QuestionFromUser", api.QuestionFromUserViewSet)
router.register("QuestionForExpert", api.QuestionForExpertViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("fake-checker/Expert/", views.ExpertListView.as_view(), name="fake-checker_Expert_list"),
    path("fake-checker/Expert/create/", views.ExpertCreateView.as_view(), name="fake-checker_Expert_create"),
    path("fake-checker/Expert/detail/<int:pk>/", views.ExpertDetailView.as_view(), name="fake-checker_Expert_detail"),
    path("fake-checker/Expert/update/<int:pk>/", views.ExpertUpdateView.as_view(), name="fake-checker_Expert_update"),
    path("fake-checker/Redactor/", views.RedactorListView.as_view(), name="fake-checker_Redactor_list"),
    path("fake-checker/Redactor/create/", views.RedactorCreateView.as_view(), name="fake-checker_Redactor_create"),
    path("fake-checker/Redactor/detail/<int:pk>/", views.RedactorDetailView.as_view(), name="fake-checker_Redactor_detail"),
    path("fake-checker/Redactor/update/<int:pk>/", views.RedactorUpdateView.as_view(), name="fake-checker_Redactor_update"),
    path("fake-checker/QuestionCollection/", views.QuestionCollectionListView.as_view(), name="fake-checker_QuestionCollection_list"),
    path("fake-checker/QuestionCollection/create/", views.QuestionCollectionCreateView.as_view(), name="fake-checker_QuestionCollection_create"),
    path("fake-checker/QuestionCollection/detail/<int:pk>/", views.QuestionCollectionDetailView.as_view(), name="fake-checker_QuestionCollection_detail"),
    path("fake-checker/QuestionCollection/update/<int:pk>/", views.QuestionCollectionUpdateView.as_view(), name="fake-checker_QuestionCollection_update"),
    path("fake-checker/Review/", views.ReviewListView.as_view(), name="fake-checker_Review_list"),
    path("fake-checker/Review/create/", views.ReviewCreateView.as_view(), name="fake-checker_Review_create"),
    path("fake-checker/Review/detail/<int:pk>/", views.ReviewDetailView.as_view(), name="fake-checker_Review_detail"),
    path("fake-checker/Review/update/<int:pk>/", views.ReviewUpdateView.as_view(), name="fake-checker_Review_update"),
    path("fake-checker/Category/", views.CategoryListView.as_view(), name="fake-checker_Category_list"),
    path("fake-checker/Category/create/", views.CategoryCreateView.as_view(), name="fake-checker_Category_create"),
    path("fake-checker/Category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="fake-checker_Category_detail"),
    path("fake-checker/Category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="fake-checker_Category_update"),
    path("fake-checker/QuestionFromUser/", views.QuestionFromUserListView.as_view(), name="fake-checker_QuestionFromUser_list"),
    path("fake-checker/QuestionFromUser/create/", views.QuestionFromUserCreateView.as_view(), name="fake-checker_QuestionFromUser_create"),
    path("fake-checker/QuestionFromUser/detail/<int:pk>/", views.QuestionFromUserDetailView.as_view(), name="fake-checker_QuestionFromUser_detail"),
    path("fake-checker/QuestionFromUser/update/<int:pk>/", views.QuestionFromUserUpdateView.as_view(), name="fake-checker_QuestionFromUser_update"),
    path("fake-checker/QuestionForExpert/", views.QuestionForExpertListView.as_view(), name="fake-checker_QuestionForExpert_list"),
    path("fake-checker/QuestionForExpert/create/", views.QuestionForExpertCreateView.as_view(), name="fake-checker_QuestionForExpert_create"),
    path("fake-checker/QuestionForExpert/detail/<int:pk>/", views.QuestionForExpertDetailView.as_view(), name="fake-checker_QuestionForExpert_detail"),
    path("fake-checker/QuestionForExpert/update/<int:pk>/", views.QuestionForExpertUpdateView.as_view(), name="fake-checker_QuestionForExpert_update"),
)
