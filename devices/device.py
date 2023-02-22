# Developed By: Tyler Chang
"""Module for devices."""

# pylint: disable=W0511


class device():
    """Base class for devices.
    """

    def __init__(self, device_type):
        self.device_type = device_type

    def get_device(self):
        """Returns the device as a string.
        """
        return self.device_type

    # TODO: Method to get amplifier volume control commands
    # TODO: Method adjust volume accordingly
