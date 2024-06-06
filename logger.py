"""
This module contains the BatteryLogger class which logs battery information.

The BatteryLogger class is used for debugging purposes and provides methods to
log the power source and battery percentage of the device.
"""

import logging
from battery import BatteryInfo


class BatteryLogger:
    """
    A class to log battery information.

    This class sets up logging and logs detailed battery information, including
    the power source and battery percentage.
    """

    def __init__(self):
        """
        Initializes the BatteryLogger with an instance of BatteryInfo.
        """
        self.battery_info = BatteryInfo()

    def setup_logging(self):
        """
        Set up logging to output to console.
        """
        logging.basicConfig(level=logging.INFO)

    def get_power_source(self) -> str | None:
        """
        Get the power source of the device.

        Returns:
            str | None: The power source of the device, or None if retrieval fails.
        """
        return self.battery_info.get_power_source()

    def get_battery_percentage(self) -> int | None:
        """
        Get the battery percentage of the device.

        Returns:
            int | None: The battery percentage of the device, or None if retrieval fails.
        """
        return self.battery_info.get_battery_percentage()

    def log_battery_info(self):
        """
        Log battery information, including power source and battery percentage.

        Logs:
            Power source of the device
            Battery percentage of the device
        """
        self.setup_logging()
        logging.info("Power Source: %s", self.get_power_source())
        logging.info("Battery Percentage: %s", self.get_battery_percentage())
