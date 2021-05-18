from django.apps import AppConfig


class ProfileConfig(AppConfig):
    name = 'Profile'

    def ready(self):
        import Profile.signals