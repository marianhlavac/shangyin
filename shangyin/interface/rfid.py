from pirc522 import RFID

def init():
    return RFID()

def wait_for_card(rdr):
    rdr.wait_for_tag()
    (error, _tag_type) = rdr.request()

    if not error:
        (error, uid) = rdr.anticoll()

    if not error:
        return uid
    else:
        return None