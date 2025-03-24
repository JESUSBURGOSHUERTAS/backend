from fastapi import FastAPI
from app.core.config import settings

from app.api.v1.routes.task import task
# from app.api.v1.routes.company import company

app = FastAPI()
# Mensaje según el entorno
if settings.ENVIRONMENT == "development":
    print("🔧 Ejecutando en modo DESARROLLO")
else:
    print("🚀 Ejecutando en modo PRODUCCIÓN")

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI!"}

app.include_router(task, tags=["Tasks"]) # prefix si quiero cambiar la ruta y tags es el nombre que aparece en la documentación
# app.include_router(company, prefix="/api/v1/companies", tags=["Companies"])
