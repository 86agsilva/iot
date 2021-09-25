import machine
r = machine.Pin(2, machine.Pin.OUT)
def relay(temp, umid):
    if temp > 30 or umid > 70:
        r.value(1)
        return 1
    else:
        r.value(0)
        return 0