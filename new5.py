from fastapi import FastAPI, status, Body, HTTPException, requests
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')
dict_humans = []

class Model(BaseModel):
    id: int
    name: str
    age: int


@app.get('/')
async def main(request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'messages': dict_humans})




@app.get('/user/{user_id}')
async def new_func(request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': user_id})


@app.post('/user')
async def main2(user: Model) -> list:
    user.id = len(dict_humans)
    dict_humans.append(user)
    return dict_humans



