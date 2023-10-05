# Heatbox: A Temperature Testing Kit by Albeit Studio

Heatbox is a temperature and humidity logging tool devised by Albeit Studio. Its core purpose is to evaluate the performance of different materials in maintaining temperature and humidity levels. The testing process involves creating boxes out of diverse materials, fitting them with DHT11 temperature sensors, and concurrently assessing up to three boxes to gauge their performance.

## Setup

1. **Hardware Requirements:**

    - Raspberry Pi (any model with GPIO pins)
    - DHT11 Temperature and Humidity Sensors
    - Breadboard and jumper wires

2. **Software Requirements:**

    - Python 3.x
    - Adafruit DHT Library
    - Adafruit Blinka Library (for interfacing with the GPIO pins)

3. **Installation:**
    - Install the required libraries using pip:
    ```bash
    pip install adafruit-circuitpython-dht adafruit-blinka
    ```

## Usage

1. Clone this repository or copy the code below into a file named `heatbox.py`.
2. Connect the DHT11 sensors to the GPIO pins on the Raspberry Pi.
3. Run the program using the command below, specifying the GPIO pin numbers, filename, and data logging frequency in seconds as needed:
    ```bash
    python heatbox.py --sensor_pins 2 3 4 --filename temp_log.csv --frequency 10
    ```

## Output

The program will generate a CSV file named `temp_log.csv` in a subdirectory named `logs`. Each row in the CSV file contains a timestamp, followed by temperature and humidity readings from each sensor:

```
timestamp, temperature_1, humidity_1, temperature_2, humidity_2, temperature_3, humidity_3
2023-09-25 14:30:00, 20.0, 50.0, 20.1, 49.9, 19.9, 50.1
...
```

The program also prints the temperature and humidity data to the console in the following format:

```
T1: 20.0°C;  H1: 50.0%; T2: 20.1°C;  H2: 49.9%; T3: 19.9°C;  H3: 50.1%;
```

---

Crafted with ❤️ by Albeit Studio
