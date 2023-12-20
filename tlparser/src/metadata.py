"""
metadata.py: File, containing metadata for a entire project.
"""


from common.utils.decorators import ReadOnlyClassProperty


class ProjectMetadata:
    """
    Metadata: Class, containing project metadata.
    """

    project_summary: str = 'Parsing Twich games, users and streams and Lamoda products by category.'
    project_description: str = (
        'This applications stands for parsing Twich and Lamoda. '
        'Twich can be parsed by games, streams and users. Lamoda can be parsed by categories. '
        'There are 2 types of endpoints. Firstly there are endpoints that are called by user. '
        'They do nothing except for producing message for kafka. '
        'Then there are endpoinds for that are called by kafka. They really do parsing. '
        'They are called when kafka consumer get a message. Kafka called them directly. '
    )

    @ReadOnlyClassProperty
    def metadata(cls) -> dict:
        """
        project: Return project metadata.

        Returns:
            dict: Project metadata.
        """

        return {
            'summary': cls.project_summary,
            'description': cls.project_description,
        }
