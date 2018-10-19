from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        """
        应用的初始化
        """
        # 导入signal处理器
        import user.signals
