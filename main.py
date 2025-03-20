from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI!"}

@app.get("/api/tasks")
async def get_tasks():
    return "all tasks"

@app.post("/api/tasks")
async def create_task():
    return "task created"

@app.get("/api/tasks/{id}")
async def get_task():
    return "single task"

@app.put("/api/tasks/{id}")
async def update_task():
    return "update task"

@app.delete("/api/tasks/{id}")
async def delete_task():
    return "delete task"


