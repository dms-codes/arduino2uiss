import serial
import time

def read_serial_data(port: str, baudrate: int = 9600) -> str:
    """
    Reads data from the specified serial port.

    Args:
        port (str): The serial port to read from (e.g., 'COM6').
        baudrate (int): Baud rate for serial communication. Default is 9600.

    Returns:
        str: The decoded and stripped serial data as a string.
    """
    with serial.Serial(port, baudrate, timeout=1) as ser:
        data = ser.readline().decode().rstrip()
    return data

def format_temperature(temp: str) -> str:
    """
    Formats the temperature string by ensuring it is at least two digits.

    Args:
        temp (str): The temperature string to format.

    Returns:
        str: The formatted temperature string.
    """
    return temp.zfill(3) if int(temp) < 100 else temp

def save_to_file(filename: str, content: str) -> None:
    """
    Saves the provided content to a file.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to be written into the file.
    """
    with open(filename, "w") as f:
        f.write(content)

def main():
    port = 'COM6'

    while True:
        data = read_serial_data(port)
        if "t" in data:  # Ensure the data contains a temperature reading
            humi, temp = data.split("t")
            humi = humi[1:]  # Removing the first character from humidity

            temp = format_temperature(temp)
            result = f"!0619.80S/10648.25E_000/000g000t{temp}h{humi}DMS"
            
            save_to_file("data.txt", result)
            print(result)
        else:
            print("Invalid data format")

if __name__ == '__main__':
    main()
