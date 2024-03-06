"""
stream_metadata.py: File, containing metadata for a twich stream.
"""


from common.utils import ReadOnlyClassProperty


class TwichStreamMetadata:
    """
    TwichStreamMetadata: Class, containing twich stream metadata.
    """

    parse_stream_summary: str = 'Produce message to kafka to parse twich stream.'
    parse_stream_description: str = 'Produce message to kafka to parse twich stream.'
    parse_stream_response_description: str = 'Produce message to kafka to parse twich stream.'

    private_parse_stream_summary: str = 'Parse stream of the twich platform.'
    private_parse_stream_description: str = 'Parse stream of the twich platform.'
    private_parse_stream_response_description: str = 'Twich stream has been parsed.'

    delete_stream_by_user_login_summary: str = 'Delete twich stream.'
    delete_stream_by_user_login_description: str = 'Delete twich stream.'
    delete_stream_by_user_login_response_description: str = 'Twich stream has been deleted.'

    get_all_streams_summary: str = 'Return all twich streams.'
    get_all_streams_description: str = 'Return all twich streams.'
    get_all_streams_response_description: str = 'All twich streams have been returned.'

    get_stream_by_user_login_summary: str = 'Return twich stream by user login.'
    get_stream_by_user_login_description: str = 'Return twich stream by user login.'
    get_stream_by_user_login_response_description: str = 'Twich stream has been returned.'

    @ReadOnlyClassProperty
    def parse_stream(cls) -> dict:
        """
        parse_stream: Return private parse stream metadata.

        Returns:
            dict: Parse stream metadata.
        """

        return {
            'summary': cls.parse_stream_summary,
            'description': cls.parse_stream_description,
            'response_description': cls.parse_stream_response_description,
        }

    @ReadOnlyClassProperty
    def private_parse_stream(cls) -> dict:
        """
        private_parse_stream: Return private parse stream metadata.

        Returns:
            dict: Private parse stream metadata.
        """

        return {
            'summary': cls.private_parse_stream_summary,
            'description': cls.private_parse_stream_description,
            'response_description': cls.private_parse_stream_response_description,
        }

    @ReadOnlyClassProperty
    def delete_stream_by_user_login(cls) -> dict:
        """
        delete_stream_by_user_login: Return delete stream metadata.

        Returns:
            dict: Delete stream metadata.
        """

        return {
            'summary': cls.delete_stream_by_user_login_summary,
            'description': cls.delete_stream_by_user_login_description,
            'response_description': cls.delete_stream_by_user_login_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_streams(cls) -> dict:
        """
        get_all_streams: Return get all streams metadata.

        Returns:
            dict: Get all streams metadata.
        """

        return {
            'summary': cls.get_all_streams_summary,
            'description': cls.get_all_streams_description,
            'response_description': cls.get_all_streams_response_description,
        }

    @ReadOnlyClassProperty
    def get_stream_by_user_login(cls) -> dict:
        """
        get_stream_by_user_login: Return get stream by user login metadata.

        Returns:
            dict: Get stream by user login metadata.
        """

        return {
            'summary': cls.get_stream_by_user_login_summary,
            'description': cls.get_stream_by_user_login_description,
            'response_description': cls.get_stream_by_user_login_response_description,
        }
