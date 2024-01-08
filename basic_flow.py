from prefect import flow, task

@task(log_prints=True, name="I have a really really really long task name")
def long_long_long_long_long_name():
    print("hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi hi")
    return "hi"

@flow(log_prints=True)
def basic_flow(hi:str="hi"):
    long_long_long_long_long_name()
    print(hi, "new world new world new world new world new world new new world  new world   new world   new world   new world   new world   new world   new world   new world   new world   new world   new world   new world   v       v   vvvnew world")
    return hi

if __name__ == "__main__":
    basic_flow.serve(name="print")