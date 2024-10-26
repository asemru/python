from fastapi import FastAPI
from homework2 import task, user

apo = FastAPI()

@apo.get('/')
async def welcome():
    return {'message': 'welcome, this is my project'}




