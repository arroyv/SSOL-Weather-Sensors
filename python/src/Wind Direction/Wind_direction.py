import minimalmodbus

mb_address = 1

sensor = minimalmodbus.Instrument('/dev/ttyS0', mb_address)

sensor.serial.baudrate = 4800
sensor.serial.bytesize = 8
sensor.serial.parity = minimalmodbus.serial.PARITY_NONE
sensor.serial.stopbits = 1
sensor.serial.timeout = 0.5
sensor.mode = minimalmodbus.MODE_RTU

# sensor.clear_buffers_before_each_transaction = True
# sensor.close_port_after_each_call = True

print("")
print("Requesting Data From Sensor...")


# Example of SINGLE Registers:
# sensor.read_registers(REGISTER ADDRESS, NUMBER OF DECIMALS, FUNCTION CODE, IS VALUE SIGNED OR UNSIGNED (TRUE OR FASLSE))

# Example of MULTIPLE Registers
# sensor.read_registers(REGISTER START ADDRESS, NUMBER OF REGISTERS TO READ, FUNCTION CODE)
while(1):
    data =  sensor.read_registers(0,2,3)

    # print(type(data[0])) 
    print("")
    print("Direction:")
    print(f"Raw Data is {data}")
    position = data[0]
    str_dir = "Invalid"
    if (position == 0 or position == 8):
        str_dir = "North"
    elif(position == 1):
        str_dir = "Northeast"
    elif(position == 2):
        str_dir = "East"
    elif (position == 3):
        str_dir = "Southeast"
    elif (position == 4): 
        str_dir = "South"
    elif (position == 5):
        str_dir = "Southwest"
    elif (position == 6):
        str_dir = "West"
    elif (position == 7):
        str_dir = "Northwest"

    # match position:
    #     case 0:
    #         str_dir = "North"
    #     case 1:
    #         str_dir = "Northeast"
    #     case 2:
    #         str_dir = "East"
    #     case 3:
    #         str_dir = "Southeast"
    #     case 4: 
    #         str_dir = "South"
    #     case 5:
    #         str_dir = "Southwest"
    #     case 6:
    #         str_dir = "West"
    #     case 7:
    #         str_dir = "Northwest"
    #     case default:
    #         str_dir = "Invalid"
    
    angle = data[1]
    print(f"Position: {position}")
    print(f"Direction: {str_dir}")
    print(f"Angle: {angle}°")
