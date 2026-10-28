from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    price: float = Field(ge=0)
    description: str = Field(min_length=1)
    stock: int = Field(ge=0)


class ProductUpdate(ProductCreate):
    """Fields for replacing an existing product."""


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str
    stock: int

    model_config = ConfigDict(from_attributes=True)
