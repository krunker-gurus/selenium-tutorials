from pynput.mouse import Controller
import time

#You have 5 seconds to move mouse to position
time.sleep(5)
mouse = Controller()
print('The current pointer position is {0}'.format(mouse.position))
