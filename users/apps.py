from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # import signals to allow creation of profiles for users automatically
    def ready(self):
        import users.signals