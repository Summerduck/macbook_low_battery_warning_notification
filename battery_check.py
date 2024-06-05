import subprocess


def get_battery_percentage():
    try:
        # Get battery information using pmset
        battery_info = subprocess.check_output(["pmset", "-g", "batt"]).decode("utf-8")

        # Extract battery percentage from the output
        battery_percentage = int(battery_info.split("\t")[1].split("%")[0])

        return battery_percentage
    except Exception as e:
        print(f"An error occurred while getting battery percentage: {e}")
        return None


def get_power_source():
    try:
        # Get battery information using pmset
        battery_info = subprocess.check_output(["pmset", "-g", "batt"]).decode("utf-8")
        power_source = battery_info.split("\n")[0]

        return power_source
    except Exception as e:
        print(f"An error occurred while getting battery info: {e}")
        return None

    # Now drawing from 'Battery Power'
    # Now drawing from 'AC Power'


def send_notification(message):
    try:
        # Send a notification using osascript
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display notification "{message}" with title "Low Battery Warning" sound name "default"',
            ]
        )
    except Exception as e:
        print(f"An error occurred while sending notification: {e}")


def main():
    power_source = get_power_source()
    print(f"power_source: {power_source}")

    battery_percentage = get_battery_percentage()
    print(f"battery_percentage: {battery_percentage}%")

    if battery_percentage < 35 and power_source == "Now drawing from 'Battery Power'":
        send_notification(f"Battery is low: {battery_percentage}% remaining")

    if battery_percentage > 80 and power_source == "Now drawing from 'AC Power'":
        send_notification(f"Battery is high: {battery_percentage}% remaining")
    else:
        print("Could not retrieve battery percentage")


if __name__ == "__main__":
    main()


# */5 * * * * /usr/local/bin/python3 /Users/dariasamardak/Documents/macbook_low_battery_warning_notification/battery_check.py
