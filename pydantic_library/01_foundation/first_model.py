from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool


# if any data is in wrong format/datatype then pydantic tries to convert the values into expected type if it fails then raises type error
input_data = {'id': 101, 'name': "Chai", 'is_active': True}

user = User(**input_data)
print(user)
