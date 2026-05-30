from pydantic import BaseModel


class ProductCreate(BaseModel):

    name: str

    slug: str

    description: str

    price: float

    stock: int

    category_id: int


class ProductResponse(BaseModel):

    id: int

    name: str

    price: float

    stock: int

    image_url: str | None = None

    class Config:
        from_attributes = True