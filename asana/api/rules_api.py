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


class RulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def trigger_rule(self, body, rule_trigger_gid, **kwargs):  # noqa: E501
        """Trigger a rule  # noqa: E501

        Trigger a rule which uses an [\"incoming web request\"](/docs/incoming-web-requests) trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trigger_rule(body, rule_trigger_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RuleTriggerGidRunBody body: A dictionary of variables accessible from within the rule. (required)
        :param str rule_trigger_gid: The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint. (required)
        :return: RuleTriggerResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.trigger_rule_with_http_info(body, rule_trigger_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_rule_with_http_info(body, rule_trigger_gid, **kwargs)  # noqa: E501
            return data

    def trigger_rule_with_http_info(self, body, rule_trigger_gid, **kwargs):  # noqa: E501
        """Trigger a rule  # noqa: E501

        Trigger a rule which uses an [\"incoming web request\"](/docs/incoming-web-requests) trigger.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trigger_rule_with_http_info(body, rule_trigger_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RuleTriggerGidRunBody body: A dictionary of variables accessible from within the rule. (required)
        :param str rule_trigger_gid: The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint. (required)
        :return: RuleTriggerResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'rule_trigger_gid']  # noqa: E501
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
                    " to method trigger_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `trigger_rule`")  # noqa: E501
        # verify the required parameter 'rule_trigger_gid' is set
        if ('rule_trigger_gid' not in params or
                params['rule_trigger_gid'] is None):
            raise ValueError("Missing the required parameter `rule_trigger_gid` when calling `trigger_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_trigger_gid' in params:
            path_params['rule_trigger_gid'] = params['rule_trigger_gid']  # noqa: E501

        query_params = []


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/rule_triggers/{rule_trigger_gid}/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RuleTriggerResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
