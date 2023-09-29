import time

from prefect import task, flow

@task(tags=["foo"])
def sleep_task(num: int):
    time.sleep(num)


@flow()
def sleep_flow() -> None:
    sleep_task.map([1000000,20000000,3000000,4000000,50000000,6000000,7000000,80000000,90990,100000])

sleep_flow()