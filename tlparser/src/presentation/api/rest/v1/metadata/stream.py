"""
stream.py: File, containing twich stream metadata.
"""


from typing import ClassVar
from shared.utils import ReadOnlyClassProperty


class TwichStreamMetadata:
    parse_stream_summary: ClassVar[str] = 'Parse stream of the twich platform.'
    parse_stream_description: ClassVar[str] = 'Parse stream of the twich platform.'
    parse_stream_response_description: ClassVar[str] = 'Twich stream has been parsed.'

    delete_stream_summary: ClassVar[str] = 'Delete twich stream.'
    delete_stream_description: ClassVar[str] = 'Delete twich stream.'
    delete_stream_response_description: ClassVar[str] = 'Twich stream has been deleted.'

    get_stream_by_user_login_summary: ClassVar[str] = 'Return twich stream by user login.'
    get_stream_by_user_login_description: ClassVar[str] = 'Return twich stream by user login.'
    get_stream_by_user_login_response_description: ClassVar[str] = 'Twich stream has been returned.'

    get_all_streams_summary: ClassVar[str] = 'Return all twich streams.'
    get_all_streams_description: ClassVar[str] = 'Return all twich streams.'
    get_all_streams_response_description: ClassVar[str] = 'All twich streams have been returned.'

    @ReadOnlyClassProperty
    def parse_stream(cls) -> dict:
        return {
            'summary': cls.parse_stream_summary,
            'description': cls.parse_stream_description,
            'response_description': cls.parse_stream_response_description,
        }

    @ReadOnlyClassProperty
    def delete_stream(cls) -> dict:
        return {
            'summary': cls.delete_stream_summary,
            'description': cls.delete_stream_description,
            'response_description': cls.delete_stream_response_description,
        }

    @ReadOnlyClassProperty
    def get_stream_by_user_login(cls) -> dict:
        return {
            'summary': cls.get_stream_by_user_login_summary,
            'description': cls.get_stream_by_user_login_description,
            'response_description': cls.get_stream_by_user_login_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_streams(cls) -> dict:
        return {
            'summary': cls.get_all_streams_summary,
            'description': cls.get_all_streams_description,
            'response_description': cls.get_all_streams_response_description,
        }
