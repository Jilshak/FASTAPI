from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello world'}

@app.post('/', description="This is the first route")
async def the_post_route():
    return {'message': 'hello from post route'}

@app.get('/items')
async def get_list_items():
    return {"Message":"this is the list items"}

@app.get('/items/{item_id}')
async def get_item(item_id : int):
    return {"item_id": item_id}