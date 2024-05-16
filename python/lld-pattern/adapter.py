'''
- Structural Patter: Adapter Pattern
(This pattern should be called - Loose Your Hair slowly pattern)

Screw (small) --> Hole(big) [cannot fit]

Screw(small) --> Adapter = Screw(Big)
Screw(Big) --> Hole(big)

Adapter pattern is kind of a strategy pattern? Go figure out how
'''

class UsbCable:
    def __init__(self):
        self.isPlugged = False
    
    def plugUsb(self):
        self.isPlugged = True
    
    def isConnected(self):
        print(self.isPlugged)


class UsbPort:
    def __init__(self):
        self.portAvailable = True
    
    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False
    
    def isOccupied(self):
        print(self.portAvailable)

# UsbCables can plug directly into UsbPorts
usbCable = UsbCable()
usbPort = UsbPort()

usbPort.plug(usbCable)
usbPort.isOccupied()
usbCable.isConnected()

class MicroUsbCable:
    def __init__(self):
        self.isPlugged = False
    
    def plugMicroUsb(self):
        self.isPlugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb() 
    # can override UsbCable.plugUsb() if needed

# microUsbCable --> MicroUsbAdapter --> Port
microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable)
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)

