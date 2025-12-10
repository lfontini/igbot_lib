"""
Base classes and interfaces for network devices.

This module defines the abstract Device interface used as a contract
for Cisco, MikroTik, and other network drivers.
"""

from abc import ABC, abstractmethod


class Device:
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    @abstractmethod
    def connect(self):
        """Connect to the device."""
        pass

    @abstractmethod
    def run(self, command):
        """Run a command on the device."""
        pass

    @abstractmethod
    def close(self):
        """Close the connection to the device."""
        pass
