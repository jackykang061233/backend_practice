from api_architecture.db.mysql.mysql_user import create_mysql_user
from sqlalchemy import text
import pytest


class TestMysqlUser:

    def test_create_mysql_user_valid_parameters(self, mocker):
        # Arrange
        username = "test_user"
        password = "test_password"
        database_name = "test_database"

        mock_session = mocker.Mock()
        mocker.patch("api_architecture.db.mysql.mysql_user.session", mock_session)

        # Act
        create_mysql_user(username, password, database_name)
        # Assert
        mock_session.execute.assert_called_with(text(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';"))
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once()

    def test_create_mysql_user_empty_username(self):
        # Arrange
        username = ""
        password = "test_password"
        database_name = "test_database"

        # Act/Assert
        with pytest.raises(ValueError, match="Username, password, and database_name cannot be empty strings."):
            create_mysql_user(username, password, database_name)

    def test_create_mysql_user_empty_password(self):
        # Arrange
        username = "test_user"
        password = ""
        database_name = "test_database"

        # Act/Assert
        with pytest.raises(ValueError, match="Username, password, and database_name cannot be empty strings."):
            create_mysql_user(username, password, database_name)

    def test_create_mysql_user_empty_database_name(self):
        # Arrange
        username = "test_user"
        password = "test_password"
        database_name = ""

        # Act/Assert
        with pytest.raises(ValueError, match="Username, password, and database_name cannot be empty strings."):
            create_mysql_user(username, password, database_name)