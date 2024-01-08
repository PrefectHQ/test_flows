from prefect import flow, deploy

if __name__ == "__main__":

    deploy(
        flow.from_source(
            source="https://github.com/PrefectHQ/test_flows.git",
            entrypoint="basic_flow.py:basic_flow",
        ).to_deployment(
            name="azure-test-deploy",
        ),
        work_pool_name="abc-work-pool",
    )