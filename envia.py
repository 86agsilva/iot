def enviadados(temp, umid, r):
    import urequests
    urequests.get("http://api.thingspeak.com/update?api_key=Y83THQQBP8CGOJHN&field1="+str(temp)+"&field2="+str(umid)+"&field3="+str(r))