import serial
ser = serial.Serial('COM7', 
    baudrate=115200, 
    parity=serial.PARITY_NONE, 
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS, 
    timeout=1
)

data = []
try:
    while True:
        try:
            while len(data) < 20:
                binary = ser.read(1)  # Read one byte at a time
                if binary:  # Avoid appending empty data
                    hex_value = binary.hex()
                    data.append(hex_value)
                
        except KeyboardInterrupt:
            ser.close()
            break

        print(len(data))
        print(data)
        data = []  # Reset the data list after each 20 bytes

except KeyboardInterrupt:
    ser.close()

print("bye")
