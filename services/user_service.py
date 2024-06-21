from utils import hash_password 
from repositories.user_repository import register, login
from models import UserRegister, UserLogin

def arrange_register(user: UserRegister):
    user.password = hash_password(user.password)
    return register(user)

def arrange_login(user: UserLogin):
    user.password = hash_password(user.password)
    return login(user)