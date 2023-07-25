from prefect import task, flow, pause_flow_run

@task
def marvin_setup():
    return "a raft of ducks walk into a bar..."
@task
def marvin_punchline():
    return "it's a wonder none of them ducked!"
@flow
def inspiring_joke():
    marvin_setup()
    pause_flow_run(timeout=31536000)  
    marvin_punchline()

if __name__ == "__main__":
    inspiring_joke()