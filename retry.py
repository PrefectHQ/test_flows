import time
from datetime import datetime

from prefect import flow, task
import random



@task(name="Test Task")
def test_task(my_range):
    print(my_range)
    time.sleep(5)
    print(datetime.today())
    
    
@task(name="Test Task")
def fail_task(my_range):
    print(my_range)
    time.sleep(5)
    print(datetime.today())
    newNum = random.randint(0,9)
    if newNum > 5:
        raise ValueError("This is a random failure")
    
@flow
def many_mapped_tasks_flow(persist_result=True):
    iterate_list = [x for x in range(30)]
    test_task.map(iterate_list)

@flow
def myImportantFlow(persist_result=True):
    fail_task(3)
    many_mapped_tasks_flow()
    test_task(1)
    