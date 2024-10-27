from fastapi import APIRouter
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from homework.backend import db


app = APIRouter(prefix='/user', tags=['user'])

class User(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, index=True, unique=True)
    tasks = relationship('Task', back_populates='user')




@app.get('/')
async def all_task():
    pass

@app.get('/user_id')
async def user_by_id():
    pass

@app.post('/create')
async def create_user():
    pass

@app.put('/update')
async def update_user():
    pass

@app.delete('/delete')
async def delete_user():
    pass
