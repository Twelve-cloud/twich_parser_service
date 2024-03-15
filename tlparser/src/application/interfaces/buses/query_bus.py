"""
base.py: File, containing query bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from typing import Generic
from application.dto import RD
from application.interfaces.handlers import QH
from application.queries import Q


class IQueryBus(Interface, Generic[Q, QH, RD]):
    """
    IQueryBus: Class, representing query bus interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
        2) Generic[Q, QH, RD]: Generic class. This class makes query bus interface generic.
    """

    @abstractmethod
    def register(self, query_class: type[Q], query_handler: QH) -> None:
        """
        register: Should register query in query bus.
        Must be overriden.

        Args:
            query_class (type[Q]): Class of the query.
            query_handler (QH): Query handler.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    def dispatch(self, query: Q) -> RD:
        """
        dispatch: Should dispatch query to query handler.
        Must be overriden.

        Args:
            query (Q): Query.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            RD: Any result dto that query handler returns.
        """

        raise NotImplementedError
