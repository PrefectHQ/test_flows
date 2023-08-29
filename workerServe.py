import asyncio
from datetime import timedelta

from prefect import flow
from prefect.client.schemas.schedules import IntervalSchedule
from prefect.workers.process import ProcessWorker, DeployConfig


@flow
def my_flow_1():
    print("I'm the first flow run via an in-memory worker!")


@flow
def my_flow_2():
    print("I'm the second flow run via an in-memory worker!")


if __name__ == "__main__":
    asyncio.run(
        ProcessWorker(work_pool_name="serve-test").serve(
            [
                my_flow_1,
                DeployConfig(
                    flow=my_flow_2,
                ),
            ]
        )
    )