from pydantic import BaseModel

class ToDoRequest(BaseModel):
    name: str
    completed: bool

class ToDoResponse(BaseModel):
    id: int
    name: str
    completed: bool

    class Config:
        from_attributes = True  # para Pydantic v2

    @classmethod
    def from_orm(cls, obj):
        """Compatibility wrapper for Pydantic v1 style usage."""
        return cls.model_validate(obj)
