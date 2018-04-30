import os
import RPi.GPIO as GPIO
from charlcd import direct as lcd
from charlcd.drivers.gpio import Gpio

def truncated(line, width, offset=0, center=False):
    if len(line) < width:
        return line.center(width, ' ') if center else line
    else:
        offset = 0 if offset < 0 else offset
        return line[offset:offset+width]

class Display:
    def __init__(self, disp_width = 16, disp_lines = 2, view_offset = 5):
        self.width = disp_width
        self.lines = disp_lines
        self.view_offset = view_offset
        self.messages = [''] * disp_lines
        self.positions = [-view_offset] * disp_lines

        g = Gpio()
        g.pins = {
            'RS': 22,
            'E': 18,
            'E2': None,
            'DB4': 15,
            'DB5': 16,
            'DB6': 13,
            'DB7': 11
        }

        self.lcd = lcd.CharLCD(16, 2, g)
        self.lcd.init()

    def set(self, linenum, message):
        self.messages[linenum] = message
        self.positions[linenum] = -self.view_offset

    def update(self):
        for i in range(self.lines):
            # Increment view position
            self.positions[i] += 1

            # Check for view position overflow
            if self.positions[i] > len(self.messages[i]):
                self.positions[i] = -self.view_offset

            line = truncated(self.messages[i], self.width, self.positions[i], True)

            self.lcd.set_xy(0, i)
            self.lcd.write(line)
