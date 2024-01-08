from typing import Optional

from prefect import flow
from prefect.deployments import Deployment
from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str

class Postcard(BaseModel):
    sender: Optional[Person]
    recipient: Person
    text: str

@flow(log_prints=True)
def send_postcard(postcard: Postcard):
    print(f"Sending {postcard.text} to {postcard.recipient} (sender: {postcard.sender})")

my_postcard = Postcard(
    recipient=Person(first_name="My", last_name="Friend"),
    text="Greetings from Prefect"
)

if __name__ == "__main__":
    send_postcard.serve(name="postcardParams", parameters={"postcard": my_postcard})

