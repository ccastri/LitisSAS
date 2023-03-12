from pydantic import BaseModel
from typing import Optional, List


class Plan (BaseModel):
    id: int
    name: str
    description: str
    price: str
    risk_level: List[int]
    img: Optional[str]
    role: str
    # google: False
