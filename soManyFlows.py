from prefect import flow

if __name__ == "__main__":
    # generate 500 flows and run them
    for i in range(500):
        exec(f"@flow()\ndef f_{i}(): print({i})")
    for i in range(500):
        exec(f"f_{i}()")