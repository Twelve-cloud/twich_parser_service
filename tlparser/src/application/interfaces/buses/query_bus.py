"""
base.py: File, containing query bus interface.
"""


from abc import ABC as Interface
from abc import abstractmethod
from application.dto import DTO
from application.interfaces.handlers import IQueryHandler
from application.queries import Query


class IQueryBus(Interface):
    """
    IQueryBus: Class, representing query bus interface. This class is an interface.
    You can create an instance of this class, but Interface shows that you should not do this.
    Interface base class is Abstract Base Class. It is called Interface to make intention explicit.

    Bases:
        1) Interface: Abstract Base Class. It is a marker that this class provides interface only.
        2) Generic[Q, QH, RD]: Generic class. This class makes query bus interface generic.
    """

    @abstractmethod
    def register(self, query_class: type[Query], query_handler: IQueryHandler) -> None:
        """
        register: Should register query in query bus.
        Must be overriden.

        Args:
            query_class (type[Query]): Class of the query.
            query_handler (IQueryHandler): Query handler.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.
        """

        raise NotImplementedError

    @abstractmethod
    async def dispatch(self, query: Query) -> DTO:
        """
        dispatch: Should dispatch query to query handler.
        Must be overriden.

        Args:
            query (Query): Query.

        Raises:
            NotImplementedError: Raises to prevent calling this method by super.

        Returns:
            DTO: Any result dto that query handler returns.
        """

        raise NotImplementedError
