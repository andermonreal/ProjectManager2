from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

class UserManager:
    def get_by_email(self, email):
        try:
            return User.objects.filter(email=email).first()
        except self.model.DoesNotExist:
            return None

    def create_user(self, name, email, password, phone, birthday, **extra_fields):
        try:
            if not User.is_older_than(birthday, 18):
                raise ValueError("The user must be of legal age")
            
            return User.objects.create_user(name, email, password, phone, birthday, **extra_fields)
        except ValueError as e:
            raise ValueError(f"Error creating user: {e}")

    def create_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
