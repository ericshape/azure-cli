# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class DataDiskProperties(Model):
    """Request body for adding a new or existing data disk to a virtual machine.

    :param attach_new_data_disk_options: Specifies options to attach a new
     disk to the virtual machine.
    :type attach_new_data_disk_options: :class:`AttachNewDataDiskOptions
     <azure.mgmt.devtestlabs.models.AttachNewDataDiskOptions>`
    :param existing_lab_disk_id: Specifies the existing lab disk id to attach
     to virtual machine.
    :type existing_lab_disk_id: str
    :param host_caching: Caching option for a data disk (i.e. None, ReadOnly,
     ReadWrite). Possible values include: 'None', 'ReadOnly', 'ReadWrite'
    :type host_caching: str or :class:`HostCachingOptions
     <azure.mgmt.devtestlabs.models.HostCachingOptions>`
    """

    _attribute_map = {
        'attach_new_data_disk_options': {'key': 'attachNewDataDiskOptions', 'type': 'AttachNewDataDiskOptions'},
        'existing_lab_disk_id': {'key': 'existingLabDiskId', 'type': 'str'},
        'host_caching': {'key': 'hostCaching', 'type': 'str'},
    }

    def __init__(self, attach_new_data_disk_options=None, existing_lab_disk_id=None, host_caching=None):
        self.attach_new_data_disk_options = attach_new_data_disk_options
        self.existing_lab_disk_id = existing_lab_disk_id
        self.host_caching = host_caching
