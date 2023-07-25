import time
from datetime import datetime

from prefect import flow, task


@task(name="Test Task")
def test_task(my_range):
    print(my_range)
    time.sleep(5)
    print(datetime.today())

@flow
def many_mapped_tasks_flow():
    iterate_list = [x for x in range(30)]
    test_task.map(iterate_list)

@flow
def parentFlow():
    many_mapped_tasks_flow()
    