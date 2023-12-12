"""
twich_metadata.py: File, containing metadata for a twich app.
"""

parse_user_endpoint_summary: str = 'Parse user of the twich platform.'

parse_user_endpoint_description: str = '''
Parse user of the twich platform. Every exception is handled by twich controller.
It uses request library for parsing.
'''

parse_user_endpoint_response_description: str = 'Twich game has been parsed.'

parse_game_endpoint_summary: str = 'Parse game of the twich platform.'

parse_game_endpoint_description: str = '''
Parse game of the twich platform. Every exception is handled by twich controller.
It uses request library for parsing.
'''

parse_game_endpoint_response_description: str = 'Twich game has been parsed.'

parse_stream_endpoint_summary: str = 'Parse stream of the twich platform.'

parse_stream_endpoint_description: str = '''
Parse stream of the twich platform. Every exception is handled by twich controller.
It uses request library for parsing.
'''

parse_stream_endpoint_response_description: str = 'Twich stream has been parsed.'

parse_user_metadata: dict = {
    'summary': parse_user_endpoint_summary,
    'description': parse_user_endpoint_description,
    'response_description': parse_user_endpoint_response_description,
}


parse_game_metadata: dict = {
    'summary': parse_game_endpoint_summary,
    'description': parse_game_endpoint_description,
    'response_description': parse_game_endpoint_response_description,
}

parse_stream_metadata: dict = {
    'summary': parse_stream_endpoint_summary,
    'description': parse_stream_endpoint_description,
    'response_description': parse_stream_endpoint_response_description,
}
