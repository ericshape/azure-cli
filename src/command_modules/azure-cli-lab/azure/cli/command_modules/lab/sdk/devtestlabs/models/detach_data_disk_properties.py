# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class DetachDataDiskProperties(Model):
    """Request body for detaching data disk from a virtual machine.

    :param existing_lab_disk_id: Specifies the disk resource ID to detach from
     virtual machine.
    :type existing_lab_disk_id: str
    """

    _attribute_map = {
        'existing_lab_disk_id': {'key': 'existingLabDiskId', 'type': 'str'},
    }

    def __init__(self, existing_lab_disk_id=None):
        self.existing_lab_disk_id = existing_lab_disk_id
