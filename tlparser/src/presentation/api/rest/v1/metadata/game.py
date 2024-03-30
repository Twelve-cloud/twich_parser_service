"""
game.py: File, containing twich game metadata.
"""


from typing import ClassVar

from shared.utils import ReadOnlyClassProperty


class TwichGameMetadata:
    parse_game_summary: ClassVar[str] = 'Parse game of the twich platform.'
    parse_game_description: ClassVar[str] = 'Parse game of the twich platform.'
    parse_game_response_description: ClassVar[str] = 'Game has been parsed.'

    delete_game_summary: ClassVar[str] = 'Delete twich game by id.'
    delete_game_description: ClassVar[str] = 'Delete twich game by id.'
    delete_game_response_description: ClassVar[str] = 'Game has been deleted.'

    delete_game_by_name_summary: ClassVar[str] = 'Delete twich game by name.'
    delete_game_by_name_description: ClassVar[str] = 'Delete twich game by name.'
    delete_game_by_name_response_description: ClassVar[str] = 'Game has been deleted.'

    get_game_summary: ClassVar[str] = 'Return twich game by id.'
    get_game_description: ClassVar[str] = 'Return twich game by id.'
    get_game_response_description: ClassVar[str] = 'Game has been returned.'

    get_game_by_name_summary: ClassVar[str] = 'Return twich game by name.'
    get_game_by_name_description: ClassVar[str] = 'Return twich game by name.'
    get_game_by_name_response_description: ClassVar[str] = 'Game has been returned.'

    get_all_games_summary: ClassVar[str] = 'Return all twich games.'
    get_all_games_description: ClassVar[str] = 'Return all twich games.'
    get_all_games_response_description: ClassVar[str] = 'All games have been returned.'

    @ReadOnlyClassProperty
    def parse_game(cls) -> dict:
        return {
            'summary': cls.parse_game_summary,
            'description': cls.parse_game_description,
            'response_description': cls.parse_game_response_description,
        }

    @ReadOnlyClassProperty
    def delete_game(cls) -> dict:
        return {
            'summary': cls.delete_game_summary,
            'description': cls.delete_game_description,
            'response_description': cls.delete_game_response_description,
        }

    @ReadOnlyClassProperty
    def delete_game_by_name(cls) -> dict:
        return {
            'summary': cls.delete_game_by_name_summary,
            'description': cls.delete_game_by_name_description,
            'response_description': cls.delete_game_by_name_response_description,
        }

    @ReadOnlyClassProperty
    def get_game(cls) -> dict:
        return {
            'summary': cls.get_game_summary,
            'description': cls.get_game_description,
            'response_description': cls.get_game_response_description,
        }

    @ReadOnlyClassProperty
    def get_game_by_name(cls) -> dict:
        return {
            'summary': cls.get_game_by_name_summary,
            'description': cls.get_game_by_name_description,
            'response_description': cls.get_game_by_name_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_games(cls) -> dict:
        return {
            'summary': cls.get_all_games_summary,
            'description': cls.get_all_games_description,
            'response_description': cls.get_all_games_response_description,
        }
