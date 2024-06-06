"""
BatteryHandler class to handle battery percentage and power source.

This class inherits from BatteryInfo and provides methods to handle battery
conditions based on specified thresholds. If the battery percentage is below
the minimum threshold, it sends a low battery notification. If the battery
percentage is above the maximum threshold, it sends a high battery notification.
"""

import logging
from battery import BatteryInfo
from notification import Notifier


class BatteryHandler(BatteryInfo):
    """
    A class to handle battery percentage and power source notifications.

    This class inherits from BatteryInfo and provides methods to handle battery
    conditions based on specified thresholds. If the battery percentage is below
    the minimum threshold, it sends a low battery notification. If the battery
    percentage is above the maximum threshold, it sends a high battery
    notification.
    """

    def __init__(
        self, notifier: Notifier, min_percentage: int = 35, max_percentage: int = 75
    ):
        """
        Initializes the BatteryHandler with the specified notifier and
        thresholds.

        Args:
            notifier (Notifier): An instance of the Notifier class to send
                                 notifications.
            min_percentage (int): The minimum battery percentage threshold.
                                  Defaults to 35.
            max_percentage (int): The maximum battery percentage threshold.
                                  Defaults to 75.
        """
        super().__init__()
        self.notifier = notifier
        self.min_percentage = min_percentage
        self.max_percentage = max_percentage

    def handle_low_battery_percentage(self):
        """
        Sends a notification if the battery percentage is below the minimum
        threshold.
        """
        battery_percentage = self.get_battery_percentage()
        power_source = self.get_power_source()

        if self._is_low_battery(battery_percentage, power_source):
            message = f"Your MacBook battery is low: {battery_percentage}%. \nPlease plug in your charger."
            self.notifier.send_notification(message)

    def handle_high_battery_percentage(self):
        """
        Sends a notification if the battery percentage is above the maximum
        threshold.
        """
        battery_percentage = self.get_battery_percentage()
        power_source = self.get_power_source()

        if self._is_high_battery(battery_percentage, power_source):
            message = f"Your MacBook battery is charged: {battery_percentage}%. \nYou can unplug your charger."
            self.notifier.send_notification(message)

    def _is_low_battery(self, battery_percentage: int, power_source: str) -> bool:
        """
        Checks if the battery percentage is below the minimum threshold and
        the power source is battery.

        Args:
            battery_percentage (int): The current battery percentage.
            power_source (str): The current power source.

        Returns:
            bool: True if the battery percentage is below the minimum threshold
                  and the power source is battery, False otherwise.
        """
        if battery_percentage is None or power_source is None:
            logging.warning("Battery percentage or power source is not available")
            return False
        return (
            battery_percentage < self.min_percentage and power_source == "Battery Power"
        )

    def _is_high_battery(self, battery_percentage: int, power_source: str) -> bool:
        """
        Checks if the battery percentage is above the maximum threshold and
        the power source is AC.

        Args:
            battery_percentage (int): The current battery percentage.
            power_source (str): The current power source.

        Returns:
            bool: True if the battery percentage is above the maximum threshold
                  and the power source is AC, False otherwise.
        """
        if battery_percentage is None or power_source is None:
            logging.warning("Battery percentage or power source is not available")
            return False
        return battery_percentage > self.max_percentage and power_source == "AC Power"
