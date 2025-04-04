from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "PlayStation 5 Pro"


def test_schemas_return_raise():
    data = {"name": "PlayStation 5 Pro", "quantity": 10, "price": 5.858, "status": True}

    with pytest.raises[ValidationError] as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "PlayStation 5 Pro", "quantity": 10, "price": 5.858},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }
