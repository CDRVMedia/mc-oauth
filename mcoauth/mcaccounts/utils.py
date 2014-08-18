from django.contrib.auth import get_user_model

from .models import MinecraftAccount


User = get_user_model()


def create_minecraft_user(email, password, profiles, primary):
    # Save user
    user = User(email=email)
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
