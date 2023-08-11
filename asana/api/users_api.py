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


class UsersApi(object):
"""NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
Ref: https://github.com/swagger-api/swagger-codegen
"""

def __init__(self, api_client=None):
    if api_client is None:
        api_client = ApiClient()
    self.api_client = api_client

def get_favorites_for_user(self, user_gid, resource_type, workspace, **kwargs):  # noqa: E501
    """Get a user's favorites  # noqa: E501

    Returns all of a user's favorites in the given workspace, of the given type. Results are given in order (The same order as Asana's sidebar).  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_favorites_for_user(user_gid, resource_type, workspace, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
    :param str resource_type: The resource type of favorites to be returned. (required)
    :param str workspace: The workspace in which to get favorites. (required)
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AsanaNamedResourceArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_favorites_for_user_with_http_info(user_gid, resource_type, workspace, **kwargs)  # noqa: E501
    else:
        (data) = self.get_favorites_for_user_with_http_info(user_gid, resource_type, workspace, **kwargs)  # noqa: E501
        return data

def get_favorites_for_user_with_http_info(self, user_gid, resource_type, workspace, **kwargs):  # noqa: E501
    """Get a user's favorites  # noqa: E501

    Returns all of a user's favorites in the given workspace, of the given type. Results are given in order (The same order as Asana's sidebar).  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_favorites_for_user_with_http_info(user_gid, resource_type, workspace, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
    :param str resource_type: The resource type of favorites to be returned. (required)
    :param str workspace: The workspace in which to get favorites. (required)
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AsanaNamedResourceArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['user_gid', 'resource_type', 'workspace', 'limit', 'offset', 'opt_fields']  # noqa: E501
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
                " to method get_favorites_for_user" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'user_gid' is set
    if ('user_gid' not in params or
            params['user_gid'] is None):
        raise ValueError("Missing the required parameter `user_gid` when calling `get_favorites_for_user`")  # noqa: E501
    # verify the required parameter 'resource_type' is set
    if ('resource_type' not in params or
            params['resource_type'] is None):
        raise ValueError("Missing the required parameter `resource_type` when calling `get_favorites_for_user`")  # noqa: E501
    # verify the required parameter 'workspace' is set
    if ('workspace' not in params or
            params['workspace'] is None):
        raise ValueError("Missing the required parameter `workspace` when calling `get_favorites_for_user`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'user_gid' in params:
        path_params['user_gid'] = params['user_gid']  # noqa: E501

    query_params = []
    if 'limit' in params:
        query_params.append(('limit', params['limit']))  # noqa: E501
    if 'offset' in params:
        query_params.append(('offset', params['offset']))  # noqa: E501
    if 'resource_type' in params:
        query_params.append(('resource_type', params['resource_type']))  # noqa: E501
    if 'workspace' in params:
        query_params.append(('workspace', params['workspace']))  # noqa: E501
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
        '/users/{user_gid}/favorites', 'GET',
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

def get_user(self, user_gid, **kwargs):  # noqa: E501
    """Get a user  # noqa: E501

    Returns the full user record for the single user with the provided ID.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_user(user_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_user_with_http_info(user_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.get_user_with_http_info(user_gid, **kwargs)  # noqa: E501
        return data

def get_user_with_http_info(self, user_gid, **kwargs):  # noqa: E501
    """Get a user  # noqa: E501

    Returns the full user record for the single user with the provided ID.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_user_with_http_info(user_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str user_gid: A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['user_gid', 'opt_fields']  # noqa: E501
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
                " to method get_user" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'user_gid' is set
    if ('user_gid' not in params or
            params['user_gid'] is None):
        raise ValueError("Missing the required parameter `user_gid` when calling `get_user`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'user_gid' in params:
        path_params['user_gid'] = params['user_gid']  # noqa: E501

    query_params = []
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
        '/users/{user_gid}', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='UserResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def get_users(self, **kwargs):  # noqa: E501
    """Get multiple users  # noqa: E501

    Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter. Results are sorted by user ID.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_users(async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str workspace: The workspace or organization ID to filter users on.
    :param str team: The team ID to filter users on.
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_users_with_http_info(**kwargs)  # noqa: E501
    else:
        (data) = self.get_users_with_http_info(**kwargs)  # noqa: E501
        return data

def get_users_with_http_info(self, **kwargs):  # noqa: E501
    """Get multiple users  # noqa: E501

    Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter. Results are sorted by user ID.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_users_with_http_info(async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str workspace: The workspace or organization ID to filter users on.
    :param str team: The team ID to filter users on.
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['workspace', 'team', 'limit', 'offset', 'opt_fields']  # noqa: E501
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
                " to method get_users" % key
            )
        params[key] = val
    del params['kwargs']

    collection_formats = {}

    path_params = {}

    query_params = []
    if 'workspace' in params:
        query_params.append(('workspace', params['workspace']))  # noqa: E501
    if 'team' in params:
        query_params.append(('team', params['team']))  # noqa: E501
    if 'limit' in params:
        query_params.append(('limit', params['limit']))  # noqa: E501
    if 'offset' in params:
        query_params.append(('offset', params['offset']))  # noqa: E501
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
        '/users', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='UserResponseArray',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def get_users_for_team(self, team_gid, **kwargs):  # noqa: E501
    """Get users in a team  # noqa: E501

    Returns the compact records for all users that are members of the team. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_users_for_team(team_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str team_gid: Globally unique identifier for the team. (required)
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_users_for_team_with_http_info(team_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.get_users_for_team_with_http_info(team_gid, **kwargs)  # noqa: E501
        return data

def get_users_for_team_with_http_info(self, team_gid, **kwargs):  # noqa: E501
    """Get users in a team  # noqa: E501

    Returns the compact records for all users that are members of the team. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_users_for_team_with_http_info(team_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str team_gid: Globally unique identifier for the team. (required)
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['team_gid', 'offset', 'opt_fields']  # noqa: E501
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
                " to method get_users_for_team" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'team_gid' is set
    if ('team_gid' not in params or
            params['team_gid'] is None):
        raise ValueError("Missing the required parameter `team_gid` when calling `get_users_for_team`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'team_gid' in params:
        path_params['team_gid'] = params['team_gid']  # noqa: E501

    query_params = []
    if 'offset' in params:
        query_params.append(('offset', params['offset']))  # noqa: E501
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
        '/teams/{team_gid}/users', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='UserResponseArray',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def get_users_for_workspace(self, workspace_gid, **kwargs):  # noqa: E501
    """Get users in a workspace or organization  # noqa: E501

    Returns the compact records for all users in the specified workspace or organization. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_users_for_workspace(workspace_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_users_for_workspace_with_http_info(workspace_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.get_users_for_workspace_with_http_info(workspace_gid, **kwargs)  # noqa: E501
        return data

def get_users_for_workspace_with_http_info(self, workspace_gid, **kwargs):  # noqa: E501
    """Get users in a workspace or organization  # noqa: E501

    Returns the compact records for all users in the specified workspace or organization. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_users_for_workspace_with_http_info(workspace_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: UserResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['workspace_gid', 'offset', 'opt_fields']  # noqa: E501
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
                " to method get_users_for_workspace" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'workspace_gid' is set
    if ('workspace_gid' not in params or
            params['workspace_gid'] is None):
        raise ValueError("Missing the required parameter `workspace_gid` when calling `get_users_for_workspace`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'workspace_gid' in params:
        path_params['workspace_gid'] = params['workspace_gid']  # noqa: E501

    query_params = []
    if 'offset' in params:
        query_params.append(('offset', params['offset']))  # noqa: E501
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
        '/workspaces/{workspace_gid}/users', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='UserResponseArray',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)
