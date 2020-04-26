from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'football_app._auth'

    def ready(self):
        import football_app._auth.signals
