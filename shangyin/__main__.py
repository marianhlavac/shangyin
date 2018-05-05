from shangyin.interface import display, rfid, speaker
import shangyin.storage as storage
import time

# Connect database and RFID reader
db = storage.connect()
db_cur = db.cursor()
reader = rfid.init()

# Init database if needed
if storage.need_setup(db_cur):
    storage.setup(db_cur)

# Init LCD display
disp = display.Display()

# Init speaker
speaker.init()

disp.set(0, 'shangyin v0.1 T')
disp.set(1, 'Hello! The machine is ready for some work. Tap your card now.')
disp.update()
speaker.beep(0.5, 200)

while True:
    # When card is tapped
    if reader.irq.is_set:
        card = rfid.read_card(reader)

        # Display a debug message
        disp.set(1, 'Card: {}'.format(card))
        print('Card with hash {} tapped.'.format(card))
        
        # Sound feedback
        speaker.beep(0.1, 250)
        speaker.beep(0.1, 500)

        # Log a coffee for this card
        # storage.log_coffee_to_uid(db_cur, cuid)

        # Update the display
        disp.update()
        time.sleep(2)

    # Back to standby display
    disp.set(1, 'Hello! The machine is ready for some work. Tap your card now.')
    disp.update()
    time.sleep(0.5)