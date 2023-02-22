# Devloped By: Tyler Chang
"""Module for a file."""

import configparser


class file():
    """Class for an ini file.
    """

    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.config_file)
        except FileNotFoundError:
            print(f'ERROR: Could not open {self.config_file}.')

    def get_from_config(self, section, key):
        """Returns any key from an ini file.
            Variables:
                section: Section of a ini file.
                key: Key of an ini file.
        """
        return self.config.get(section, key)
