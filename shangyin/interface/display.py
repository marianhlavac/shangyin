import os

disp_w = 16

status = ''
message = ''
message_view = -3

def line(line, offset = 0):
    if len(line) < disp_w:
        return line.center(disp_w, ' ')
    else:
        return line[offset:offset+disp_w]

def change(new_status, new_message):
    global status, message, message_view
    status = new_status
    message = new_message
    message_view = -3

def update():
    global message_view
    message_view += 1
    if message_view > len(message) + 3:
        message_view = -3

def draw():
    #TODO: Draw to display
    pass

def debug_in_console():
    os.system('clear')
    print(line(status))
    print(line(message, 0 if message_view < 0 else message_view))

