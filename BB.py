import serial

ser = serial.Serial("COM7", 9600, timeout = 1) #Change your port name COM... and your baudrate


while(True):
    uInput = input("Retrieve data? ")
    if uInput == 'F':
        ser.write(b'F')
    if uInput == 'R':
        ser.write(b'R')
    if uInput == 'L':
        ser.write(b'L')
    if uInput == 'B':
        ser.write(b'B')
    if uInput == 'I':
        ser.write(b'I')
    if uInput == 'J':
        ser.write(b'J')
    if uInput == 'K':
        ser.write(b'K')
    if uInput == 'M':
        ser.write(b'M')
    if uInput == 'T':
        ser.write(b'T')
    if uInput == 'P':
        ser.write(b'P')
    if uInput == 'O':
        ser.write(b'O')
    if uInput == 'S':
        ser.write(b'S')
