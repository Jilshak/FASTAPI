from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get('/')
async def root():
    return {"Message": "This is the root page"}

todos = []

# get all todo


@app.get("/todos")
async def get_todos():
    return {"Todos": todos}

# get a single todo

@app.get('/todos/{todo_id}')
async def get_single_todo(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            return {"Todo": todo}
    return {"Message": "item is not present"}

# create a todo


@app.post('/todos')
async def cretate_todos(todo : Todo):
    print("The new todo is: ", todo)
    todos.append(todo)
    return {'Created Todos': todos}

# update a todo
@app.put('/todos/{todo_id}')
async def update_todo(todo_id:int, todo: Todo):
    for i in todos:
        if i.id == todo_id:
            i.id = todo_id
            i.item = todo.item
            return {'Todo':i}
    return {'Message': "No todos found by the id you have given"}
            

# delete a todo
@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id: int):
    for i in todos:
        if i.id == todo_id:
            todos.remove(i)
        else:
            pass
    return {"Message":todos}
