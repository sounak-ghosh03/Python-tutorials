from pydantic import BaseModel, field_validator, model_validator, computed_field
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # self refencing comments


Comment.model_rebuild()

address = Address(
    street="123 Main Street",
    city="kolkata",
    postal_code="12345"
)

user = User(
    id=1,
    name="Sounak Ghosh",
    address=address
)

comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply2")
    ]
)
