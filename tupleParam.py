from typing import Tuple

from prefect import flow


@flow(log_prints=True)
def tuple_flow(tuple:Tuple[str, int, float] = ("a", 1, 1.0)):
    print(tuple)
    return tuple

if __name__ == "__main__":
    tuple_flow.serve(parameters=dict(tuple=("b", 2, 2.0)))