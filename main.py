from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Удаление")
    await create_tables()
    print("Готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)









#
# @app.post("/tasks/")
# async def add_task(task: Annotated[STaskAdd, Depends()]):
#     tasks.append(task)
#     return {"ok": True}
#     # return STask(
#     #     id=1,
#     #     name=task.name,
#     #     description=task.description,
#     # )
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.get("/tasks/")
# async def get_tasks():
#     task = Task(name="test", description="test")
#     return {"data": task}
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
