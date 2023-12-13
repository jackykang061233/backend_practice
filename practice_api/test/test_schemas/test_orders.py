import pytest
from datetime import datetime
from api_architecture.schemas.orders import OrderCreate, OrderGet, OrderStatus

class TestOrderCreate:
    def test_create_order_with_required_fields(self):
        order = OrderCreate(user_id=123, product_name="Product", order_status=OrderStatus.Accepted)
        assert order.user_id == 123
        assert order.product_name == "Product"
        assert order.quantity == 0
        assert order.total_price == 0.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

        # Creating an order with optional order_notes field
    def test_create_order_with_optional_order_notes(self):
        order = OrderCreate(user_id=123, product_name="Product", order_status=OrderStatus.Accepted, order_notes="Some notes")
        assert order.user_id == 123
        assert order.product_name == "Product"
        assert order.quantity == 0
        assert order.total_price == 0.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes == "Some notes"

        # Creating an order with default values for quantity and total_price
    def test_create_order_with_default_values(self):
        order = OrderCreate(user_id=123, product_name="Product", order_status=OrderStatus.Accepted)
        assert order.user_id == 123
        assert order.product_name == "Product"
        assert order.quantity == 0
        assert order.total_price == 0.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None
    
        # Creating an order with an empty user_id field
    def test_create_order_with_empty_user_id(self):
        with pytest.raises(ValueError):
            OrderCreate(user_id=None, product_name="Product", order_status=OrderStatus.Accepted)

        # Creating an order with an empty product_name field
    def test_create_order_with_empty_product_name(self):
        with pytest.raises(ValueError):
            OrderCreate(user_id=123, product_name="", order_status=OrderStatus.Accepted)

        # Creating an order with a negative quantity value
    def test_create_order_with_negative_quantity(self):
        with pytest.raises(ValueError):
            OrderCreate(user_id=123, product_name="Product", quantity=-1, order_status=OrderStatus.Accepted)

    def test_create_order_with_negative_price(self):
        with pytest.raises(ValueError):
            OrderCreate(user_id=123, product_name="Product", total_price=-1, order_status=OrderStatus.Accepted)

class TestOrderGet:
    def test_valid_input_values(self):
        order = OrderGet(
            id=123,
            user_id=456,
            product_name="Product",
            quantity=10,
            total_price=100.0,
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes=None
        )
        assert order.id == 123
        assert order.user_id == 456
        assert order.product_name == "Product"
        assert order.quantity == 10
        assert order.total_price == 100.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

    def test_optional_fields_none(self):
        order = OrderGet(
            id=123,
            user_id=456,
            product_name="Product",
            quantity=10,
            total_price=100.0,
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes=None
        )
        assert order.id == 123
        assert order.user_id == 456
        assert order.product_name == "Product"
        assert order.quantity == 10
        assert order.total_price == 100.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

    def test_quantity_price_default(self):
        order = OrderGet(
            id=123,
            user_id=456,
            product_name="Product",
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes=None
        )
        assert order.id == 123
        assert order.user_id == 456
        assert order.product_name == "Product"
        assert order.quantity == 0
        assert order.total_price == 0.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes is None

    def test_order_notes_length_100(self):
        order = OrderGet(
            id=123,
            user_id=456,
            product_name="Product",
            quantity=10,
            total_price=100.0,
            order_date=datetime.now(),
            order_status=OrderStatus.Accepted,
            order_notes="Awesome"
        )
        assert order.id == 123
        assert order.user_id == 456
        assert order.product_name == "Product"
        assert order.quantity == 10
        assert order.total_price == 100.0
        assert isinstance(order.order_date, datetime)
        assert order.order_status == OrderStatus.Accepted
        assert order.order_notes == "Awesome"

    def test_empty_id(self):
        with pytest.raises(ValueError):
            OrderGet(
                id=None,
                user_id=456,
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
                id=123,
                user_id=None,
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
                id=123,
                user_id=456,
                product_name="",
                quantity=10,
                total_price=100.0,
                order_date=datetime.now(),
                order_status=OrderStatus.Accepted,
                order_notes=None
            )

    def test_get_order_with_negative_quantity(self):
        with pytest.raises(ValueError):
            OrderGet(
                id=123,
                user_id=456,
                product_name="",
                quantity=-1,
                total_price=100.0,
                order_date=datetime.now(),
                order_status=OrderStatus.Accepted,
                order_notes=None
            )

    def test_get_order_with_negative_price(self):
        with pytest.raises(ValueError):
            OrderGet(
                id=123,
                user_id=456,
                product_name="",
                quantity=10,
                total_price=-1,
                order_date=datetime.now(),
                order_status=OrderStatus.Accepted,
                order_notes=None
            )
