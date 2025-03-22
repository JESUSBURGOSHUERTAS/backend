from motor.motor_asyncio import AsyncIOMotorClient
from models import Task, TaskOut
from bson import ObjectId


client = AsyncIOMotorClient('mongodb://localhost')
database = client.taskdatabase
collection = database.tasks

async def get_one_task_id(id: str):
    task = await collection.find_one({"_id": ObjectId(id)})
    if task:
        task["_id"] = str(task["_id"])  # Convertir ObjectId a string
        return TaskOut.model_validate(task)  # Usar el modelo con alias
    return None

async def get_one_task(title):
    task = await collection.find_one({'title': title})
    return task


async def get_all_task():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        document["_id"] = str(document["_id"])  # Convertir ObjectId a string
        tasks.append(TaskOut.model_validate(document))  # Usar el modelo con alias
    return tasks
    

async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({'_id': new_task.inserted_id})
    # Convertir el _id de ObjectId a string:
    created_task['_id'] = str(created_task['_id'])
    return created_task


async def update_task(id: str, task):
    await collection.update_one({'_id': ObjectId(id)}, {'$set': task})
    document = await collection.find_one({'_id': id})
    return document

async def delete_task(id: str):
    await collection.delete_one({'_id': ObjectId(id)})
    return True

