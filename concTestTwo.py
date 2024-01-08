from prefect import flow, task, get_run_logger
import time

@task(tags=["jenny"])
def log_something(x):
    logger = get_run_logger()
    logger.info(f"this is log number {x}")
    time.sleep(60)

@flow
def smoke_test_flow():
    for x in range(0, 100):
        log_something.submit(x)

if __name__ == "__main__":
    smoke_test_flow()