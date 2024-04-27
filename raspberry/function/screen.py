from rpi_lcd import LCD
from time import sleep

lcd = LCD()

def writeLCD(text1, text2):
    lcd.text('Hello World!', 1)
    lcd.text('Raspberry Pi', 2)

def clearLCD():
    lcd.clear()

def status():
    lcd.text('LCD Status: OK', 1)