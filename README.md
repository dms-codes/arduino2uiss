# Serial Data Logger Arduino to UISS software

This Python script is a simple serial data logger that reads data from a serial port, processes it, and logs it to a text file. It's designed to work with a device connected to a serial port (e.g., an Arduino) that sends data in a specific format.

## Requirements

Before you begin, make sure you have the following:

- Python installed on your system.
- A device (e.g., Arduino) connected to a serial port (COM6 in this example).
- The device should send data in a specific format (temperature and humidity values).
- You may need to install the `pyserial` library if it's not already installed. You can install it using the following command:

   ```bash
   pip install pyserial
   ```

## Usage

1. Clone this repository or download the script.

2. Open the script and modify the serial port and baud rate settings as needed. In this example, the serial port is set to 'COM6' and the baud rate is 9600.

3. Run the script using the following command:

   ```bash
   python serial_data_logger.py
   ```

4. The script will continuously read data from the specified serial port, extract temperature and humidity values, and create a formatted result string.

5. The result string is logged to a text file named "data.txt" in the same directory as the script.

## Example

Here's an example of what the script's output might look like in "data.txt":

```plaintext
!0619.80S/10648.25E_000/000g000t025h059DMS
!0619.80S/10648.25E_000/000g000t026h060DMS
!0619.80S/10648.25E_000/000g000t026h061DMS
```

## Note

- Ensure that the connected device is sending data in the expected format (temperature and humidity values).
- This script continuously logs data, so be cautious about running it for extended periods as it will keep appending data to "data.txt."

Feel free to customize and extend the script to meet your specific requirements or integrate it into other projects as necessary.
