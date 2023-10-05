import os
import time
import csv
import board
import adafruit_dht
from datetime import datetime
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Log temperature and humidity data to a CSV file.')
    parser.add_argument('--sensor_pins', nargs='*', type=int, default=[2],
                        help='GPIO pin numbers where the sensors are connected [default: 2].')
    parser.add_argument('--filename', type=str, default=None,
                        help='Name of the CSV file to log data.')
    parser.add_argument('--frequency', type=int, default=10,
                        help='Frequency in seconds [default: 10].')
    return parser.parse_args()

def initialize_sensors(sensor_pins):
    # Convert pin numbers to board pin objects
    pin_objects = [getattr(board, f'D{pin}') for pin in sensor_pins]
    # Initialize DHT devices
    return [adafruit_dht.DHT11(pin) for pin in pin_objects]

def generate_filename():
    now = datetime.now().strftime('%y%m%d_%H-%M-%S')
    return os.path.join('logs', f'{now}-log.csv')

def log_data(filename, data):
    # Ensure the /logs subfolder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Check if CSV file exists, if not, create it with headers
    try:
        with open(filename, 'x', newline='') as file:
            writer = csv.writer(file)
            headers = ['timestamp']
            # Derive the number of sensor pairs from the length of the data array
            num_sensors = (len(data) - 1) // 2
            for i in range(1, num_sensors + 1):
                headers.extend([f'temperature_{i}', f'humidity_{i}'])
            writer.writerow(headers)
    except FileExistsError:
        pass

    # Append data to CSV file
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    args = parse_args()
    sensor_pins = args.sensor_pins
    filename = args.filename
    frequency = args.frequency
    dht_devices = initialize_sensors(sensor_pins)

    if filename is None:
        filename = generate_filename()  # Generate filename based on current date and time if not provided

    while True:
        data = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]  # Start with timestamp
        output_str = ''
        for idx, dht_device in enumerate(dht_devices, 1):
            try:
                temperature = dht_device.temperature
                humidity = dht_device.humidity
                if humidity is not None and temperature is not None:
                    data.extend([temperature, humidity])
                    output_str += f'T{idx}: {temperature:.1f}°C;  H{idx}: {humidity:.1f}%; '
                else:
                    print(f"Failed to retrieve data from sensor {idx}")
                    data.extend([None, None])  # Append None for missing data
                    output_str += f'T{idx}: None;  H{idx}: None; '
            except RuntimeError as error:
                print(error.args[0])
                data.extend([None, None])  # Append None for missing data
                output_str += f'T{idx}: None;  H{idx}: None; '
        print(output_str.strip())  # Print the formatted string
        log_data(filename, data)
        time.sleep(frequency)  # Wait for <frequency> seconds before the next reading

if __name__ == '__main__':
    main()
