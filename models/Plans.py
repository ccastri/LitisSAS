from pydantic import BaseModel
from typing import Optional, List


class Plan (BaseModel):
    id: int
    name: str
    description: str
    price: List[str]
    # risk_level: List[int]
    img: str
    # isSelected: bool
    # google: False
