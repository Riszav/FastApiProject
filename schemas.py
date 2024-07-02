from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


class STackId(BaseModel):
    ok: bool = True
    tack_id: int