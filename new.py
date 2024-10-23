from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return 'Главная страница'

@app.get('/user')
async def main4(username: str, age: int):
    return f'Пользователь - {username},возраст - {age}'

@app.get('/user/admin')
async def main2():
    return "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def main3(user_id: str):
    return f'Вы вошли как пользователь № {user_id}'






