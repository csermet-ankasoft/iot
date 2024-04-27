from rpi_lcd import LCD
from time import sleep

lcd = LCD()

def writeLCD(text1, text2):
    lcd.text(text1, 1)
    lcd.text(text2, 2)

def clearLCD():
    lcd.clear()

def status():
    lcd.text('LCD Status: OK', 1)