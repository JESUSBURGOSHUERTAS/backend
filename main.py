from fastapi import FastAPI
from routes.task import task
app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI!"}

app.include_router(task) # incluye las rutas de task.py

