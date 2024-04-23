import psutil
import pync
import time

def check_battery_and_notify():
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        if percent in [100, 2, 1]:
            pync.notify(f"Your MacBook is on {percent}% battery.", title="Low Battery Warning")
    else:
        print("Could not access battery status")

if __name__ == "__main__":
    check_battery_and_notify()
