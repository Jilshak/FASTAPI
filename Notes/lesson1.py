# main.py --> the base of fast api

# the bease of the fastapi is this file
# import fast api and instatiate our app

# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/')
# async def root():
#     return {'message': 'Hello world'}

# This is how we write the basic fastapi root

# > To run the server you need to use the command:

#  >> uvicorn main:app
# > main is the file name
# > app is the name of fastapi

#  > IN THE COMMAND  uvicorn main:app you can use multiple flags like

# > uvicorn main:app --port=8001
# > uvicorn main:app --reload
# >> this flag reloads the app whenever there is a change in the app so that we don't need to reload every time

# fast api has its own default api documentation created when we create endpoints.

#  > we jsut need to go to the localhost that is 128.0.0.1:8000/docs

#   > inside the docs we can see many details and by adding many things to the app methods itself

# @app.post('/')
# async def post():
#     return {'message': 'hello from post route'}

# by changing the name of the functoin the docs name for that route also changes

#  async def this_is_post():
# return {"Message": "This is the post route"}

#  now if we were to check the docs we can see that the route with the post method will be called the 'this_is_the_post'

# similarly we can also add description to the route like:

# app.post('/', descriptoin="This is the first route")
#  async def this_is_the_post():
# return {"Message":"This is the post route"}

#  also add deprecated route

# app.post('/', descriptoin="This is the first route", deprecated=True)
#  async def this_is_the_post():
# return {"Message":"This is the post route"}
