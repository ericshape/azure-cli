# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class LabCostDetailsProperties(Model):
    """The properties of a lab cost item.

    :param date_property: The date of the cost item.
    :type date_property: datetime
    :param cost: The cost component of the cost item.
    :type cost: float
    :param cost_type: The type of the cost. Possible values include:
     'Unavailable', 'Reported', 'Projected'
    :type cost_type: str or :class:`CostType
     <azure.mgmt.devtestlabs.models.CostType>`
    """

    _attribute_map = {
        'date_property': {'key': 'date', 'type': 'iso-8601'},
        'cost': {'key': 'cost', 'type': 'float'},
        'cost_type': {'key': 'costType', 'type': 'str'},
    }

    def __init__(self, date_property=None, cost=None, cost_type=None):
        self.date_property = date_property
        self.cost = cost
        self.cost_type = cost_type
