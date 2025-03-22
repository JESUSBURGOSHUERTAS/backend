from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# Modelo de entrada: sin id
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Modelo de salida: incluye el id asignado
class TaskOut(Task):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
