# Devloped By: Tyler Chang
"""Module for a file."""

import configparser


class file():
    """Class for an ini file.
    """

    def __init__(self):
        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser()
        self.command = ''
        try:
            self.config.read(self.config_file)
        except FileNotFoundError:
            print(f'ERROR: Could not open {self.config_file}.')

    def set_command(self, volume):
        """Returns a volume value from an ini file.
        """
        self.command = self.config.get('SETTINGS', 'volume_command') + volume

    def get_device_type(self):
        """Returns a device type value from an ini file.
        """
        return self.config.get('SETTINGS', 'device_type')

    def get_default_volume(self):
        """Returns a default volume value from an ini file.
        """
        volume = self.config.get('SETTINGS', 'default_volume')
        return self.set_command(volume)

    def get_volume_command(self):
        """Returns a volume command value from an ini file.
        """
        return self.config.get('SETTINGS', 'volume_command')
