from django.contrib.auth.mixins import AccessMixin

from FakeChecker.settings import MIN_REVIEWS_FOR_PUBLIC_QUESTION
from .models import Redactor, Expert


class PermissionMessages:
    general_permission_denied = "Nie masz uprawnień do przeglądania tej treści"


class RoleCheckMixin(AccessMixin):
    permission_denied_message = PermissionMessages.general_permission_denied


class IsRedactorMixin(RoleCheckMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            redactor = request.user.redactor
        except Redactor.DoesNotExist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsExpertMixin(RoleCheckMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            expert = request.user.expert
        except Expert.DoesNotExist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsRedactorQuestionsAuthorMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        no_permission = True
        try:
            redactor = request.user.redactor
            request.
        except Redactor.DoesNotExist:
            pass
        if no_permission:
            return self.handle_no_permission()


class IsNumberOfReviewsExceededMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        pass