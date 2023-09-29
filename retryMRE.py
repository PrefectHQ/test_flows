from prefect import task, flow
from prefect.deployments.deployments import Deployment
from prefect.task_runners import SequentialTaskRunner
import asyncio

@task(persist_result=True)
def task_1():
    print("success!")

@task(persist_result=True)
def task_2():
    raise RuntimeError

@task(persist_result=True)
def task_3():
    print("success!")

@flow(task_runner=SequentialTaskRunner(), persist_result=True)
def demo_restart_issue():
    task_1()
    task_2()
    task_3()

async def deploy():
    local_deployment = await Deployment.build_from_flow(
        flow=demo_restart_issue,
        name=f"deployment_demo_restart_issue",
    )
    await local_deployment.apply()


if __name__ == "__main__": 
    asyncio.run(deploy())