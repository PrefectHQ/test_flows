from prefect import flow

@flow(log_prints=True)
def sub_flow():
    print('hi sub flow')
    # raise Exception("Error") #COMMENT THIS CODE LATER
    return

@flow(log_prints=True)
def main_flow():
    print('hi')
    sub_flow()

if __name__ == "__main__":
    main_flow.serve('serve', interval=60)
