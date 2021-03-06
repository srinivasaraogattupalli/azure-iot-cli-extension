# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PropertyTest(Model):
    """PropertyTest.

    :param property:
    :type property: ~product.models.PropertyModel
    :param value_to_write:
    :type value_to_write: str
    :param value_to_report:
    :type value_to_report: str
    :param validation_timeout:
    :type validation_timeout: int
    :param is_mandatory:
    :type is_mandatory: bool
    :param should_validate:
    :type should_validate: bool
    """

    _attribute_map = {
        'property': {'key': 'property', 'type': 'PropertyModel'},
        'value_to_write': {'key': 'valueToWrite', 'type': 'str'},
        'value_to_report': {'key': 'valueToReport', 'type': 'str'},
        'validation_timeout': {'key': 'validationTimeout', 'type': 'int'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'should_validate': {'key': 'shouldValidate', 'type': 'bool'},
    }

    def __init__(self, *, property=None, value_to_write: str=None, value_to_report: str=None, validation_timeout: int=None, is_mandatory: bool=None, should_validate: bool=None, **kwargs) -> None:
        super(PropertyTest, self).__init__(**kwargs)
        self.property = property
        self.value_to_write = value_to_write
        self.value_to_report = value_to_report
        self.validation_timeout = validation_timeout
        self.is_mandatory = is_mandatory
        self.should_validate = should_validate
