import utime

from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.putstr("It Works!\nSecond line!\nThird Line!\nFourth Line!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        lcd.clear()
        lcd.putstr("%7d" % (utime.time() // 1000))
        if count % 10 == 0:
            print("Turning cursor on")
            lcd.show_cursor()
        if count % 10 == 1:
            print("Turning cursor off")
            lcd.hide_cursor()
        if count % 10 == 2:
            print("Turning blink cursor on")
            lcd.blink_cursor_on()
        if count % 10 == 3:
            print("Turning blink cursor off")
            lcd.blink_cursor_off()                    
        if count % 10 == 4:
            print("Turning backlight off")
            lcd.backlight_off()
        if count % 10 == 5:
            print("Turning backlight on")
            lcd.backlight_on()
        if count % 10 == 6:
            print("Turning display off")
            lcd.display_off()
        if count % 10 == 7:
            print("Turning display on")
            lcd.display_on()
        if count % 10 == 8:
            print("Filling display")
            lcd.clear()
            string = ""
            for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
                string += chr(x)
            lcd.putstr(string)
        count += 1
        utime.sleep(2)

#if __name__ == "__main__":
test_main()