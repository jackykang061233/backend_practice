import pytest
from datetime import datetime
from api_architecture.schemas.items import ItemCreate, ItemGet

class TestItemCreate:
    def test_valid_name_and_price(self):
        item = ItemCreate(name="item", price=10.0)
        assert item.name == "item"
        assert item.price == 10.0
    def test_valid_name_no_price(self):
        item = ItemCreate(name="item")
        assert item.name == "item"
        assert item.price == 0.0
    def test_valid_name_empty_description(self):
        item = ItemCreate(name="item", description="")
        assert item.name == "item"
        assert item.description == ""

    def test_created_time(self):
        item = ItemCreate(name="item", price=10.0, created_time=datetime.now())
        assert item.name == "item"
        assert item.price == 10.0
        assert item.created_time is not None

    def test_last_update(self):
        item = ItemCreate(name="item", price=10.0, created_time=datetime.now(), last_update=datetime.now())
        assert item.name == "item"
        assert item.price == 10.0
        assert item.created_time is not None
        assert item.last_update is not None
    def test_empty_name(self):
        with pytest.raises(ValueError):
            item = ItemCreate(name="")
    def test_negative_price(self):
        with pytest.raises(ValueError):
            item = ItemCreate(name="item", price=-10.0)
    def test_long_description(self):
        with pytest.raises(ValueError):
            item = ItemCreate(name="item", description="a" * 301)

    def test_wrong_createed_time_format(self):
        with pytest.raises(ValueError):
            item = ItemCreate(name="item", price=10.0, created_time='')
    def test_wrong_last_update_format(self):
        with pytest.raises(ValueError):
            item = ItemCreate(name="item", price=10.0, last_update='')
    
class TestItemGet:
    def test_valid_id_name_created_time(self):
        item = ItemGet(id=1, name="item", created_time=datetime.now())
        assert item.id == 1
        assert item.name == "item"
        assert item.created_time is not None

    def test_default_orders(self):
        item = ItemGet(id=1, name="item", created_time=datetime.now())
        assert item.orders == []

    def test_valid_all_fields(self):
        item = ItemGet(id=1, name="item", price=10.0, description="description", orders=[1, 2], created_time=datetime.now(), last_update=datetime.now())
        assert item.id == 1
        assert item.name == "item"
        assert item.price == 10.0
        assert item.description == "description"
        assert item.orders == [1, 2]
        assert item.created_time is not None
        assert item.last_update is not None

    def test_update_last_update(self):
        item = ItemGet(id=1, name="item", created_time=datetime.now())
        last_update_before = item.last_update
        item.last_update = datetime.now()
        assert item.last_update != last_update_before

    def test_empty_id_validation_error(self):
        with pytest.raises(ValueError):
            ItemGet(id=None, name="item", created_time=datetime.now())

    def test_negative_price_validation_error(self):
        with pytest.raises(ValueError):
            ItemGet(id=1, name="item", price=-10.0, created_time=datetime.now())
