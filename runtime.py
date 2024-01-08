from prefect import flow, runtime
import datetime


def get_flow_run_name():
    date = datetime.datetime.now().isoformat()
    print('bob', runtime)
    print(f"{runtime.deployment.name}-{date}")

@flow(log_prints=True, flow_run_name=get_flow_run_name())
def hi_named_flow(name:str="world"):
    '''
#Flow code

```python
from prefect import flow, runtime
import datetime

def get_flow_run_name():
    date = datetime.datetime.now().isoformat()
    print('bob')
    print(f"{runtime.deployment.name}-{date}")

```

'''
    print(f"Hi {name}")

if __name__ == "__main__":
    hi_named_flow.serve(name="bob")