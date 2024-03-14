"""
base.py: File, containing base parser interface.
"""


from abc import ABC as Interface


class IParser(Interface):
    """
    IParser: Class, representing parser interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
    """

    pass
