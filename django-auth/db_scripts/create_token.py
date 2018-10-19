import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

if __name__ == '__main__':
    import django
    django.setup()

    from django.contrib.auth import get_user_model
    from rest_framework.authtoken.models import Token

    User = get_user_model()

    # 为所有已经存在的用户创建token
    for user in User.objects.all():
        Token.objects.get_or_create(user=admin)