"""
game_metadata.py: File, containing metadata for a twich game.
"""


from common.utils import ReadOnlyClassProperty


class TwichGameMetadata:
    """
    TwichGameMetadata: Class, containing metadata for twich game.
    """

    parse_game_summary: str = 'Produce message to kafka to parse twich game.'
    parse_game_description: str = 'Produce message to kafka to parse twich game.'
    parse_game_response_description: str = 'Message has been produced to kafka.'

    private_parse_game_summary: str = 'Parse game of the twich platform.'
    private_parse_game_description: str = 'Parse game of the twich platform.'
    private_parse_game_response_description: str = 'Twich game has been parsed.'

    delete_game_by_name_summary: str = 'Delete twich game by name.'
    delete_game_by_name_description: str = 'Delete twich game by name.'
    delete_game_by_name_response_description: str = 'Twich game has been deleted.'

    get_all_games_summary: str = 'Return all twich games.'
    get_all_games_description: str = 'Return all twich games.'
    get_all_games_response_description: str = 'All twich games have been returned.'

    get_game_by_name_summary: str = 'Return twich game by name.'
    get_game_by_name_description: str = 'Return twich game by name.'
    get_game_by_name_response_description: str = 'Twich game has been returned.'

    @ReadOnlyClassProperty
    def parse_game(cls) -> dict:
        """
        parse_game: Return parse game metadata.

        Returns:
            dict: Parse game metadata.
        """

        return {
            'summary': cls.parse_game_summary,
            'description': cls.parse_game_description,
            'response_description': cls.parse_game_response_description,
        }

    @ReadOnlyClassProperty
    def private_parse_game(cls) -> dict:
        """
        private_parse_game: Return private parse game metadata.

        Returns:
            dict: Private parse game metadata.
        """

        return {
            'summary': cls.private_parse_game_summary,
            'description': cls.private_parse_game_description,
            'response_description': cls.private_parse_game_response_description,
        }

    @ReadOnlyClassProperty
    def delete_game_by_name(cls) -> dict:
        """
        delete_game_by_name: Return delete game metadata.

        Returns:
            dict: Delete game metadata.
        """

        return {
            'summary': cls.delete_game_by_name_summary,
            'description': cls.delete_game_by_name_description,
            'response_description': cls.delete_game_by_name_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_games(cls) -> dict:
        """
        get_all_games: Return all games metadata.

        Returns:
            dict: Get all games metadata.
        """

        return {
            'summary': cls.get_all_games_summary,
            'description': cls.get_all_games_description,
            'response_description': cls.get_all_games_response_description,
        }

    @ReadOnlyClassProperty
    def get_game_by_name(cls) -> dict:
        """
        get_game_by_name: Return game by name metadata.

        Returns:
            dict: Get game by name metadata.
        """

        return {
            'summary': cls.get_game_by_name_summary,
            'description': cls.get_game_by_name_description,
            'response_description': cls.get_game_by_name_response_description,
        }
