import dht
import machine    
r = machine.Pin(2,machine.Pin.OUT)
d=dht.DHT11(machine.Pin(4))
d.measure()

def umidnow():
    return(str(d.humidity()))

def tempnow():
    return(str(d.temperature()))