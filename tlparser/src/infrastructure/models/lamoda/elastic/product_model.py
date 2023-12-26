"""
product_model: File, containing lamoda product model for elastic search.
"""


from elasticsearch_dsl import Date, Document, Float, Text


class LamodaProduct(Document):
    """
    LamodaProduct: Class, that represents lamoda product document in elasticsearch database.

    Args:
        Document (_type_): Base superclass for LamodaProduct class.
    """

    sku: Text = Text()
    url: Text = Text()
    category: Text = Text()
    description: Text = Text()
    price: Float = Float()
    price_currency: Text = Text()
    price_valid_until: Date = Date(default_timezone='UTC')
    parsed_at: Date = Date(default_timezone='UTC')

    class Index:
        name: str = 'lamoda_product'
