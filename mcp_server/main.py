# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:12:41+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import (
    APIKeyHeader,
    BaseSecurity,
    UnsuportedSecurityStub,
)

app = MCPProxy(
    contact={
        'email': 'data@gov.bc.ca',
        'name': 'Data BC',
        'url': 'http://data.gov.bc.ca/',
    },
    description='This API provides live access to the BC Data Catalogue. Further documentation on the API is available from http://docs.ckan.org/en/latest/ Confirm the version of the API available from the catalogue by requesting https://catalogue.data.gov.bc.ca/api/3/action/status_show. \n\nPlease note that you may experience issues when submitting requests to the delivery or test environment if using this [OpenAPI specification](https://github.com/bcgov/api-specs) in other API console viewers.',
    license={
        'name': 'Open Government License - British Columbia',
        'url': 'https://www2.gov.bc.ca/gov/content?id=A519A56BC2BF44E4A008B33FCF527F61',
    },
    termsOfService='https://www2.gov.bc.ca/gov/content?id=D1EE0A405E584363B205CD4353E02C88',
    title='BC Data Catalogue API',
    version='3.0.1',
    servers=[
        {'description': 'Production', 'url': 'https://catalogue.data.gov.bc.ca/api/3'},
        {'description': 'Test', 'url': 'https://cat.data.gov.bc.ca/api/3'},
        {'description': 'Delivery', 'url': 'https://cad.data.gov.bc.ca/api/3'},
    ],
)


@app.get(
    '/action/organization_activity_list',
    description=""" Return an organization's activity stream """,
    tags=['organization_activity_management', 'organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_activity_list(
    id: Optional[str] = 'ministry-of-agriculture',
):
    """
    Get the activity stream of an organization
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_activity_list_html',
    description=""" Return an organization's activity stream as HTML """,
    tags=['organization_activity_management', 'organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_activity_list_html(
    id: Optional[str] = 'ministry-of-agriculture',
):
    """
    Get the activity stream of an organization, HTML format
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_autocomplete',
    description=""" Return a list of organization names that contain a string """,
    tags=['organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_autocomplete(
    q: Optional[str] = 'ministry', limit: Optional[int] = 20
):
    """
    Get names of organizations that match a query string
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_follower_count',
    description=""" Return the number of followers of an organization """,
    tags=['organization_activity_management', 'organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_follower_count(
    id: Optional[str] = 'ministry-of-agriculture',
):
    """
    Get number of followers of an organization
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_follower_list',
    description=""" Return a list of users that are following a given organization """,
    tags=['organization_activity_management', 'organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_follower_list(
    id: Optional[str] = 'ministry-of-agriculture',
):
    """
    Get users following an organization
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_list',
    description=""" Returns the names of all indexed organizations """,
    tags=['organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_list(offset: Optional[int] = 0, limit: Optional[int] = 100):
    """
    Get names of all organizations
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_list_for_user',
    description=""" Return the organizations that the user has a given permission for """,
    tags=['organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_list_for_user(permission: Optional[str] = '"edit_group"'):
    """
    Get organizations that a user has a given permission for
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_revision_list',
    description=""" Return an organization's revisions """,
    tags=['organization_activity_management', 'organization_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_revision_list(
    id: Optional[str] = 'ministry-of-agriculture',
):
    """
    Get organization revisions
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/organization_show',
    description=""" Return the details of an organization """,
    tags=['organization_management', 'organization_activity_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_organization_show(
    id: Optional[str] = 'ministry-of-agriculture',
    include_datasets: Optional[bool] = True,
):
    """
    Get details of a specific organization
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_activity_list',
    description=""" Returns a package's activity stream """,
    tags=['package_activity_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_activity_list(
    id: Optional[str] = 'grizzly-bear-population-units',
    offset: Optional[int] = 0,
    limit: Optional[int] = 31,
):
    """
    Get the activity stream of a package (dataset)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_activity_list_html',
    description=""" The activity stream is rendered as a snippet of HTML meant to be included in an HTML pag, i.e it doesn't have any header or footer. """,
    tags=['package_activity_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_activity_list_html(
    id: Optional[str] = 'grizzly-bear-population-units',
    offset: Optional[int] = 0,
    limit: Optional[int] = 31,
):
    """
    Get the activity stream of a package (dataset), HTML format
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_autocomplete',
    description=""" Return a list of datasets that match a string """,
    tags=['package_management', 'resource_metadata_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_autocomplete(
    q: Optional[str] = '"Okanagan Lake"', limit: Optional[int] = 10
):
    """
    Find packages (datasets) matching a query
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_list',
    description=""" Returns the names of all indexed packages (datasets) """,
    tags=['package_management', 'package_activity_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_list(offset: Optional[int] = 0, limit: Optional[int] = 100):
    """
    Get a list of all packages (datasets)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_relationships_list',
    description=""" Return a dataset's relationships """,
    tags=['package_activity_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_relationships_list(
    id: Optional[str] = 'grizzly-bear-population-units',
    id2: Optional[str] = 'important-fossil-areas',
    rel: Optional[str] = None,
):
    """
    Get package (dataset) relationships
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_revision_list',
    description=""" Return a dataset's revision as a list of dictionaries """,
    tags=['package_activity_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_revision_list(
    id: Optional[str] = 'grizzly-bear-population-units',
):
    """
    Get list of revisions for a package (dataset)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_search',
    description=""" Searches for packages (datasets) matching the specified query terms """,
    tags=['package_management', 'resource_metadata_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_search(q: Optional[str] = '"Okanagan Lake"'):
    """
    Find packages (datasets) matching query terms
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/package_show',
    description=""" Returns metadata about the package (dataset) corresponding to the specified unique name """,
    tags=['package_management', 'resource_metadata_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_package_show(id: Optional[str] = 'grizzly-bear-population-units'):
    """
    Get metadata about one specific package (dataset)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/related_list',
    description=""" Returns a dataset's related items. """,
    tags=['package_activity_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_related_list(
    id: Optional[str] = None,
    dataset: Optional[str] = None,
    type_filter: Optional[str] = None,
    sort: Optional[str] = None,
    featured: Optional[str] = None,
):
    """
    Gets items related to a package (dataset)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/resource_search',
    description=""" Returns a dictionary with two fields ``count`` and ``results``.             The ``count`` field contains the total number of Resources                found without the limit or query parameters having an effect.             The ``results`` field is a list of dictized Resource objects.             The query parameter is a required field. It is a string in                the form ``{field}:{term}`` or a list of strings, each of the             same form. Within each string, ``{field}`` is a field or extra             field on the Resource domain object. """,
    tags=['resource_metadata_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_resource_search(
    query: Optional[str] = 'format:csv',
    fields: Optional[str] = None,
    order_by: Optional[str] = None,
    offset: Optional[int] = 0,
    limit: Optional[int] = 0,
):
    """
    Find resources
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/resource_show',
    description=""" Return the metadata of a resource """,
    tags=['resource_metadata_management', 'package_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_resource_show(
    id: Optional[str] = 'e6c8bb1d-3726-418b-9b7e-1d97a9bbb817',
    include_tracking: Optional[bool] = False,
):
    """
    Get metadata for a specific resource
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/status_show',
    description=""" Returns the site status """,
    tags=['site_health_status'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_status_show():
    """
    Get the site status
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/action/tag_list',
    description=""" Returns the names of all indexed tags """,
    tags=['tagging_system_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyHeader(name="ckan_api_key"),
    ],
)
def get_action_tag_list(offset: Optional[int] = 0, limit: Optional[int] = 100):
    """
    Get a list of tags
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
