from prefect import flow

@flow
def tay():
    print("Hello world")
    
if __name__ == "__main__":  
    tay()