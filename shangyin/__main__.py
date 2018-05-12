from shangyin.interface import display, rfid, speaker
import shangyin.storage as storage
import shangyin.server as server
import time

# Connect database and RFID reader
db = storage.Storage()
reader = rfid.init()

# Start up the statistics server
srun = server.ServerRunner()
srun.assign_db(db)
srun.start()

# Init database if needed
db.setup()

# Init LCD display
disp = display.Display()

# Init speaker
speaker.init()

# Periodically update display
disp_upd = display.DisplayUpdater()
disp_upd.set_disp(disp)
disp_upd.start()

disp.set(0, 'shangyin v0.1-a')
disp.set(1, 'Hello! The machine is ready for some work. Tap your card now.')
speaker.beep(0.2, 250)

while True:
    # Read card
    card = rfid.read_card(reader)

    # Display a debug message
    disp.set(1, 'Card: {}'.format(card))
    print('Card with hash {} tapped.'.format(card))

    # Sync the card with db
    cardrow = db.get_by_id('card', card, 'id, user_id')

    if cardrow == None:
        db.create_card(card)

    # Log a coffee for this card
    db.create_coffee(card)
    
    # Sound feedback
    speaker.beep(0.1, 400)
    speaker.beep(0.1, 700)

    # Hold the message for a while
    time.sleep(2)

    # Back to standby display
    disp.set(1, 'Hello! The machine is ready for some work. Tap your card now.')
    