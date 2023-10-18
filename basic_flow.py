from prefect import flow

@flow (log_prints=True)
def basic_flow(hi:str="hi"):
    print(hi, "world")
    return hi