from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello world'}

@app.post('/', description="This is the first route")
async def the_post_route():
    return {'message': 'hello from post route'}