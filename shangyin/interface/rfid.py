from pirc522 import RFID
import hashlib

def init():
    return RFID(pin_irq=8, pin_rst=10)

def hash_card(uid):
    return hashlib.sha256(''.join(str(e) for e in uid).encode('utf-8')).hexdigest()

def read_card(rdr):
    rdr.wait_for_tag()
    (error, _tag_type) = rdr.request()

    if not error:
        (error, uid) = rdr.anticoll()

    # Check if it's a valid card
    if not error:
        return hash_card(uid)