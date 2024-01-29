from prefect import flow, pause_flow_run
from prefect.input import RunInput

class UserName(RunInput):
    name: str

@flow(log_prints=True)
async def greet_user():
    user_input = await pause_flow_run(
        wait_for_input=UserName
    )
    print(f"Hello, {user_input.name}!")

