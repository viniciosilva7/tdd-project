from typing import List
from uuid import UUID
import pytest
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecasses.product import product_usecase
from store.core.exceptions import NotFoundException


async def test_usecase_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "PlayStation 5 Pro"


async def test_usecase_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "PlayStation 5 Pro"


async def test_usecase_get_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecase_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecase_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecase_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecase_delete_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with delete: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
