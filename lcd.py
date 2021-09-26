def tela(t1,t2,t3,t4):
    import ssd1306
    from machine import I2C, Pin

    t1 = str(t1)
    t2 = str(t2)
    t3 = str(t3)
    t4 = str(t4)
    
    scl = Pin(22)
    sda = Pin(21)
    i2c = I2C(scl=scl, sda=sda)

    oled = ssd1306.SSD1306_I2C(128, 32 , i2c)
    oled.text(t1, 0, 0)
    oled.show()
    oled.text(t2,0,8)
    oled.show()
    oled.text(t3,0,16)
    oled.show()
    oled.text(t4,0,24)
    oled.show()
    
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
    
def tela2(t1):
    import ssd1306
    from machine import I2C, Pin

    t1 = str(t1)
    
    scl = Pin(22)
    sda = Pin(21)
    i2c = I2C(scl=scl, sda=sda)

    oled = ssd1306.SSD1306_I2C(128, 32 , i2c)
    oled.text(t1, 0, 0)
    oled.show()
    oled.show()
    oled.text("Reiniciando...",0,24)
