from fastapi import FastAPI
from app.api.v1.routes.task import task
# from app.api.v1.routes.company import company

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI!"}

app.include_router(task, prefix="/api/v1/tasks", tags=["Tasks"])
# app.include_router(company, prefix="/api/v1/companies", tags=["Companies"])
