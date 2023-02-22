# Devloped By: Tyler Chang
"""Main Module"""

from devices.microphone import microphone
from file import file


def main():
    """The main function that opens an ini file and gets the attributes.
    """
    config = file('config.ini')
    device_type = config.get_from_config('SETTINGS', 'device_type')

    mic = microphone(device_type)
    print(mic.get_device())


if __name__ == '__main__':
    main()
