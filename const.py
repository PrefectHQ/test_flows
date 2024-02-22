from typing import Union
from prefect import flow
from pydantic import BaseModel, Extra, Field


class CustomConfig(BaseModel, extra=Extra.forbid):
    value: float


class DefaultConfig(BaseModel, extra=Extra.forbid):
    value: float = Field(
        default=0.1,
        Literal=True,
    )


class FlowConfig(BaseModel, extra=Extra.forbid):
	config: CustomConfig | DefaultConfig


@flow()
async def my_flow(
    configuration: FlowConfig,
) -> None:
    # do something
	...