'''
Serial communication with SC300 device.
By Yu Ge
'''

import serial
import serial.tools.list_ports

        
def findCOM():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        print("No COM found.")
    else:
        print("COM available: ")
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])
            
class SC300(object):
    def __init__(self, port, baudrate = 19200, stepLen = .3125):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        
    # You have to initialize the device (open serial port) before usage.
    def initialize(self):
        self.ser.open()
        
    def deInitialize(self):
        self.ser.close()
        
    # Send messages to SC300. cmd is 'VX', 'HX' and so on.
    def sendCmd(self, cmd, *params):
        for i in params:
            cmd=cmd+','+str(i)
        cmd=(cmd+'\r').encode('ascii')
        #print(cmd)
        #print(self.ser.readline())
        self.ser.reset_input_buffer()
        self.ser.write(cmd)
        
    # Read the answer from the device.
    def read(self, dataType = 'string'):
        data=b''
        while True:
            x=self.ser.read(1)
            if x==b'\r':
                break
            else:
                data = data + x
        #print(data)
        data=data.split(b',') # split prefix and data value
        # for different types, we choose different ways to convert it into int. All data in SC300 is represented as string. 
        if data[0]=='ER' or data[0]=='E0' or data[0]=='E1':
            raise ValueError(data[0])
        if len(data)==1:
            return data[0].decode('ascii')
        else:
            if dataType=='string':
                return int(data[1].decode('ascii'))
            elif dataType=='long':
                return int.from_bytes(data[1], byteorder='big', signed=True)

        
    # In following methods, thread is bloked while waiting for response from SC300. 
    # axis = 'X', 'Y' or 'Z'
    def getVersion(self):
        self.sendCmd('VE')
        return self.read()
    
    def getType(self):
        self.sendCmd('TY')
        return self.read()
    
    def getID(self):
        self.sendCmd('ID')
        return self.read()
    
    def setSpeed(self, axis, speed):
        self.sendCmd('V'+axis, speed)
        return self.read()
        
    def setAcc(self, axis, acc):
        self.sendCmd('A'+axis, acc)
        return self.read()
    
    def setInit(self, axis, initSpeed):
        self.sendCmd('F'+axis, initSpeed)
        return self.read()
    
    def stop(self, axis):
        self.sendCmd('SP'+axis)
        return self.read()

    def gohome(self, axis):
        self.sendCmd('H'+axis)
        return self.read()
    
    def move(self, axis, length):
        if length <0:
            self.sendCmd('-'+axis, -length)
        else:
            self.sendCmd('+'+axis, length)
        return self.read()
    
    def moveto(self, axis, pos):
        l=pos-self.getPosition(axis)
        if l==0:
            return self.getPosition(axis)
        return self.move(axis,l)
    
    def getPosition(self, axis):
        self.sendCmd('?'+axis)
        return self.read()
    
    def getSpeed(self, axis):
        self.sendCmd(axis+'V')
        return self.read()
    
    def getInitSpeed(self, axis):
        self.sendCmd(axis+'F')
        return self.read()
    
    def getAcc(self, axis):
        self.sendCmd(axis+'A')
        return self.read()
