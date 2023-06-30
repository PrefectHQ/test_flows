from prefect import flow

@flow
def basic_flow(hi:str="hi"):
    print(hi)
    return hi