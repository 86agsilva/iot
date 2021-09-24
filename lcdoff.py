def desligatela():
    import ssd1306
    from machine import I2C, Pin
   
    scl = Pin(22)
    sda = Pin(21)
    i2c = I2C(scl=scl, sda=sda)

    oled = ssd1306.SSD1306_I2C(128, 32 , i2c)
    oled.fill(1)
    oled.show()
    oled.poweroff()