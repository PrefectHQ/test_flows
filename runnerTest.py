from prefect import flow, Runner

@flow(log_prints=True)
def local_flow():
    print("I'm a locally defined flow!")

runner = Runner()
runner.add_flow(local_flow, "test-runner-deploy")
# runner.add_flow(
#     flow.from_source(
#         source="https://github.com/PrefectHQ/test_flows.git", entrypoint="retry.py:myImportantFlow"
#     ),
#     "test-from-public-source",
# )

# runner.serve()
# runner.build_image(image_name="test-runner-image-two", tag="latest", pull=False)
# runner.deploy(work_pool_name="ui-sandbox-worker")