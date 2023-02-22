# Devloped By: Tyler Chang
"""Main Module"""

from devices.microphone import microphone
from devices.capture_card import capture_card
from file import file


def main():
    """The main function that opens an ini file and gets the attributes.
    """
    config = file('config.ini')
    device_type = config.get_from_config('SETTINGS', 'device_type')

    if device_type == 'microphone':
        mic = microphone(device_type)
        print(mic.get_device())
    else:
        cap_card = capture_card(device_type)
        print(cap_card.get_device())


if __name__ == '__main__':
    main()
