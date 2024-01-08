from prefect import flow, task, unmapped
from prefect.blocks.core import Block

from prefect.blocks.system import JSON

json_block = JSON.load("test")

@task
def accept_foo_and_block(foo: str, block: Block):
    print(f"Received foo {foo!r} of type {type(foo)}")
    print(f"Received block {block!r} of type {type(block)}")
    
@flow(log_prints=True)
def some_flow(block: Block, hello: str):
    print("This is a flow that accepts a block")
    accept_foo_and_block(block=block, foo=hello)
    print(block)

if __name__ == "__main__":
    some_flow.serve('block', parameters={'block': json_block, 'hello': 'world' })
    # some_flow(json_block,'world')