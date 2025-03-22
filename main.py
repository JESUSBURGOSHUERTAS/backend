from fastapi import FastAPI, HTTPException
from database import get_all_task, create_task, get_one_task, get_one_task_id, delete_task
from models import Task,TaskOut
app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI!"}

@app.get("/api/tasks", response_model=list[TaskOut])
async def get_tasks():
    task = await get_all_task()
    return task

@app.post("/api/tasks", response_model=TaskOut)
async def save_task(task: Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(400, "Task already exists") 
    created_task = await create_task(task.model_dump())
    if created_task:
        return created_task
    raise HTTPException(400, "Task not created")

@app.get("/api/tasks/{id}", response_model=TaskOut)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Task with id {id} not found')

@app.put("/api/tasks/{id}")
async def update_task():
    return "update task"

@app.delete("/api/tasks/{id}")
async def remove_task(id: str):
   response = await delete_task(id)
   if response:
        return "Task deleted successfully"
   raise HTTPException(404, f'Task with id {id} not found')


