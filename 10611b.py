from typing import Any, Dict, Optional, Union
from prefect import flow, task

@task
def demo_task():
    print("Demo Task")

@flow
def demo_flow_optionalb(input_dict: Optional[Dict[str, Any]]):
    print("Demo Flow")
    demo_task()

