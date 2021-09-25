from lcd import *
import time
from wifilib import conecta
import sys
import machine
import lerdados
from cronometro import countdown
from envia import enviadados
from relay import *

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
        temp = lerdados.tempnow()
        umid = lerdados.umidnow()
        r = relay(temp, umid)
        enviadados(temp,umid,r)
        station.disconnect()
        tela("A WIFI FOI","DESATIVADA","AGUARDE NOVA","LEITURA DE DADOS")
        time.sleep(5)
        countdown(temp,umid,300)
except:
    tela("OCORREU","UM ERRO","INESPERADO","REINICIANDO...")
    time.sleep(10)
    machine.reset()

