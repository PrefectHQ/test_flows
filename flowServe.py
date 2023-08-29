import asyncio
from prefect import flow, task
from datetime import timedelta
import time

@task
def sleep():
	time.sleep(50)

@flow(log_prints=True)
def no_work_pool(name:str="I'm a parameter!"):
	"""This is a flow that will be run via .serve()!
```python
import asyncio
from prefect import flow, task
from datetime import timedelta
import time

@task
def sleep():
	time.sleep(50)

@flow(log_prints=True)
def no_work_pool(name:str="I'm a parameter!"):
	sleep()
	print("I'm run via .serve()!")
	print(name)

if __name__ == "__main__":
	no_work_pool.serve(__file__, parameters=dict(name="I'm a parameter 2!"))
```
"""
	sleep()
	print("I'm run via .serve()!")
	print(name)

if __name__ == "__main__":
	no_work_pool.serve(__file__, parameters=dict(name="I'm a parameter 2!"), tags=["test", "served"])