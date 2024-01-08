from typing import Optional

from prefect import flow
from pydantic import BaseModel, Field

class PydanticFieldsDefault(BaseModel): 
    str_field_default: Optional[str] = Field(
        title="Title str_field_default", description="Description str_field_default"
    )
@flow(log_prints=True)
def optional(pydantic_fields_default: PydanticFieldsDefault = PydanticFieldsDefault()):
    print(pydantic_fields_default)
    return pydantic_fields_default

if __name__ == "__main__":
    optional.serve(name="print")