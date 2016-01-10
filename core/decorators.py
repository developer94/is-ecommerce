from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def user_is_instance(model, login_url=None, raise_exception=False):
    def check_instance(user):
        if isinstance(user, model):
            return True
        else:
            raise PermissionDenied

        return False

    user_passes_test(check_instance, login_url=login_url)

