from prefect import flow
import time


@flow(log_prints=True)
def local_flow(sleep:int=1):
    time.sleep(sleep)
    print("I'm a flow written to test flow.deploy using a local docker worker")


if __name__ == "__main__":
    local_flow.deploy(
        name="test-remote-flow-deploy-docker-worker",
        work_pool_name="docker",
        image_name="jennyprefect/dep",
        tag="dev",
        build_kwargs={"pull": False}
    )