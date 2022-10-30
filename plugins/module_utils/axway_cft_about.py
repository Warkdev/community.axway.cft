# -*- coding: utf-8 -*-
#
# Copyright: (c) 2022, Cédric Servais <cedric.servais@outlook.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.warkdev.axway_cft.plugins.module_utils.axway_utils import parse_fail_message
from ansible_collections.warkdev.axway_cft.plugins.module_utils.common import AxwayModuleError
from ansible.module_utils.connection import Connection

import logging

uri = '/about'

logger = logging.getLogger(__name__)


def fetch_about(module):
    """ This function fetch the Axway CFT version from the product

    Returns:
        _type_: _description_
    """
    connection = Connection(module._socket_path)
    response = connection.send_request(path=uri)

    if response['code'] != 200:
        raise AxwayModuleError(parse_fail_message(response['code'], response['contents']))

    return response['contents']
