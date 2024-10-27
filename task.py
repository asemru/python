from fastapi import APIRouter
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from homework.backend.db import *

api = APIRouter(prefix='/task', tags=['task'])

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, index=True, unique=True)
    user = relationship('User', back_populates='tasks')



@api.get('/')
async def all_task():
    pass

@api.get('/task_id')
async def task_by_id():
    pass

@api.post('/create')
async def create_task():
    pass

@api.put('/update')
async def update_task():
    pass

@api.delete('/delete')
async def delete_task():
    pass
