"""
Notification module to send notifications to the user using 'osascript'.

This module provides the Notifier class, which is used to send notifications
to the user on macOS devices.
"""

import subprocess
import logging


class Notifier:
    """
    A class to send notifications to the user.

    This class uses 'osascript' to display notifications on macOS devices.
    """

    def __init__(self, title="Battery Warning", sound="default"):
        """
        Initializes the Notifier with a title and sound.

        Args:
            title (str): The title of the notification. Defaults to "Battery Warning".
            sound (str): The sound to play with the notification. Defaults to "default".
        """
        self.title = title
        self.sound = sound

    def send_notification(self, message: str):
        """
        Send a notification to the user using 'osascript'.

        Args:
            message (str): The message to display in the notification.

        Logs:
            Logs the title and message of the notification if successful.
            Logs an error if the notification sending fails.
        """
        try:
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    f'display notification "{message}" with title "{self.title}" sound name "{self.sound}"',
                ],
                check=False,
            )
            logging.info("Notification title: %s", self.title)
            logging.info("Notification sent: %s", message)
        except subprocess.CalledProcessError as e:
            logging.error("An error occurred while sending notification: %s", e)
