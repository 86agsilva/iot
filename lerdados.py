import dht
import machine    
r = machine.Pin(2,machine.Pin.OUT)
d=dht.DHT11(machine.Pin(4))
d.measure()

def umidnow():
    return d.humidity()

def tempnow():
    return d.temperature()