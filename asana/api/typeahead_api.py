# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from asana.api_client import ApiClient


class TypeaheadApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def typeahead_for_workspace(self, workspace_gid, resource_type, **kwargs):  # noqa: E501
        """Get objects via typeahead  # noqa: E501

        Retrieves objects in the workspace based via an auto-completion/typeahead search algorithm. This feature is meant to provide results quickly, so do not rely on this API to provide extremely accurate search results. The result set is limited to a single page of results with a maximum size, so you won’t be able to fetch large numbers of results.  The typeahead search API provides search for objects from a single workspace. This endpoint should be used to query for objects when creating an auto-completion/typeahead search feature. This API is meant to provide results quickly and should not be relied upon for accurate or exhaustive search results. The results sets are limited in size and cannot be paginated.  Queries return a compact representation of each object which is typically the gid and name fields. Interested in a specific set of fields or all of the fields?! Of course you are. Use field selectors to manipulate what data is included in a response.  Resources with type `user` are returned in order of most contacted to least contacted. This is determined by task assignments, adding the user to projects, and adding the user as a follower to tasks, messages, etc.  Resources with type `project` are returned in order of recency. This is determined when the user visits the project, is added to the project, and completes tasks in the project.  Resources with type `task` are returned with priority placed on tasks the user is following, but no guarantee on the order of those tasks.  Resources with type `project_template` are returned with priority placed on favorited project templates.  Leaving the `query` string empty or omitted will give you results, still following the resource ordering above. This could be used to list users or projects that are relevant for the requesting user's api token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.typeahead_for_workspace(workspace_gid, resource_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param str resource_type: The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `project`, `project_template`, `portfolio`, `tag`, `task`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported. (required)
        :param str type: *Deprecated: new integrations should prefer the resource_type field.*
        :param str query: The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results.
        :param int count: The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: AsanaNamedResourceArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.typeahead_for_workspace_with_http_info(workspace_gid, resource_type, **kwargs)  # noqa: E501
        else:
            (data) = self.typeahead_for_workspace_with_http_info(workspace_gid, resource_type, **kwargs)  # noqa: E501
            return data

    def typeahead_for_workspace_with_http_info(self, workspace_gid, resource_type, **kwargs):  # noqa: E501
        """Get objects via typeahead  # noqa: E501

        Retrieves objects in the workspace based via an auto-completion/typeahead search algorithm. This feature is meant to provide results quickly, so do not rely on this API to provide extremely accurate search results. The result set is limited to a single page of results with a maximum size, so you won’t be able to fetch large numbers of results.  The typeahead search API provides search for objects from a single workspace. This endpoint should be used to query for objects when creating an auto-completion/typeahead search feature. This API is meant to provide results quickly and should not be relied upon for accurate or exhaustive search results. The results sets are limited in size and cannot be paginated.  Queries return a compact representation of each object which is typically the gid and name fields. Interested in a specific set of fields or all of the fields?! Of course you are. Use field selectors to manipulate what data is included in a response.  Resources with type `user` are returned in order of most contacted to least contacted. This is determined by task assignments, adding the user to projects, and adding the user as a follower to tasks, messages, etc.  Resources with type `project` are returned in order of recency. This is determined when the user visits the project, is added to the project, and completes tasks in the project.  Resources with type `task` are returned with priority placed on tasks the user is following, but no guarantee on the order of those tasks.  Resources with type `project_template` are returned with priority placed on favorited project templates.  Leaving the `query` string empty or omitted will give you results, still following the resource ordering above. This could be used to list users or projects that are relevant for the requesting user's api token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.typeahead_for_workspace_with_http_info(workspace_gid, resource_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :param str resource_type: The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `project`, `project_template`, `portfolio`, `tag`, `task`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported. (required)
        :param str type: *Deprecated: new integrations should prefer the resource_type field.*
        :param str query: The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results.
        :param int count: The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: AsanaNamedResourceArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_gid', 'resource_type', 'type', 'query', 'count', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method typeahead_for_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_gid' is set
        if ('workspace_gid' not in params or
                params['workspace_gid'] is None):
            raise ValueError("Missing the required parameter `workspace_gid` when calling `typeahead_for_workspace`")  # noqa: E501
        # verify the required parameter 'resource_type' is set
        if ('resource_type' not in params or
                params['resource_type'] is None):
            raise ValueError("Missing the required parameter `resource_type` when calling `typeahead_for_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_gid' in params:
            path_params['workspace_gid'] = params['workspace_gid']  # noqa: E501

        query_params = []
        if 'resource_type' in params:
            query_params.append(('resource_type', params['resource_type']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace_gid}/typeahead', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsanaNamedResourceArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
