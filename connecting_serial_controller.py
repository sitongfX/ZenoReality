# import serial

# change the port as necessary by your OS

ser = None


def connect_ser():
    """
        This function allows the user to set up serial connection with the controller
    """
    # ser  =  serial.Serial('/dev/cu.wchusbserial531C0151591', 250000)
    ser = True
    return ser

connect_ser()
