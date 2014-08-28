from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model

from .models import MinecraftAccount


User = get_user_model()


def create_minecraft_user(username, password, profiles, primary):
    try:
        validate_email(username)
    except ValidationError:
        email = None
    else:
        email = username

    # Save user
    user = User(username=username, email=email)
    user.set_password(password)  # Encrypted
    user.save()

    # Save profiles
    for profile in profiles:
        MinecraftAccount.objects.create(
            user=user,
            profile=profile.get('name'),
            profile_id=profile.get('id'),
            primary=primary,
        )

    return user
