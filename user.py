from fastapi import APIRouter

app = APIRouter(prefix='/user', tags=['user'])

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
