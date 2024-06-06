"""
Script to check battery percentage and power source.
Send a notification if the battery percentage is below the minimum threshold
or above the maximum threshold.

Example:
    $ python main.py
"""

import argparse
from battery_handler import BatteryHandler
from logger import BatteryLogger
from notification import Notifier


def parse_arguments():
    """Parse command-line arguments for configuration options."""
    parser = argparse.ArgumentParser(description="Battery monitoring script")
    parser.add_argument(
        "--min-percentage",
        type=int,
        default=35,
        help="Minimum battery percentage to trigger low battery warning",
    )
    parser.add_argument(
        "--max-percentage",
        type=int,
        default=75,
        help="Maximum battery percentage to trigger high battery warning",
    )
    parser.add_argument(
        "--notification-title",
        type=str,
        default="Battery Warning",
        help="Title of the notification",
    )
    parser.add_argument(
        "--notification-sound",
        type=str,
        default="default",
        help="Sound of the notification",
    )
    return parser.parse_args()


def setup():
    """Set up the application based on parsed arguments."""
    return parse_arguments()


def main():
    """Main function to check battery percentage and power source"""
    args = setup()

    logger = BatteryLogger()
    notifier = Notifier(title=args.notification_title, sound=args.notification_sound)
    handler = BatteryHandler(
        notifier, min_percentage=args.min_percentage, max_percentage=args.max_percentage
    )

    logger.log_battery_info()
    handler.handle_low_battery_percentage()
    handler.handle_high_battery_percentage()


if __name__ == "__main__":
    main()
