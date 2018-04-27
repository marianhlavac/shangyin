from shangyin.interface import display, rfid
import time

# Init database if needed
# if not storage.initialized():
#     storage.initialize()

# Init LCD display
lcd = display.Display(None)

lcd.set(0, 'shangyin v0.1 T')
lcd.set(1, 'Hello! The machine is ready for some work. Tap your card now.')

while True:
    if rfid.card_present():
        lcd.set(1, 'Card is present.')

    lcd.update()
    time.sleep(0.25)