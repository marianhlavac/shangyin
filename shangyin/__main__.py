from shangyin.interface import display, rfid, speaker
from shangyin.server import server
import shangyin.storage as storage
from subprocess import check_output
import time
import random

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

# Display machine IP address
ip = check_output(['hostname', '--all-ip-addresses'])
disp.set(0, 'shangyin v1.0')
disp.set(1, str(ip))
speaker.play_intro()
time.sleep(5)

# Display default message
disp.set(0, 'Ready.')
disp.set(1, 'Hey, tap your card to log your coffee.')

while True:
    # Read card
    card = rfid.read_card(reader)

    # Tap feedback
    speaker.play_wait()
    disp.set(0, 'Card scanned')
    disp.set(1, 'Saving log...')

    # Sync the card with db
    cardrow = db.get_by_id('card', card, 'id, user_id')

    if cardrow == None:
        db.create_card(card)

    # Log a coffee for this card
    db.create_coffee(card)
    
    # Sound feedback
    speaker.play_success()

    # Display a success message
    messages = [
        'Got your coffee written down.',
        'There are now records of your coffee.',
        'Enjoy your coffee.',
        'Ok.'
        ]
    disp.set(0, 'Logged!')
    disp.set(1, messages[random.randint(0, 3)])

    # Hold the message for a while
    time.sleep(4)

    # Back to standby display
    disp.set(0, 'Ready.')
    disp.set(1, 'Hey, tap your card to log your coffee.')
    