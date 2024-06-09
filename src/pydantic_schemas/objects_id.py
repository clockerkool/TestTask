from pydantic import BaseModel, Field, field_validator


class ObjectsID(BaseModel):
    total: int
    objectIDs: list[int] = Field(validator='validate_objectIDs')

    @field_validator('objectIDs')
    def validate_objectIDs(cls, value):
        for obj_id in value:
            if not isinstance(obj_id, int):
                raise ValueError("Все значения в objectIDs должны быть целыми числами")
        return value
