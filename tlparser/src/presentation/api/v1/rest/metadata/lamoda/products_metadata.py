"""
products_metadata.py: File, containing metadata for a lamoda products.
"""


from common.utils.decorators import ReadOnlyClassProperty


class LamodaProductsMetadata:
    """
    LamodaProductsMetadata: Class, containing metadata for lamoda products.
    """

    parse_products_summary: str = 'Produce message to kafka to parse lamoda products.'
    parse_products_description: str = 'Produce message to kafka to parse lamoda products.'
    parse_products_response_description: str = 'Message has been produced to kafka.'

    private_parse_products_summary: str = 'Parse products by category id.'
    private_parse_products_description: str = 'Parse products of the lamoda platform by categories.'
    private_parse_products_response_description: str = 'Lamoda products have been parsed.'

    delete_products_by_category_summary: str = 'Delete products by category.'
    delete_products_by_category_description: str = 'Delete products by category. Category - field.'
    delete_products_by_category_response_description: str = 'Products have been deleted.'

    get_all_products_summary: str = 'Return all products.'
    get_all_products_description: str = 'Return all products.'
    get_all_products_response_description: str = 'All products have been returned.'

    get_products_by_category_summary: str = 'Return products by category.'
    get_products_by_category_description: str = 'Return products by category.'
    get_products_by_category_response_description: str = 'Products have been returned.'

    @ReadOnlyClassProperty
    def parse_products(cls) -> dict:
        """
        parse_products: Return parse products metadata.

        Returns:
            dict: Parse products metadata.
        """

        return {
            'summary': cls.parse_products_summary,
            'description': cls.parse_products_description,
            'response_description': cls.parse_products_response_description,
        }

    @ReadOnlyClassProperty
    def private_parse_products(cls) -> dict:
        """
        private_parse_products: Return private parse products metadata.

        Returns:
            dict: Private parse products metadata.
        """

        return {
            'summary': cls.private_parse_products_summary,
            'description': cls.private_parse_products_description,
            'response_description': cls.private_parse_products_response_description,
        }

    @ReadOnlyClassProperty
    def delete_products_by_category(cls) -> dict:
        """
        delete_products_by_category: Delete products metadata.

        Returns:
            dict: Delete products metadata.
        """

        return {
            'summary': cls.delete_products_by_category_summary,
            'description': cls.delete_products_by_category_description,
            'response_description': cls.delete_products_by_category_response_description,
        }

    @ReadOnlyClassProperty
    def get_all_products(cls) -> dict:
        """
        get_all_products: Return get all products metadata.

        Returns:
            dict: Get all products metadata.
        """

        return {
            'summary': cls.get_all_products_summary,
            'description': cls.get_all_products_description,
            'response_description': cls.get_all_products_response_description,
        }

    @ReadOnlyClassProperty
    def get_products_by_category(cls) -> dict:
        """
        get_products_by_category: Return get products by category metadata.

        Returns:
            dict: Get products by category metadata.
        """

        return {
            'summary': cls.get_products_by_category_summary,
            'description': cls.get_products_by_category_description,
            'response_description': cls.get_products_by_category_response_description,
        }
