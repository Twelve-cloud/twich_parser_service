"""
metadata.py: File, containing metadata for a project and routes.
"""

project_summary: str = 'Parsing Twich games, users and streams and Lamoda products by category'

project_description: str = '''
This applications stands for parsing Twich and Lamoda.
Twich can be parsed by games, streams and users. Lamoda can be parsed by categories.
There are 2 types of endpoints. Firstly there are endpoints that are called by user.
They do nothing except for producing message for kafka.
Then there are endpoinds for that are called by kafka. They really do parsing.
They are called when kafka consumer get a message. Kafka called them directly.
'''

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

parse_products_endpoint_summary: str = 'Parse products of the lamoda platform by category.'

parse_products_endpoint_description: str = '''
Parse products of the lamoda platform by categories. Every exception is handled by twich controller.
It uses beautifulsoup library for parsing.
'''

parse_products_endpoint_response_description: str = 'Lamoda products have been parsed.'

project_metadata: dict = {
    'summary': project_summary,
    'description': project_description,
}

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

parse_products_metadata: dict = {
    'summary': parse_products_endpoint_summary,
    'description': parse_products_endpoint_description,
    'response_description': parse_products_endpoint_response_description,
}
