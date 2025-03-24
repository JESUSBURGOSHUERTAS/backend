from fastapi import APIRouter, HTTPException
from app.services.task_service import (
    get_all_task, create_task, get_one_task, get_one_task_id, delete_task, update_task
)
from app.schemas.task import Task,TaskOut, UpdateTask

task = APIRouter()

@task.get("/api/tasks", response_model=list[TaskOut])
async def get_tasks():
    task = await get_all_task()
    return task

@task.post("/api/tasks", response_model=TaskOut)
async def save_task(task: Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(400, "Task already exists") 
    created_task = await create_task(task.model_dump())
    if created_task:
        return created_task
    raise HTTPException(400, "Task not created")

@task.get("/api/tasks/{id}", response_model=TaskOut)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Task with id {id} not found')

@task.put("/api/tasks/{id}", response_model=TaskOut)
async def put_task(id: str, task: UpdateTask):
    response = await update_task(id, task.model_dump()) # Aqui se hace el update con el id y el task
    if response:
        return response
    return HTTPException(404, f'Task with id {id} not found')

@task.delete("/api/tasks/{id}")
async def remove_task(id: str):
   response = await delete_task(id)
   if response:
        return "Task deleted successfully"
   raise HTTPException(404, f'Task with id {id} not found')

