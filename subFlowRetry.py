from prefect import flow

@flow
def sub_flow():
    # raise Exception("Error") #COMMENT THIS CODE LATER
    return

@flow
def main_flow():
    sub_flow()

