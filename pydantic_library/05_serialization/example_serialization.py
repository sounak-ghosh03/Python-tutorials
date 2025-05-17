from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


# creating a user instance
user = User(
    id=1,
    name="Sounak Ghosh",
    email="3kKpA@example.com",
    createdAt=datetime.now(),
    address=Address(
        street="123 Main Street",
        city="kolkata",
        zip_code="12345"
    ),
    tags=["premium", "vip"]
)

# Using the model dump() that returns --> dictionary
python_dict = user.model_dump()
print(python_dict)


# Using the model dump_json() that returns --> json
json_string = user.model_dump_json()
print(json_string)
