from pynput.keyboard import Key, Controller
from pynput import keyboard
import time

time.sleep(3)

key_board = Controller()

with key_board.pressed(Key.shift):
    key_board.press("0")
    key_board.release("0")

    key_board.press(Key.left)
    key_board.release(Key.left)



