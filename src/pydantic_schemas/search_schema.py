from typing import List, Optional
from pydantic import BaseModel, field_validator


class Search(BaseModel):
     total: int
     objectIDs: List[int] = []

     # @field_validator('objectIDs')
     # def validate_objectIDs(cls, value):
     #      assert len(set(value)) != len(value), "Идентификаторы в objectIDs не уникальны"



