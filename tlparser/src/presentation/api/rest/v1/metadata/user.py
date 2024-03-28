"""
user.py: File, containing twich user metadata.
"""


from typing import ClassVar
from shared.utils import ReadOnlyClassProperty


class TwichUserMetadata:
    parse_user_summary: ClassVar[str] = 'Parse user of the twich platform.'
    parse_user_description: ClassVar[str] = 'Parse user of the twich platform.'
    parse_user_response_description: ClassVar[str] = 'Twich game has been parsed.'

    delete_user_summary: ClassVar[str] = 'Delete twich user.'
    delete_user_description: ClassVar[str] = 'Delete twich user.'
    delete_user_response_description: ClassVar[str] = 'Twich user has been deleted.'

    get_user_by_login_summary: ClassVar[str] = 'Return user by login.'
    get_user_by_login_description: ClassVar[str] = 'Return user by login.'
    get_user_by_login_response_description: ClassVar[str] = 'Twich user has been returned.'

    get_all_users_summary: ClassVar[str] = 'Return all twich users.'
    get_all_users_description: ClassVar[str] = 'Return all twich users.'
    get_all_users_response_description: ClassVar[str] = 'All twich users have beed returned.'

    @ReadOnlyClassProperty
    def parse_user(cls) -> dict:
        return {
            'summary': cls.parse_user_summary,
            'description': cls.parse_user_description,
            'response_description': cls.parse_user_response_description,
        }

    @ReadOnlyClassProperty
    def delete_user(cls) -> dict:
        return {
            'summary': cls.delete_user_summary,
            'description': cls.delete_user_description,
            'response_description': cls.delete_user_response_description,
        }

    @ReadOnlyClassProperty
    def get_user_by_login(cls) -> dict:
        return {
            'summary': cls.get_user_by_login_summary,
            'description': cls.get_user_by_login_description,
            'response_description': cls.get_user_by_login_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_users(cls) -> dict:
        return {
            'summary': cls.get_all_users_summary,
            'description': cls.get_all_users_description,
            'response_description': cls.get_all_users_response_description,
        }
