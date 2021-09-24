def enviadados(temp, umid):
    import urequests
    temp = str(temp)
    umid = str(umid)
    urequests.get(str("http://api.thingspeak.com/update?api_key=Y83THQQBP8CGOJHN&field1="+temp+"&field2="+umid))
