from typing import Type

class IUserService:
    def create_user(self, user_data: dict):
        raise NotImplementedError

    def get_user_by_id(self, user_id: int):
        raise NotImplementedError

    def get_all_users(self):
        raise NotImplementedError

    def update_user(self, user_id: int, user_data: dict):
        raise NotImplementedError

    def delete_user(self, user_id: int):
        raise NotImplementedError


class ServiceMeta:
    def get_user_service(self) -> Type[IUserService]:
        raise NotImplementedError