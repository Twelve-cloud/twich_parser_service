"""
containers.py: File, containing container that describe all dependencies in the project.
"""


from controllers.twich_controllers import TwichController
from dependency_injector.providers import Factory
from controllers.lamoda_controllers import LamodaController
from dependency_injector.containers import WiringConfiguration, DeclarativeContainer


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

    twich_controller: Factory = Factory(TwichController)
    lamoda_controller: Factory = Factory(LamodaController)
