from fastapi import FastAPI, Path
from typing import Annotated

api = FastAPI()

user = {'1': 'Имя: Example, возраст: 18'}

@api.delete('/user/{user_id}')
async def main5(user_id: str):
    del user[user_id]
    return "Delete"

@api.post("/user/{username}/{age}")
async def main2(username: str, age: int):
    user[str(int(max(user, key=int))+1)]=f'Имя: {username}, возраст:{age}'
    return f'User {str(int(max(user, key=int))+1)} is registered'



@api.put('/user/{user_id}/{username}/{age}')
async def main4(user_id: str, username: str, age: int):
    user[user_id] = f'Имя: {username}, возраст:{age}'
    return f'The user {user_id} is registered'



@api.get('/')
async def main3():
    return 'Hellow'

@api.get('/user')
async def main():
    return user







