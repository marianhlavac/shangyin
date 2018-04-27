import os

def truncated(line, width, offset=0, center=False):
    if len(line) < width:
        return line.center(width, ' ') if center else line
    else:
        offset = 0 if offset < 0 else offset
        return line[offset:offset+width]

class Display:
    def __init__(self, driver, disp_width = 16, disp_lines = 2, view_offset = 5):
        self.width = disp_width
        self.lines = disp_lines
        self.view_offset = view_offset
        self.messages = [''] * disp_lines
        self.positions = [-view_offset] * disp_lines
        self.driver = driver

    def set(self, linenum, message):
        self.messages[linenum] = message
        self.positions[linenum] = -self.view_offset

    def update(self):
        os.system('clear')

        for i in range(self.lines):
            # Increment view position
            self.positions[i] += 1

            # Check for view position overflow
            if self.positions[i] > len(self.messages[i]):
                self.positions[i] = -self.view_offset

            if self.driver == None:
                print(truncated(
                    self.messages[i], self.width, self.positions[i], True
                ))
