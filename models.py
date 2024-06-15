from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    user_name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    user_name: str
    password: str

class UserOut(BaseModel):
    user_name: str
    email: EmailStr