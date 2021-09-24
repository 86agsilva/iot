def lertemp():
    import dht
    import machine
    from lcd import tela
    from envia import enviadados
    import time
    from cronometro import countdown
    
    r = machine.Pin(2,machine.Pin.OUT)
    d=dht.DHT11(machine.Pin(4))
    d.measure()
    temp = d.temperature()
    umid = d.humidity()
    temp1 = str(d.temperature())
    umid1 = str(d.humidity())
    if temp > 30 or umid >70:
        tela(("TEMPERATURA: "+temp1+"C"),("    UMIDADE: "+umid1+"%"),"RELAY ON","ENVIANDO DADOS")
        env = enviadados(temp1,umid1)
        r.value(1)
        tela("ENVIO DE DADOS","REALIZADO COM","SUCESSO.","RELAY LIGADO")
        time.sleep(5)
        countdown(temp1,umid1,300)
    else:
        tela(("TEMPERATURA: "+temp1+"C"),("    UMIDADE: "+umid1+"%"),"RELAY OFF","ENVIANDO DADOS")
        env = enviadados(temp1,umid1)
        r.value(0)
        tela("ENVIO DE DADOS","REALIZADO COM","SUCESSO.","RELAY DESLIGADO")
        time.sleep(5)
        countdown(temp1,umid1,300)