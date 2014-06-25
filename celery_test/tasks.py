from celery.task import task
from celery import current_task
from celery_test.models import CounterModel
from time import sleep

@task()
def add_two_numbers(a, b):
    """This is where you do the bulk of the your queued task needs to do"""
    sleep(10)
    count = CounterModel.objects.create(count = a + b)
    return count

@task()
def do_something_long():
    for i in range(100):
        sleep(0.2)
        current_task.update_state(state="PROGRESS", meta={'current':i, 'total':100})