"""
LibNix
Copyright (C) 2017  Mark Biciunas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import typing


class SysClassNet:

    def __init__(self):
        self._PATH = "/sys/class/net"

        self._ADDR_ASSIGN_TYPE = "addr_assign_type"
        self._ADDRESS = "address"
        self._ADDR_LEN = "addr_len"
        self._BROADCAST = "broadcast"
        self._CARRIER = "carrier"
        self._CARRIER_CHANGES = "carrier_changes"
        self._DEV_ID = "dev_id"
        self._DEV_PORT = "dev_port"
        self._DORMANT = "dormant"
        self._DUPLEX = "duplex"
        self._FLAGS = "flags"
        self._GRO_FLUSH_TIMEOUT = "gro_flush_timeout"
        self._IF_ALIAS = "ifalias"
        self._IF_INDEX = "ifindex"
        self._IF_LINK = "iflink"
        self._LINK_MODE = "link_mode"
        self._MTU = "mtu"
        self._NAME_ASSIGN_TYPE = "name_assign_type"
        self._NETDEV_GROUP = "netdev_group"
        self._OPERSTATE = "operstate"
        self._PHYS_PORT_ID = "phys_port_id"
        self._PHYS_PORT_NAME = "phys_port_name"
        self._PHYS_SWITCH_ID = "phys_switch_id"
        self._PROTO_DOWN = "proto_down"
        self._SPEED = "speed"
        self._TX_QUEUE_LEN = "tx_queue_len"
        self._TYPE = "type"
        self._UEVENT = "uevent"

        self._network = {}

        for _name in self._get_immediate_subdirectories():
            self._network[_name] = self._gather_interface(_name)

    def _get_immediate_subdirectories(self) -> list:
        return [name for name in os.listdir(self._PATH) if os.path.isdir(os.path.join(self._PATH, name))]

    def _gather_interface(self, interface: str) -> dict:
        _interface = {}

        _path = os.path.join(self._PATH, interface)

        _interface[self._ADDR_ASSIGN_TYPE] = self._read(os.path.join(_path, "addr_assign_type"))
        _interface[self._ADDRESS] = self._read(os.path.join(_path, "address"))
        _interface[self._ADDR_LEN] = self._read(os.path.join(_path, "addr_len"))
        _interface[self._BROADCAST] = self._read(os.path.join(_path, "broadcast"))
        _interface[self._CARRIER] = self._read(os.path.join(_path, "carrier"))
        _interface[self._CARRIER_CHANGES] = self._read(os.path.join(_path, "carrier_changes"))
        _interface[self._DEV_ID] = self._read(os.path.join(_path, "dev_id"))
        _interface[self._DEV_PORT] = self._read(os.path.join(_path, "dev_port"))
        _interface[self._DORMANT] = self._read(os.path.join(_path, "dormant"))
        _interface[self._DUPLEX] = self._read(os.path.join(_path, "duplex"))
        _interface[self._FLAGS] = self._read(os.path.join(_path, "flags"))
        _interface[self._GRO_FLUSH_TIMEOUT] = self._read(os.path.join(_path, "gro_flush_timeout"))
        _interface[self._IF_ALIAS] = self._read(os.path.join(_path, "ifalias"))
        _interface[self._IF_INDEX] = self._read(os.path.join(_path, "ifindex"))
        _interface[self._IF_LINK] = self._read(os.path.join(_path, "iflink"))
        _interface[self._LINK_MODE] = self._read(os.path.join(_path, "link_mode"))
        _interface[self._MTU] = self._read(os.path.join(_path, "mtu"))
        _interface[self._NAME_ASSIGN_TYPE] = self._read(os.path.join(_path, "name_assign_type"))
        _interface[self._NETDEV_GROUP] = self._read(os.path.join(_path, "netdev_group"))
        _interface[self._OPERSTATE] = self._read(os.path.join(_path, "operstate"))
        _interface[self._PHYS_PORT_ID] = self._read(os.path.join(_path, "phys_port_id"))
        _interface[self._PHYS_PORT_NAME] = self._read(os.path.join(_path, "phys_port_name"))
        _interface[self._PHYS_SWITCH_ID] = self._read(os.path.join(_path, "phys_switch_id"))
        _interface[self._PROTO_DOWN] = self._read(os.path.join(_path, "proto_down"))
        _interface[self._SPEED] = self._read(os.path.join(_path, "speed"))
        _interface[self._TX_QUEUE_LEN] = self._read(os.path.join(_path, "tx_queue_len"))
        _interface[self._TYPE] = self._read(os.path.join(_path, "type"))
        _interface[self._UEVENT] = self._read(os.path.join(_path, "uevent"))

        return _interface

    @staticmethod
    def _read(filename: str) -> str:
        try:
            with open(filename, 'r') as f:
                _data = f.read().strip()
        except OSError:
            _data = None

        return _data

    def get_interfaces(self) -> iter:
        return self._network.keys()

    def get_addr_assign_type(self, interface: str) -> str:
        return self._get_value(interface, self._ADDR_ASSIGN_TYPE)

    def get_address(self, interface: str) -> str:
        return self._get_value(interface, self._ADDRESS)

    def get_addr_len(self, interface: str) -> str:
        return self._get_value(interface, self._ADDR_LEN)

    def get_broadcast(self, interface: str) -> str:
        return self._get_value(interface, self._BROADCAST)

    def get_carrier(self, interface: str) -> str:
        return self._get_value(interface, self._CARRIER)

    def get_carrier_changes(self, interface: str) -> str:
        return self._get_value(interface, self._CARRIER_CHANGES)

    def get_dev_id(self, interface: str) -> str:
        return self._get_value(interface, self._DEV_ID)

    def get_dev_port(self, interface: str) -> str:
        return self._get_value(interface, self._DEV_PORT)

    def get_dormant(self, interface: str) -> str:
        return self._get_value(interface, self._DORMANT)

    def get_duplex(self, interface: str) -> str:
        return self._get_value(interface, self._DUPLEX)

    def get_flags(self, interface: str) -> str:
        return self._get_value(interface, self._FLAGS)

    def get_gro_flush_timeout(self, interface: str) -> str:
        return self._get_value(interface, self._GRO_FLUSH_TIMEOUT)

    def get_ifalias(self, interface: str) -> str:
        return self._get_value(interface, self._IF_ALIAS)

    def get_ifindex(self, interface: str) -> str:
        return self._get_value(interface, self._IF_INDEX)

    def get_iflink(self, interface: str) -> str:
        return self._get_value(interface, self._IF_LINK)

    def get_link_mode(self, interface: str) -> str:
        return self._get_value(interface, self._LINK_MODE)

    def get_mtu(self, interface: str) -> str:
        return self._get_value(interface, self._MTU)

    def get_name_assign_type(self, interface: str) -> str:
        return self._get_value(interface, self._NAME_ASSIGN_TYPE)

    def get_netdev_group(self, interface: str) -> str:
        return self._get_value(interface, self._NETDEV_GROUP)

    def get_operstate(self, interface: str) -> str:
        return self._get_value(interface, self._OPERSTATE)

    def get_phys_port_id(self, interface: str) -> str:
        return self._get_value(interface, self._PHYS_PORT_ID)

    def get_phys_port_name(self, interface: str) -> str:
        return self._get_value(interface, self._PHYS_PORT_NAME)

    def get_phys_switch_id(self, interface: str) -> str:
        return self._get_value(interface, self._PHYS_SWITCH_ID)

    def get_proto_down(self, interface: str) -> str:
        return self._get_value(interface, self._PROTO_DOWN)

    def get_speed(self, interface: str) -> str:
        return self._get_value(interface, self._SPEED)

    def get_tx_queue_len(self, interface: str) -> str:
        return self._get_value(interface, self._TX_QUEUE_LEN)

    def get_type(self, interface: str) -> str:
        return self._get_value(interface, self._TYPE)

    def get_uevent(self, interface: str) -> str:
        return self._get_value(interface, self._UEVENT)

    def _get_value(self, interface: str, item: str) -> typing.Optional[str]:
        try:
            return self._network[interface][item]
        except KeyError:
            return None


def main():
    sys_class_net = SysClassNet()

    # sys_class_net.gather()

    for _interface in sys_class_net.get_interfaces():
        print("{}".format(_interface))
        print("  address: {}".format(sys_class_net.get_address(_interface)))
        print("  broadcast: {}".format(sys_class_net.get_broadcast(_interface)))
        print("  flags: {}".format(sys_class_net.get_flags(_interface)))
        print("  operstate: {}".format(sys_class_net.get_operstate(_interface)))

if __name__ == "__main__":
    main()
