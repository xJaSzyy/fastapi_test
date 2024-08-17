from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import TaskAdd, Task, TaskId

router = APIRouter(
    prefix="/task",
    tags=["Tasks"]
)


@router.get("")
async def get_all_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.post("")
async def add_task(
        task: Annotated[TaskAdd, Depends()]
) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}
