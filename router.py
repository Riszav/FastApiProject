from fastapi import APIRouter, Depends
from typing import Optional, Annotated
from pydantic import BaseModel
from schemas import STaskAdd
from repository import TasksRepository
from schemas import STask, STackId

router = APIRouter(prefix="/tasks", tags=["Таски"])


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STackId:
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    task = await TasksRepository.find_all()
    return {"tasks": task}