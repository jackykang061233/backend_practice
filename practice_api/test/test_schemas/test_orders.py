import pytest
from datetime import datetime
from api_architecture.schemas.orders import OrderCreate, OrderGet, OrderStatus

class TestOrderGet:
    def test_valid_input_values(self):
        order = OrderGet(
            id="123",
            user_id="456",
            product_name="Product",
            quantity=10,
            total_price=100.0,
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes=None
        )
        assert order.id == "123"
        assert order.user_id == "456"
        assert order.product_name == "Product"
        assert order.quantity == 10
        assert order.total_price == 100.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

    def test_optional_fields_none(self):
        order = OrderGet(
            id="123",
            user_id="456",
            product_name="Product",
            quantity=10,
            total_price=100.0,
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes=None
        )
        assert order.id == "123"
        assert order.user_id == "456"
        assert order.product_name == "Product"
        assert order.quantity == 10
        assert order.total_price == 100.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

    def test_quantity_price_default(self):
        order = OrderGet(
            id="123",
            user_id="456",
            product_name="Product",
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes=None
        )
        assert order.id == "123"
        assert order.user_id == "456"
        assert order.product_name == "Product"
        assert order.quantity == 0
        assert order.total_price == 0.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

    def test_order_notes_length_100(self):
        order = OrderGet(
            id="123",
            user_id="456",
            product_name="Product",
            quantity=10,
            total_price=100.0,
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes="Awesome"
        )
        assert order.id == "123"
        assert order.user_id == "456"
        assert order.product_name == "Product"
        assert order.quantity == 10
        assert order.total_price == 100.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes == "Awesome"

    def test_empty_id(self):
        with pytest.raises(ValueError):
            OrderGet(
                id="",
                user_id="456",
                product_name="Product",
                quantity=10,
                total_price=100.0,
                order_date=datetime.now(),
                order_status=OrderStatus.Accepted,
                order_notes=None
            )

    def test_empty_user_id(self):
        with pytest.raises(ValueError):
            OrderGet(
                id="123",
                user_id="",
                product_name="Product",
                quantity=10,
                total_price=100.0,
                order_date=datetime.now(),
                order_status=OrderStatus.Accepted,
                order_notes=None
            )
    def test_empty_product_name(self):
        with pytest.raises(ValueError):
            OrderGet(
                id="123",
                user_id="456",
                product_name="",
                quantity=10,
                total_price=100.0,
                order_date=datetime.now(),
                order_status=OrderStatus.Accepted,
                order_notes=None
            )
