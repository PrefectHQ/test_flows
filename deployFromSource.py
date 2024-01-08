from prefect import deploy, flow

@flow(log_prints=True)
def local_flow():
    print("I'm the flow that was created locally")

if __name__ == "__main__":
    deploy(
        local_flow.to_deployment(name="local-deploy-flow"),
        flow.from_source(
            source="https://github.com/PrefectHQ/test_flows.git",
            entrypoint="basic_flow.py:basic_flow",
        ).to_deployment(
            name="remote-deploy-flow",
        ),
        work_pool_name="ui-sandbox-worker",
        image_name="jennyprefect/dep",
        tag="dev",
		build_kwargs={"pull": False}
    )