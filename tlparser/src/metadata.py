"""
metadata.py: File, containing metadata for an entire project.
"""


from shared.utils import ReadOnlyClassProperty


class ProjectMetadata:
    """
    ProjectMetadata: Class, representing project metadata. This class contains all project metadata.
    """

    project_summary: str = 'Parser for twich games, users and streams.'
    project_description: str = (
        'This applications stands for parsing Twich.'
        'You can parse twich games, streams and users.'
        'You can use REST API or GraphQL api to make rpc calls.'
        'CUD operation are processed by PostgreSQL, R operation are processed by MongoDB.'
        'Logs are stored in Elastic Search, aggregated by Logstash, can be available in Kibana'
        'Other metrics are aggregated by Prometheus, can be available in Grafana.'
        'For IPC Kafka is used. Project architecture is DDD + Onion Architecture + CQRS.'
        'This app are deployed in Kubernetes using Docker. For CI GitHub Actions is used.'
        'Mongo supports master-slave replication and sharding, PostgreSQL supports sharding.'
    )

    @ReadOnlyClassProperty
    def metadata(cls) -> dict:
        """
        metadata: Returns project metadata.

        Returns:
            dict: Project metadata.
        """

        return {
            'summary': cls.project_summary,
            'description': cls.project_description,
        }
