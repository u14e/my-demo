import djcelery
from datetime import timedelta

djcelery.setup_loader()

CELERY_QUEUES = {
    # 定时任务的队列
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    # 默认普通的队列
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }
}

# 设置默认队列
CELERY_DEFAULT_QUEUE = 'work_queue'

CELERY_IMPORTS = (
    'course.tasks'
)

# 防止死锁
CELERY_FORCE_EXECV = True

# 设置并发worker数（看CPU）
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course-task',
        'schedule': timedelta(seconds=5),  # 每5秒一次
        'options': {
            'queue': 'beat_tasks'
        }
    }
}