from django.contrib.auth import get_user_model

User = get_user_model()

def create_new_user(data, *args, **kwargs) -> User:
        password = data.pop("password")
        user_instance = User(**data)
        user_instance.set_password(password)
        user_instance.save()
        return user_instance