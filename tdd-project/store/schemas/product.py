from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field
from store.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., descriptions="Product Name")
    quantity: int = Field(..., descriptions="Product Quantity")
    price: Decimal = Field(..., descriptions="Product Price")
    status: bool = Field(..., descriptions="Product Status")


class ProductIn(ProductBase, BaseSchemaMixin): ...


class ProductOut(ProductIn, OutMixin): ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, descriptions="Product Quantity")
    price: Optional[Decimal_] = Field(None, descriptions="Product Price")
    status: Optional[bool] = Field(None, descriptions="Product Status")


class ProductUpdateOut(ProductOut): ...
