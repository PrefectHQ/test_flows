import time
from prefect import flow, get_run_logger, task
import requests


def on_cancel():
    requests.get('https://api.stg.prefect.dev/hooks/McaomIEor--VLWBfFuy36w')
    print('called!')

@task
def sample_task():
    logger = get_run_logger()
    logger.info('Task running!')
    time.sleep(100)

@flow(on_cancellation=[on_cancel])
def sample_flow():
    sample_task.submit()

sample_flow()