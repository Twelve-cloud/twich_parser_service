"""
query_handler.py: File, containing query handler interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic
from application.dto import RD
from application.queries import Q


class IQueryHandler(Interface, Generic[Q, RD]):
    """
    IQueryHandler: Class, representing query handler interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
        2) Generic[Q, RD]: Generic class. This class makes repository interface generic.
    """

    @abstractmethod
    async def handle(self, query: Q) -> RD:
        """
        handle: Should handle query.
        Must be overriden.

        Args:
            query (Q): Query instance.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            RD: Result of the query (some DTO).
        """

        raise NotImplementedError
