from prefect.events import emit_event
from time import sleep

def emit_three_events():
    for _ in range(3):
        emit_event(event="external.resource.pinged", resource={"prefect.resource.id": "my.external.resource"})
    sleep(3)
    emit_event(event="external.resource.pinged", resource={"prefect.resource.id": "my.external.resource"})

if __name__ == "__main__":
    emit_three_events()