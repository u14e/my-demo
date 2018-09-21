from celery import Celery

# fix windows bug
# 参考链接：https://github.com/celery/celery/issues/4081
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('demo')
app.config_from_object('celery_app.celery_config')