from api_architecture.schemas.user import UserCreate, UserGet, UserSex
import pytest
from datetime import datetime
class TestUserCreate:
    def test_required_fields_success(self):
        user = UserCreate(email="test@example.com", first_name="John", last_name="Doe")
        assert user.email == "test@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.sex is None
        assert user.orders == []

    def test_optional_field_success(self):
        user = UserCreate(email="test@example.com", first_name="John", last_name="Doe", sex=UserSex.Male, orders=["order1", "order2"])
        assert user.email == "test@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.sex == UserSex.Male
        assert user.orders == ["order1", "order2"]

    def test_empty_email_validation_error(self):
        with pytest.raises(ValueError):
            user = UserCreate(email="", first_name="John", last_name="Doe")
    
    def test_empty_first_name_validation_error(self):
        with pytest.raises(ValueError):
            user = UserCreate(email="test@example.com", first_name="", last_name="Doe")

    def test_empty_last_name_validation_error(self):
        with pytest.raises(ValueError):
            user = UserCreate(email="test@example.com", first_name="John", last_name="")

    def test_sex_error(self):
        with pytest.raises(ValueError):
            user = UserCreate(email="test@example.com", first_name="John", last_name="", sex='fwf')

class TestUserGet:
    def test_create_user_with_required_fields_and_valid_data(self):
        user = UserGet(
            id="123",
            email="test@example.com",
            first_name="John",
            last_name="Doe",
            sex=UserSex.Male,
            created_time=datetime.now()
        )
        assert user.id == "123"
        assert user.email == "test@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.sex == UserSex.Male
        assert user.orders == []
        assert isinstance(user.created_time, datetime)
        assert isinstance(user.last_login, datetime)

    def test_create_user_with_all_fields_and_valid_data(self):
        user = UserGet(
            id="123",
            email="test@example.com",
            first_name="John",
            last_name="Doe",
            sex=UserSex.Male,
            orders=["order1", "order2"],
            created_time=datetime.now(),
            last_login=datetime.now()
        )
        assert user.id == "123"
        assert user.email == "test@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.sex == UserSex.Male
        assert user.orders == ["order1", "order2"]
        assert isinstance(user.created_time, datetime)
        assert isinstance(user.last_login, datetime)

    def test_create_user_with_sex_not_provided(self):
        user = UserGet(
            id="123",
            email="test@example.com",
            first_name="John",
            last_name="Doe",
            created_time=datetime.now()
        )
        assert user.id == "123"
        assert user.email == "test@example.com"
        assert user.first_name == "John"
        assert user.last_name == "Doe"
        assert user.sex is None
        assert user.orders == []
        assert isinstance(user.created_time, datetime)
        assert isinstance(user.last_login, datetime)
