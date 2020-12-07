from datetime import datetime
import os.path as path
import time
import threading
from ahk import AHK

### REQUIRES AHK V1 TO BE INSTALLED ON YOUR COMPUTER


if __name__ == "__main__":
    # initialize
    ahk = AHK()

    # go through process to get the point where mouse will be clicked
    print('Welcome to the Thumb Twiddler!')
    time.sleep(5)
    print('move your mouse over to the area where you want to click once every few minutes')
    time.sleep(3)
    print('hold still:')
    i = 5
    while i > 0:
        print(str(i))
        time.sleep(1)
        i = i - 1

    (x, y) = ahk.mouse_position
    time.sleep(1)
    ahk.mouse_position = (x, y)
    print(f'Ok! Mouse will be clicked at this location ({x}, {y}) once every few minutes, avoiding the time reports are run')
    ahk.click((x, y))
    time.sleep(2)
    print('entering loop...')
    while True:
        currMinute = datetime.now().minute
        currHour = datetime.now().hour
        if currMinute in (0, 10, 22, 34, 46, 58):
            # begin report making process
            ahk.mouse_position = (x, y)
            print(f'Click! ({currHour}:{currMinute})')
            ahk.click((x, y))
            time.sleep(2)
            ahk.click((x, y)) # for good measure
            time.sleep(57)



