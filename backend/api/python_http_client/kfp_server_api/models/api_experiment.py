# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class ApiExperiment(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'resource_references': 'list[ApiResourceReference]',
        'storage_state': 'ExperimentStorageState'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'resource_references': 'resource_references',
        'storage_state': 'storage_state'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, resource_references=None, storage_state=None, local_vars_configuration=None):  # noqa: E501
        """ApiExperiment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._resource_references = None
        self._storage_state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if resource_references is not None:
            self.resource_references = resource_references
        if storage_state is not None:
            self.storage_state = storage_state

    @property
    def id(self):
        """Gets the id of this ApiExperiment.  # noqa: E501

        Output. Unique experiment ID. Generated by API server.  # noqa: E501

        :return: The id of this ApiExperiment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiExperiment.

        Output. Unique experiment ID. Generated by API server.  # noqa: E501

        :param id: The id of this ApiExperiment.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiExperiment.  # noqa: E501

        Required input field. Unique experiment name provided by user.  # noqa: E501

        :return: The name of this ApiExperiment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiExperiment.

        Required input field. Unique experiment name provided by user.  # noqa: E501

        :param name: The name of this ApiExperiment.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiExperiment.  # noqa: E501


        :return: The description of this ApiExperiment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiExperiment.


        :param description: The description of this ApiExperiment.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ApiExperiment.  # noqa: E501

        Output. The time that the experiment created.  # noqa: E501

        :return: The created_at of this ApiExperiment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiExperiment.

        Output. The time that the experiment created.  # noqa: E501

        :param created_at: The created_at of this ApiExperiment.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def resource_references(self):
        """Gets the resource_references of this ApiExperiment.  # noqa: E501

        Optional input field. Specify which resource this run belongs to. For Experiment, the only valid resource reference is a single Namespace.  # noqa: E501

        :return: The resource_references of this ApiExperiment.  # noqa: E501
        :rtype: list[ApiResourceReference]
        """
        return self._resource_references

    @resource_references.setter
    def resource_references(self, resource_references):
        """Sets the resource_references of this ApiExperiment.

        Optional input field. Specify which resource this run belongs to. For Experiment, the only valid resource reference is a single Namespace.  # noqa: E501

        :param resource_references: The resource_references of this ApiExperiment.  # noqa: E501
        :type resource_references: list[ApiResourceReference]
        """

        self._resource_references = resource_references

    @property
    def storage_state(self):
        """Gets the storage_state of this ApiExperiment.  # noqa: E501


        :return: The storage_state of this ApiExperiment.  # noqa: E501
        :rtype: ExperimentStorageState
        """
        return self._storage_state

    @storage_state.setter
    def storage_state(self, storage_state):
        """Sets the storage_state of this ApiExperiment.


        :param storage_state: The storage_state of this ApiExperiment.  # noqa: E501
        :type storage_state: ExperimentStorageState
        """

        self._storage_state = storage_state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiExperiment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiExperiment):
            return True

        return self.to_dict() != other.to_dict()
