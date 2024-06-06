"""
This module provides a class to get battery information of the device.

The BatteryInfo class provides methods to get the battery information,
battery percentage, and power source of the device.
"""

import subprocess
import logging


class BatteryInfo:
    """
    A class to get battery information of the device.

    This class provides methods to retrieve detailed battery information,
    including the battery percentage and power source.
    """

    def __init__(self):
        """
        Initializes the BatteryInfo class and retrieves the initial battery information.
        """
        self.battery_info = self.get_battery_info()

    def get_battery_info(self) -> str:
        """
        Get the battery information of the device and return it as a string.

        Returns:
            str: The raw battery information string.

        Logs:
            Logs an error if the battery information retrieval fails.
        """
        try:
            return subprocess.check_output(["pmset", "-g", "batt"]).decode("utf-8")
        except subprocess.CalledProcessError as e:
            logging.error("Failed to get battery information: %s", e)
            return None

    def get_battery_percentage(self) -> int | None:
        """
        Get the battery percentage of the device and return it as an integer.

        Returns:
            int | None: The battery percentage, or None if retrieval or parsing fails.

        Logs:
            Logs an error if the battery information retrieval or parsing fails.
        """
        try:
            # Extract battery percentage from the output
            battery_percentage = int(self.battery_info.split("\t")[1].split("%")[0])
            return battery_percentage
        except (subprocess.CalledProcessError, ValueError) as e:
            logging.error("Failed to get or parse battery percentage: %s", e)
            return None

    def get_power_source(self) -> str | None:
        """
        Get the power source of the device and return it as a string.

        Returns:
            str | None: The power source, or None if retrieval or parsing fails.

        Logs:
            Logs an error if the power source retrieval or parsing fails.
        """
        try:
            power_source = (
                self.battery_info.split("\n", maxsplit=1)[0]
                .removeprefix("Now drawing from '")
                .removesuffix("'")
            )
            return power_source
        except Exception as e:
            logging.error("An error occurred while getting power source: %s", e)
            return None
