import dht
import machine    
r = machine.Pin(2,machine.Pin.OUT)
d=dht.DHT11(machine.Pin(4))
def leituraja():
    d.measure()
    umid = d.humidity()
    temp = d.temperature()
    return umid, temp