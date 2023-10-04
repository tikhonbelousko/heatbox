import time
import csv
import Adafruit_DHT
from datetime import datetime

# Define the sensor type and the pin it's connected to
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # The sensor is connected to GPIO4 (pin 7)

def log_data(temperature, humidity):
    # Create or open a CSV file named 'temp_humidity_log.csv'
    with open('temp_humidity_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format timestamp
        writer.writerow([timestamp, temperature, humidity])  # Write data to CSV

def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f'Temp={temperature:.1f}*C  Humidity={humidity:.1f}%')
            log_data(temperature, humidity)
        else:
            print("Failed to retrieve data from humidity sensor")
        time.sleep(60)  # Wait for 60 seconds before the next reading

if __name__ == '__main__':
    main()
