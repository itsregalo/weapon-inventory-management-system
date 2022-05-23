from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


# class to generate token for password reset
class AppTokenGenerator(PasswordResetTokenGenerator):

    # method to make hash key
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))

# calling the class
token_gen = AppTokenGenerator()