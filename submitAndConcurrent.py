import time

import prefect
from prefect.task_runners import ConcurrentTaskRunner


@prefect.task(tags=["foo"])
def sleep_task() -> None:
    time.sleep(20)


@prefect.flow(name="test", task_runner=ConcurrentTaskRunner())
def flow(bug: bool = True) -> None:
    for _ in range(10):
        if not bug:
            time.sleep(1)

        sleep_task.submit()
