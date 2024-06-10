from typing import List
from pydantic import BaseModel, model_validator
from utils import check_uniqueness_id

class Search(BaseModel):
     total: int
     objectIDs: List[int] = []

     @model_validator(mode='after')
     def validate_objectIDs(self):
          check_uniqueness_id(self.objectIDs)
          assert self.total == len(self.objectIDs), f"total не равно objectIDs"
          return self



