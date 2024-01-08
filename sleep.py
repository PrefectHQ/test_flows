from prefect import flow, task
import time

@task()
def sleepy(sleep:int=5):
     time.sleep(sleep)

@flow(log_prints=True)
def sleep_flow(sleep:int=1):
    sleepy(sleep)
    print("I'm a flow written to test flow.deploy using a local docker worker")


if __name__ == "__main__":
    sleep_flow.deploy(
        name="sleepy-deploy",
        work_pool_name="ui-sandbox-worker",
        image="jennyprefect/dep:sleep",
    )