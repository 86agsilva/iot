import time
from lcd import tela

def countdown(temp,umid,num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        tela(("TEMPERATURA: "+str(temp)+"C"), ("UMIDADE: "+str(umid)+"%")," ","        "+min_sec_format)
        time.sleep(1)
        num_of_secs -= 1