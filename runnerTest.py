from prefect import flow, Runner

@flow(log_prints=True)
def local_flow():
    print("I'm a locally defined flow!")

runner = Runner()
runner.add_flow(local_flow, "test-runner-deploy")
runner.add_flow(
    flow.from_source(
        source="https://github.com/PrefectHQ/test_flows.git", entrypoint="runnerTest.py:local_flow"
    ),
    "test-from-public-source",
)