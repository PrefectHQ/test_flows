from datetime import timedelta
from prefect import flow, task
from prefect.tasks import task_input_hash
import time

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1), tags=['jenny'])
def hello_task(name_input, sleepTime:int=1):
    # Doing some work
    print("Saying hello")
    time.sleep(sleepTime)
    return "hello " + name_input

@flow
def hello_flow(name_input, sleepTime:int=1):
    hello_task(name_input, sleepTime)

if __name__ == "__main__":
    hello_flow.deploy(
        name="cache-flow",
        work_pool_name="ui-sandbox-worker",
        image="jennyprefect/dep",
    )

    # hello_flow.serve('cacheHello', parameters={'name_input': 'world', 'sleepTime': 1})