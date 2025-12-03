from django.contrib.auth import authenticate
from datetime import date
import logging

logger = logging.getLogger(__name__)

class RegisterService:
    def __init__(self, manager):
        self.manager = manager

    def execute(self, name: str, email: str, password: str, phone: str, birthday: date):
        user = self.manager.get_by_email(email)

        if user:
            logger.warning(f"Registration failed, duplicate registration attempt: {email}")
            raise ValueError(f"Registration failed, duplicate registration attempt: {email}")
    
        try:
            user = self.manager.create_user(name, email, password, phone, birthday)
            logger.info(f"User registered succesfully: {email}")

            print("Usuario creado en el servicio")
            print(user)
            return user

        except ValueError as e:
            logger.warning(f"Error registering user: {email} - {e}")
            raise ValueError(f"Error registering user: {email} - {e}")
        
class LoginService:
    def __init__(self, manager):
        self.manager = manager

    def execute(self, email: str, password: str):
        user_auth = authenticate(username=email, password=password)

        if not user_auth:
            logger.warning(f"Login failed, invalid credentials: {email}")
            raise ValueError(f"Login failed, invalid credentials: {email}")
        if not user_auth.is_active:
            logger.warning(f"Login failed, account inactive: {email}")
            raise ValueError(f"Login failed, account inactive: {email}")

        token = self.manager.create_token(user_auth)
        
        logger.info(f"User logued: {email}")
        return user_auth, token