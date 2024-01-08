from prefect import flow, task
from prefect.concurrency.sync import concurrency

@task
def process_data(i):
    with concurrency("database", occupy=1):
        return i

@flow
def my_flow():
    for i in range(100):
        process_data.submit(i)

if __name__ == "__main__":
    my_flow()