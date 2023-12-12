"""
containers.py: File, containing container that describe all dependencies in the project.
"""


from services.twich_services import TwichService
from services.lamoda_services import LamodaService
from controllers.twich_controllers import TwichController
from dependency_injector.providers import Factory
from controllers.lamoda_controllers import LamodaController
from dependency_injector.containers import WiringConfiguration, DeclarativeContainer
from repositories.twich_repositories import TwichMongoRepository
from repositories.lamoda_repositories import LamodaMongoRepository


class Container(DeclarativeContainer):
    """
    Container: Class, that describe all dependencies in the project.

    Args:
        DeclarativeContainer (_type_): Base superclass for a Containers class.
    """

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            'api.v1.endpoints.twich',
            'api.v1.endpoints.lamoda',
        ]
    )

    twich_repository: Factory = Factory(TwichMongoRepository)
    lamoda_repository: Factory = Factory(LamodaMongoRepository)

    twich_service: Factory = Factory(TwichService, twich_repository=twich_repository)
    lamoda_service: Factory = Factory(LamodaService, lamoda_repository=lamoda_repository)

    twich_controller: Factory = Factory(TwichController, twich_service=twich_service)
    lamoda_controller: Factory = Factory(LamodaController, lamoda_service=lamoda_service)
