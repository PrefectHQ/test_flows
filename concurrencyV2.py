import time
from datetime import datetime

from prefect import flow, task, get_run_logger
from prefect.concurrency.sync import concurrency

@task(name="Test Task")
def test_task(my_range):
    with concurrency("vbc"):
        logger = get_run_logger()
        logger.info(my_range)
        time.sleep(5)
        logger.info(datetime.today())

@flow
def many_mapped_tasks_flow_conc():
    '''MRE for a [flow that has 1000+ mapped tasks](https://github.com/PrefectHQ/prefect/issues/7393)
    ```python
    from prefect import flow, task
    from datetime import datetime
    import time
    
    @task(name="Test Task")
    def test_task(my_range):
        logger = get_run_logger()
        logger.info(my_range)
        time.sleep(5)
        logger.info(datetime.today())
        
        @flow(name="Test Flow")
        def many_mapped_tasks_flow():
            iterate_list = [x for x in range(3000)]
            blah = test_task.map(iterate_list)
            print(blah)
            ```
            '''

    iterate_list = [x for x in range(30)]
    blah = test_task.map(iterate_list)
    print(blah)

if __name__ == "__main__":
    with concurrency("vb1"):
        many_mapped_tasks_flow_conc()