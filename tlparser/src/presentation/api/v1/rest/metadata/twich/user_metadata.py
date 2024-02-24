"""
user_metadata.py: File, containing metadata for a twich user.
"""


from common.utils.decorators import ReadOnlyClassProperty


class TwichUserMetadata:
    """
    TwichUserMetadata: Class, containing metadata for twich user.
    """

    parse_user_summary: str = 'Produce message to kafka to parse twich user.'
    parse_user_description: str = 'Produce message to kafka to parse twich user.'
    parse_user_response_description: str = 'Message has been produced to kafka.'

    private_parse_user_summary: str = 'Parse user of the twich platform.'
    private_parse_user_description: str = 'Parse user of the twich platform.'
    private_parse_user_response_description: str = 'Twich game has been parsed.'

    delete_user_by_login_summary: str = 'Delete twich user.'
    delete_user_by_login_description: str = 'Delete twich user.'
    delete_user_by_login_response_description: str = 'Twich user has been deleted.'

    get_all_users_summary: str = 'Return all twich users.'
    get_all_users_description: str = 'Return all twich users.'
    get_all_users_response_description: str = 'All twich users have beed returned.'

    get_user_by_login_summary: str = 'Return user by login.'
    get_user_by_login_description: str = 'Return user by login.'
    get_user_by_login_response_description: str = 'Twich user has been returned.'

    @ReadOnlyClassProperty
    def parse_user(cls) -> dict:
        """
        parse_user: Return parse user metadata.

        Returns:
            dict: Parse user metadata.
        """

        return {
            'summary': cls.parse_user_summary,
            'description': cls.parse_user_description,
            'response_description': cls.parse_user_response_description,
        }

    @ReadOnlyClassProperty
    def private_parse_user(cls) -> dict:
        """
        private_parse_user: Return private parse user metadata.

        Returns:
            dict: Private parse user metadata.
        """

        return {
            'summary': cls.private_parse_user_summary,
            'description': cls.private_parse_user_description,
            'response_description': cls.private_parse_user_response_description,
        }

    @ReadOnlyClassProperty
    def delete_user_by_login(cls) -> dict:
        """
        delete_user_by_login: Return delete user metadata.

        Returns:
            dict: Delete user metadata.
        """

        return {
            'summary': cls.delete_user_by_login_summary,
            'description': cls.delete_user_by_login_description,
            'response_description': cls.delete_user_by_login_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_users(cls) -> dict:
        """
        get_all_users: Return get all users metadata.

        Returns:
            dict: Get all users metadata.
        """

        return {
            'summary': cls.get_all_users_summary,
            'description': cls.get_all_users_description,
            'response_description': cls.get_all_users_response_description,
        }

    @ReadOnlyClassProperty
    def get_user_by_login(cls) -> dict:
        """
        get_user_by_login: Return get user by login metadata.

        Returns:
            dict: Get user by login metadata.
        """

        return {
            'summary': cls.get_user_by_login_summary,
            'description': cls.get_user_by_login_description,
            'response_description': cls.get_user_by_login_response_description,
        }
