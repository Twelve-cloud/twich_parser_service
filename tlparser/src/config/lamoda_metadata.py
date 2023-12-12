"""
lamoda_metadata.py: File, containing metadata for a lamoda app.
"""

parse_products_endpoint_summary: str = 'Parse products of the lamoda platform by category.'

parse_products_endpoint_description: str = '''
Parse products of the lamoda platform by categories. Every exception is handled by twich controller.
It uses beautifulsoup library for parsing.
'''

parse_products_endpoint_response_description: str = 'Lamoda products have been parsed.'

parse_products_metadata: dict = {
    'summary': parse_products_endpoint_summary,
    'description': parse_products_endpoint_description,
    'response_description': parse_products_endpoint_response_description,
}
