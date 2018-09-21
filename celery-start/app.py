from celery_app import task1, task2


if __name__ == '__main__':
    print('start task....')
    task1.add.delay(2, 4)
    task2.multiply.delay(4, 5)
    print('end task....')