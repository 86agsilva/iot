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
            msg = tela("A WIFI","NAO ESTA","CONECTADA","REVISAR WIFI")
            time.sleep(3)
            msg = tela("SEM WIFI NAO","E POSSIVEL","ENVIAR DADOS","DESLIGANDO")
            time.sleep(3)
            msg = desligatela()
            sys.exit()  
            
        msg = tela("A WIFI ESTA","CONECTADA","","AGUARDE LEITURAS")
        time.sleep(5)
        if station.isconnected():
            lertemp()
except:
    tela("OCORREU","UM ERRO","INESPERADO","REINICIANDO...")
    time.sleep(10)
    machine.reset()
    #teste
