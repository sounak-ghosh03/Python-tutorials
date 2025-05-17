from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str


class Settings(BaseModel):
    app_name: str = "app"
    admin_email: str = "0N@example.com"


def get_settings():
    return Settings()


@app.post('/signup')
def signup(user: UserSignUp):
    return {'message': f'User {user.username} signed up successfully'}


@app.get('/settings')
def get_setttings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
