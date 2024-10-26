from fastapi import APIRouter

api = APIRouter(prefix='/task', tags=['task'])

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
