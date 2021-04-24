import serial
import time

Gloves          = serial.Serial()
Gloves.port     = 'COM4'
Gloves.baudrate = 9600
Gloves.parity   = 'N'
Gloves.stopbits = 1
Gloves.bytesize = 8

try:
    Gloves.open()
    print("\nSelamat Datang Di Program Pembaca Data Serial")
    print("\nBerikut Konfigurasi Sambungan Serial Anda")
    print("Port     : ", Gloves.port)
    print("Baudrate : ", Gloves.baudrate)
    print("Parity   : ", Gloves.parity)
    print("Stopbits : ", Gloves.stopbits)
    print("Bytesize : ", Gloves.bytesize, "\n")

except serial.SerialException:
    print("Hubungan Gagal Pada Port " + Gloves.port)

while True:
    try:
        data = Gloves.readline().decode("utf-8").rstrip().strip("DAT")
        print(data)
        data = data.split(":")
        print()
        print (data)
        for i in range(1,18):
            data[i] = data[i].split("[")
            data[i] = data[i][0].strip("]")

        for i in range (1,18):
            print(data[i])

        time.sleep(10)
    except:
        pass
