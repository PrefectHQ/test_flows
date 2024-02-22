from typing import Any, Dict, Optional, Union
from prefect import flow, task

@task
def demo_task():
    print("Demo Task")

@flow
def demo_flow_union(input_dict: Union[Dict[str, Any], str]):
    print("Demo Flow")
    demo_task()

@flow
def demo_flow_optional(input_dict: Optional[Dict[str, Any]]):
    print("Demo Flow")
    demo_task()