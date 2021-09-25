def enviadados(temp, umid, r):
    import urequests
    urequests.get(str("http://api.thingspeak.com/update?api_key=Y83THQQBP8CGOJHN&field1="+temp+"&field2="+umid+"&field3="+r))
