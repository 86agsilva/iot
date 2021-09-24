from lcd import tela
from lcdoff import desligatela
import time
from wifilib import conecta
import sys
import machine
from lertemp import lertemp

msg = tela("LIGANDO O","SISTEMA DE","LEITURA DE","DADOS TEMP/UMID")

try:
    while True:
        station = conecta('MEO-5D2550','73aa3201a9')
        if not station.isconnected():
            tela("A WIFI","NAO ESTA","CONECTADA","REVISAR WIFI")
            time.sleep(3)
            tela("SEM WIFI NAO","E POSSIVEL","ENVIAR DADOS","DESLIGANDO")
            time.sleep(3)
            desligatela()
            sys.exit()  
            
        tela("A WIFI ESTA","CONECTADA","","AGUARDE LEITURAS")
        lertemp()
        station.disconnect()
except:
    tela("OCORREU","UM ERRO","INESPERADO","REINICIANDO...")
    time.sleep(10)
    machine.reset()
    #teste
