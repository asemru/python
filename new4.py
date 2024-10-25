from fastapi import HTTPException, Body, FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []
x = 0

class Model(BaseModel):
    id: int
    username: str
    age: int

@app.get('/')
async def main() -> List[Model]:
    return users

@app.delete('/users/{user_id}')
async def main6(user_id: int):
    try:
        users.pop(user_id)
        return users
    except:
        raise HTTPException(status_code=404, detail='User was not found')

@app.post('/user')
async def main2(user: Model) -> str:
    user.id = len(users)
    users.append(user)
    return "All"

@app.put('/user/{user_id}/{username}/{age}')
async def main3(user_id: int, username: str, age: int):
    try:
        useri = users[user_id]
        useri.username = username
        useri.age = age
        return 'You all!'
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')



