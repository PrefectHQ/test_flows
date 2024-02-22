from datetime import timedelta
from prefect import flow, task
from prefect.tasks import task_input_hash
import time
from prefect.artifacts import create_link_artifact

@task(cache_expiration=timedelta(days=1), tags=['jenny'], cache_key_fn=task_input_hash)
def hello_task(name_input, sleepTime:int=1):
    # Doing some work
    print("Saying hello")
    time.sleep(sleepTime)
    return "hello " + name_input

@task(cache_expiration=timedelta(days=1), tags=['jenny'], cache_key_fn=task_input_hash)
def my_first_link_task():
        create_link_artifact(
            key="variable-data-link",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data_.csv",
            description="## Highly variable data",
            link_text="Highly variable data",
        )

@flow
def hello_flow(name_input, sleepTime:int=1):
    hello_task(name_input, sleepTime)
    my_first_link_task()

if __name__ == "__main__":
    # hello_flow.deploy(
    #     name="cache-flow",
    #     work_pool_name="ui-sandbox-worker",
    #     image="jennyprefect/dep",
    # )

    # hello_flow.serve('cacheHello', parameters={'name_input': 'world', 'sleepTime': 1})
    hello_flow(name_input='world', sleepTime=1)