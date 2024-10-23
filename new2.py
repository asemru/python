from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def main():
    return 'Главная страница'





@app.get('/user/admin')
async def main2():
    return "Вы вошли как администратор"



@app.get('/user/{user_id}')
async def main3(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def main4(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")], age: int =
Path(ge=18, le=20, description='Enter age')):
    return f'Пользователь - {username},возраст - {age}'
