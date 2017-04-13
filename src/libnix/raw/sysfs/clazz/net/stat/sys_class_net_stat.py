# Nix
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import typing


class SysClassNetStat:

    def __init__(self) -> None:
        self._PATH = "/sys/class/net"

        self._STAT_COLLISIONS = "collisions"
        self._STAT_MULTICAST = "multicast"
        self._STAT_RX_BYTES = "rx_bytes"
        self._STAT_RX_COMPRESSED = "rx_compressed"
        self._STAT_RX_CRC_ERRORS = "rx_crc_errors"
        self._STAT_RX_DROPPED = "rx_dropped"
        self._STAT_RX_ERRORS = "rx_errors"
        self._STAT_RX_FIFO_ERROR = "rx_fifo_errors"
        self._STAT_RX_FRAME_ERRORS = "rx_frame_errors"
        self._STAT_RX_LENGTH_ERRORS = "rx_length_errors"
        self._STAT_RX_MISSED_ERRORS = "rx_missed_errors"
        self._STAT_RX_NOHANDLER = "rx_nohandler"
        self._STAT_RX_OVER_ERRORS = "rx_over_errors"
        self._STAT_RX_PACKETS = "rx_packets"
        self._STAT_TX_ABORTED_ERRORS = "tx_aborted_errors"
        self._STAT_TX_BYTES = "tx_bytes"
        self._STAT_TX_CARRIER_ERRORS = "tx_carrier_errors"
        self._STAT_TX_COMPRESSED = "tx_compressed"
        self._STAT_TX_DROPPED = "tx_dropped"
        self._STAT_TX_ERRORS = "tx_errors"
        self._STAT_TX_FIFO_ERRORS = "tx_fifo_errors"
        self._STAT_TX_HEARTBEAT_ERRORS = "tx_heartbeat_errors"
        self._STAT_TX_PACKETS = "tx_packets"
        self._STAT_TX_WINDOW_ERRORS = "tx_window_errors"

        self._network = {}

        for _name in self._get_immediate_subdirectories():
            self._network[_name] = self._gather_interface(_name)

    def _get_immediate_subdirectories(self) -> list:
        return [name for name in os.listdir(self._PATH) if os.path.isdir(os.path.join(self._PATH, name))]

    def _gather_interface(self, interface: str) -> dict:
        _interface = {}

        _path = os.path.join(self._PATH, interface, "statistics")

        _path = os.path.join(_path)

        _interface[self._STAT_COLLISIONS] = self._read(os.path.join(_path, "collisions"))
        _interface[self._STAT_MULTICAST] = self._read(os.path.join(_path, "multicast"))
        _interface[self._STAT_RX_BYTES] = self._read(os.path.join(_path, "rx_bytes"))
        _interface[self._STAT_RX_COMPRESSED] = self._read(os.path.join(_path, "rx_compressed"))
        _interface[self._STAT_RX_CRC_ERRORS] = self._read(os.path.join(_path, "rx_crc_errors"))
        _interface[self._STAT_RX_DROPPED] = self._read(os.path.join(_path, "rx_dropped"))
        _interface[self._STAT_RX_ERRORS] = self._read(os.path.join(_path, "rx_errors"))
        _interface[self._STAT_RX_FIFO_ERROR] = self._read(os.path.join(_path, "rx_fifo_errors"))
        _interface[self._STAT_RX_FRAME_ERRORS] = self._read(os.path.join(_path, "rx_frame_errors"))
        _interface[self._STAT_RX_LENGTH_ERRORS] = self._read(os.path.join(_path, "rx_length_errors"))
        _interface[self._STAT_RX_MISSED_ERRORS] = self._read(os.path.join(_path, "rx_missed_errors"))
        _interface[self._STAT_RX_NOHANDLER] = self._read(os.path.join(_path, "rx_nohandler"))
        _interface[self._STAT_RX_OVER_ERRORS] = self._read(os.path.join(_path, "rx_over_errors"))
        _interface[self._STAT_RX_PACKETS] = self._read(os.path.join(_path, "rx_packets"))
        _interface[self._STAT_TX_ABORTED_ERRORS] = self._read(os.path.join(_path, "tx_aborted_errors"))
        _interface[self._STAT_TX_BYTES] = self._read(os.path.join(_path, "tx_bytes"))
        _interface[self._STAT_TX_CARRIER_ERRORS] = self._read(os.path.join(_path, "tx_carrier_errors"))
        _interface[self._STAT_TX_COMPRESSED] = self._read(os.path.join(_path, "tx_compressed"))
        _interface[self._STAT_TX_DROPPED] = self._read(os.path.join(_path, "tx_dropped"))
        _interface[self._STAT_TX_ERRORS] = self._read(os.path.join(_path, "tx_errors"))
        _interface[self._STAT_TX_FIFO_ERRORS] = self._read(os.path.join(_path, "tx_fifo_errors"))
        _interface[self._STAT_TX_HEARTBEAT_ERRORS] = self._read(os.path.join(_path, "tx_heartbeat_errors"))
        _interface[self._STAT_TX_PACKETS] = self._read(os.path.join(_path, "tx_packets"))
        _interface[self._STAT_TX_WINDOW_ERRORS] = self._read(os.path.join(_path, "tx_window_errors"))

        return _interface

    @staticmethod
    def _read(filename: str) -> typing.Optional[str]:
        try:
            with open(filename, 'r') as f:
                _data = f.read().strip()
        except OSError:
            _data = None

        return _data

    def get_interfaces(self) -> iter:
        return self._network.keys()

    def get_stat_collisions(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_COLLISIONS)

    def get_stat_multicast(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_MULTICAST)

    def get_stat_rx_bytes(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_BYTES)

    def get_stat_rx_compressed(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_COMPRESSED)

    def get_stat_rx_crc_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_CRC_ERRORS)

    def get_stat_rx_dropped(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_DROPPED)

    def get_stat_rx_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_ERRORS)

    def get_stat_rx_fifo_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_FIFO_ERROR)

    def get_stat_rx_frame_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_FRAME_ERRORS)

    def get_stat_rx_length_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_LENGTH_ERRORS)

    def get_stat_rx_missed_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_MISSED_ERRORS)

    def get_stat_rx_nohandler(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_NOHANDLER)

    def get_stat_rx_over_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_OVER_ERRORS)

    def get_stat_rx_packets(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_RX_PACKETS)

    def get_stat_tx_aborted_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_ABORTED_ERRORS)

    def get_stat_tx_bytes(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_BYTES)

    def get_stat_tx_carrier_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_CARRIER_ERRORS)

    def get_stat_tx_compressed(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_COMPRESSED)

    def get_stat_tx_dropped(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_DROPPED)

    def get_stat_tx_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_ERRORS)

    def get_stat_tx_fifo_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_FIFO_ERRORS)

    def get_stat_tx_heartbeat_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_HEARTBEAT_ERRORS)

    def get_stat_tx_packets(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_PACKETS)

    def get_stat_tx_window_errors(self, interface: str) -> str:
        return self._get_value(interface, self._STAT_TX_WINDOW_ERRORS)

    def _get_value(self, interface: str, item: str) -> typing.Optional[str]:
        try:
            return self._network[interface][item]
        except KeyError:
            return None
