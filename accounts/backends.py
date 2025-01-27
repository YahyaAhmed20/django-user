from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Check if the input is an email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # Check if the input is a username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None  # No user found

        # Verify the password
        if user.check_password(password):
            return user
        return None  # Password is incorrect
    