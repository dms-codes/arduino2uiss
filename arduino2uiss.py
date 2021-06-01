def main():
    import serial
    import time
    import math

    while True:
        ser = serial.Serial('COM6', 9600)
        b = ser.readline()  # read a byte string
        string_n = b.decode()  # decode byte string into Unicode
        res = string_n.rstrip()
        ser.close()
        humi = res.split("t")[0][1:]
        temp = res.split("t")[1]
        if int(temp)<100:
            temp = "0"+temp
        print(temp)
        result = "!0619.80S/10648.25E_000/000g000t{}h{}DMS".format(temp,humi)
        f = open("data.txt","w")
        f.write(result)
        print(result)

if __name__ == '__main__':
    main()
