from lcd import tela
from lcdoff import desligatela
import dht
import machine
import time
from wifilib import conecta
import sys
from envia import enviadados


d=dht.DHT11(machine.Pin(4))
msg = tela("LIGANDO O","SISTEMA DE","LEITURA DE","DADOS TEMP/UMID")

station = conecta('MEO-5D2550','73aa3201a9')
if not station.isconnected():
    msg = tela("A WIFI","NAO ESTA","CONECTADA","REVISAR WIFI")
    time.sleep(3)
    msg = tela("SEM WIFI NAO","É POSSIVEL","ENVIAR DADOS","DESLIGANDO")
    time.sleep(3)
    msg = desligatela()
    sys.exit()  
    
msg = tela("A WIFI ESTA","CONECTADA","","AGUARDE LEITURAS")
time.sleep(5)

while True:
    r = machine.Pin(2,machine.Pin.OUT)
    d.measure()
    temp = d.temperature()
    umid = d.humidity()
    temp1 = str(d.temperature())
    umid1 = str(d.humidity())
    if temp > 30 or umid >70:
        teste = tela(("TEMPERATURA: "+temp1+"C"),("    UMIDADE: "+umid1+"%"),"RELAY ON","ENVIANDO DADOS")
        env = enviadados(temp1,umid1)
        r.value(1)
    else:
        teste = tela(("TEMPERATURA: "+temp1+"C"),("    UMIDADE: "+umid1+"%"),"RELAY OFF","ENVIANDO DADOS")
        env = enviadados(temp1,umid1)
        r.value(0)
        
    time.sleep(600)
    
