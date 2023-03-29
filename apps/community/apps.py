from django.apps import AppConfig


class CommunityConfig(AppConfig):
    name = 'community'
    verbose_name = "社区"

    def ready(self):
        import community.signals