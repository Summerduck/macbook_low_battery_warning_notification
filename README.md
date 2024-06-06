
# MacBook Low Battery Warning Notification

This project provides a Python script that checks the battery level of your MacBook and displays notifications if it falls below or rises above certain thresholds. It helps in managing battery usage efficiently by notifying you when the battery level is too low or too high.

## Features

- Check the battery percentage and power source status.
- Send notifications when the battery percentage falls below a specified minimum threshold.
- Send notifications when the battery percentage rises above a specified maximum threshold.
- Customizable notification sounds and titles.

## Prerequisites

- macOS
- Python 3.x
- Required Python packages (argparse, logging)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/macbook-low-battery-warning.git
   cd macbook-low-battery-warning
   ```

2. **Install required packages**:
   No external packages are required for this project. All necessary libraries are included in the standard Python library.

## Usage

### Running the Script Manually

You can run the script manually with the default thresholds (35% for minimum and 75% for maximum) or specify your own thresholds:

```bash
python3 main.py
```
Customization options. More details on customization can be found in the [Customization](#customization) section.

```bash
python3 main.py --min-percentage=30 --max-percentage=80 --notification-title="Battery Warning" --notification-sound="default"
```


### Setting Up a Cron Job

To run the script automatically at regular intervals, you can set up a cron job. For example, to run the script every 5 minutes:

1. Open your crontab file:
   ```bash
   crontab -e
   ```

2. Add the following line to the crontab file:
   ```bash
   */5 * * * * /usr/bin/python3 /path/to/your/macbook_low_battery_warning_notification/main.py
   ```

   - Replace `/path/to/your/macbook_low_battery_warning_notification/main.py` with the actual path to the `main.py` script.
   
   - Replace `/usr/bin/python3` with the actual path to the Python 3 interpreter. To get the path, run `which python3` in the terminal.

3. Costumization example:
   
   - Customize percentages, notification title, and sound. More details on customization can be found in the [Customization](#customization) section.
   
   ```bash
   */5 * * * * /usr/bin/python3 /path/to/your/macbook_low_battery_warning_notification/main.py --min-percentage=30 --max-percentage=80 --notification-title="Battery Warning" --notification-sound="default"
   ```

5. The script will now run every 5 minutes and send notifications based on the specified thresholds. You can adjust the cron schedule as needed. To change the schedule, modify the `*/5` part of the cron job entry. For example, `*/10` will run the script every 10 minutes.

4. Save and exit the crontab editor.

## Files Description

- **`battery_handler.py`**:
  Handles battery percentage and power source notifications. Inherits from `BatteryInfo` and uses `Notifier` to send notifications based on specified thresholds.

- **`battery.py`**:
  Defines `BatteryInfo` class to retrieve battery information using `ioreg` command in macOS.

- **`logger.py`**:
  Configures logging for the script, setting the logging level and format.

- **`main.py`**:
  Main script to run the battery check. Uses `argparse` for command-line argument handling and initializes `BatteryHandler` with specified thresholds.

- **`notification.py`**:
  Defines `Notifier` class to send macOS notifications using `osascript`.

- **`README.md`**:
  Project documentation.

## Customization

### Notification Sound

The notification sound can be customized by changing the `sound` parameter in the `Notifier` class. Or you can specify the sound using the `--notification-sound` option  in the command line

The available sounds on macOS include:

- `Basso`
- `Blow`
- `Bottle`
- `Frog`
- `Funk`
- `Glass`
- `Hero`
- `Morse`
- `Ping`
- `Pop`
- `Purr`
- `Sosumi`
- `Submarine`
- `Tink`

For example, to use the `Ping` sound:
```python
notifier = Notifier(sound="Ping")
```
To use the `Ping` sound from the command line:
```bash
python3 main.py --notification-sound="Ping"
```
To use the `Ping` sound from cron job:
```bash
*/5 * * * * /usr/bin/python3 /path/to/your/macbook_low_battery_warning_notification/main.py --notification-sound="Ping"

```


### Notification Title

The notification title can be customized by changing the `title` parameter in the `Notifier` class.

or you can specify the title using the `--notification-title` option in the command line or cron job.

### Percentage Thresholds

The minimum and maximum battery percentage thresholds can be customized by changing the `min_percentage` and `max_percentage` parameters in the `BatteryHandler` class.

or you can specify the thresholds using the `--min-percentage` and `--max-percentage` options in the command line or cron job.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
