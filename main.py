from fastapi import FastAPI, HTTPException
from database import get_all_task, create_task
from models import Task
app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI!"}

@app.get("/api/tasks")
async def get_tasks():
    task = await get_all_task()
    return task

@app.post("/api/tasks", response_model=Task)
async def save_task(task: Task): #recibe una task de tipo Task especificado en el modelo
    response = await create_task(task.model_dump())
    if response:
        return response
    raise HTTPException(400, "Task not created")
    

@app.get("/api/tasks/{id}")
async def get_task():
    return "single task"

@app.put("/api/tasks/{id}")
async def update_task():
    return "update task"

@app.delete("/api/tasks/{id}")
async def delete_task():
    return "delete task"


