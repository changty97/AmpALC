# Developed By: Tyler Chang
"""Module for devices."""

# pylint: disable=W0511

from file import file


class device():
    """Base class for devices.
    """

    def __init__(self, device_type):
        self.device_type = device_type
        self.file = file()

        self.file.set_command(volume='12')

    def get_device(self):
        """Returns the device as a string.
        """
        return self.device_type
