from prefect import flow, get_run_logger, task

@task
def task1(item: int) -> dict:
    logger = get_run_logger()
    logger.info(f"Starting task1 for item {item}")
    return {"item": item}


@task
def task2(d: dict) -> dict:
    logger = get_run_logger()
    logger.info(f"Starting task2 for dict {d}")
    return {"item": d["item"] + 1}


@task
def task3(d: dict) -> dict:
    logger = get_run_logger()
    logger.info(f"Starting task3 for dict {d}")
    return {"item": d["item"] + 1}



@flow
def mapped_tasks(num: int = 1000):
    '''MRE for a [flow that has 1000+ mapped tasks that used to hang](https://github.com/PrefectHQ/prefect/issues/8770)
    ```python
    from prefect import flow, get_run_logger, task


@flow(name="problem-demo")
def problem_workflow():
    number_of_items = 1000
    items = list(range(0, number_of_items))

    logger = get_run_logger()
    logger.info(f"Starting flow for list of {len(items)} items")

    results1 = task1.map(items)
    results2 = task2.map(results1)
    results3 = task3.map(results2)

    return results3


@task
def task1(item: int) -> dict:
    logger = get_run_logger()
    logger.info(f"Starting task1 for item {item}")
    return {"item": item}


@task
def task2(d: dict) -> dict:
    logger = get_run_logger()
    logger.info(f"Starting task2 for dict {d}")
    return {"item": d["item"] + 1}


@task
def task3(d: dict) -> dict:
    logger = get_run_logger()
    logger.info(f"Starting task3 for dict {d}")
    return {"item": d["item"] + 1}
```
    '''
    number_of_items = num
    items = list(range(0, number_of_items))

    logger = get_run_logger()
    logger.info(f"Starting flow for list of {len(items)} items")

    results1 = task1.map(items)
    results2 = task2.map(results1)
    results3 = task3.map(results2)

    return results3

if __name__ == "__main__":
    mapped_tasks.deploy(
        parameters={'num': 100},
        name="mapped-deploy",
        work_pool_name="azure-push-work-pool",
        image="jennyprefect/dep:mapped")
