from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/1'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=60),  # 每10秒一次
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=22, minute=10),    # 每天几点几分执行
        'args': (4, 5)
    }
}
