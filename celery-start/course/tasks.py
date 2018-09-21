from celery.task import Task
import time


class CourseTask(Task):
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start course task')
        time.sleep(4)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('end course task')