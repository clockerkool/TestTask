from pydantic import BaseModel, Field, model_validator
from utils import check_uniqueness_id


class ObjectsIDs(BaseModel):
    total: int
    objectIDs: list[int] = Field(validator='validate_objectIDs')

    @model_validator(mode='after')
    def validate_objectIDs(self):
        check_uniqueness_id(self.objectIDs)
        return self
