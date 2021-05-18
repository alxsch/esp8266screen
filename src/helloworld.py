from machine import Pin, I2C
import ssd1306

# from time import sleep

i2c = I2C(scl=Pin(5), sda=Pin(4))

def init_oled():
    oled_width = 64
    oled_height = 48
    oled_64 = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    return oled_64

def diag():
    for i in range(1, 11):
        i += 1

def hello_screen():
    oled_64 = init_oled()
    oled_64.text("Hello", 0, 0)
    oled_64.text("World!", 0, 10)
    oled_64.hline(0, 21, 45, 1)
    oled_64.text("again..", 10 , 40)
    oled_64.pixel(50, 5, 1)
    oled_64.pixel(51, 5, 1)
    oled_64.pixel(52, 6 , 1)
    oled_64.pixel(53, 7 , 1)
    oled_64.pixel(54, 8 , 1)
    oled_64.pixel(55, 9 , 1)
    oled_64.pixel(56, 10 , 1)
    oled_64.pixel(56, 11 , 1)
    oled_64.pixel(56, 12 , 1)
    oled_64.pixel(55, 13 , 1)
    oled_64.pixel(55, 14 , 1)
    oled_64.pixel(54, 15 , 1)
    oled_64.pixel(53, 16 , 1)

    oled_64.show()

hello_screen()
