import asyncio

from prefect import task, get_run_logger, flow


@task
async def task1():
    await asyncio.sleep(1)


@task
def task2():
    logger = get_run_logger()
    logger.info("hi")


@flow
async def sync_async_flow():
    '''MRE for a [flow that mixes async and sync tasks](https://github.com/PrefectHQ/prefect/issues/6318)
    ```python
    import asyncio

from prefect import task, get_run_logger, flow


@task
async def task1():
    await asyncio.sleep(1)


@task
def task2():
    logger = get_run_logger()
    logger.info("hi")


@flow
async def test_flow():
    await task1.submit()
    task2.submit() # raises here
    ```
    '''
    await task1.submit()
    task2.submit() # raises here