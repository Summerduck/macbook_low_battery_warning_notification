import subprocess

def get_battery_percentage():
    try:
        # Get battery information using pmset
        battery_info = subprocess.check_output(['pmset', '-g', 'batt']).decode('utf-8')
        
        # Extract battery percentage from the output
        battery_percentage = int(battery_info.split('\t')[1].split('%')[0])
        
        return battery_percentage
    except Exception as e:
        print(f"An error occurred while getting battery percentage: {e}")
        return None

def send_notification(message):
    try:
        # Send a notification using osascript
        subprocess.run(
            ['osascript', '-e', 
             f'display notification "{message}" with title "Low Battery Warning" sound name "default"']
        )
    except Exception as e:
        print(f"An error occurred while sending notification: {e}")

def main():
    battery_percentage = get_battery_percentage()
    
    if battery_percentage is not None:
        print(f"Battery percentage: {battery_percentage}%")
        
        if battery_percentage < 35:
            send_notification(f"Battery is low: {battery_percentage}% remaining")
    else:
        print("Could not retrieve battery percentage")

if __name__ == "__main__":
    main()


# */10 * * * * /usr/local/bin/python3 /Users/dariasamardak/Documents/macbook_low_battery_warning_notification/battery_check.py