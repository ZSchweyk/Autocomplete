from pynput.keyboard import Key, Controller, HotKey
from pynput import keyboard
import time
# import keyboard

key_board = Controller()

def press(button):
    key_board.press(button)
    key_board.release(button)


def parenthesis_autocomplete():
    print("pressed")
    with key_board.pressed(Key.shift):
        press("9")
        press("0")
    press(Key.left)


with keyboard.GlobalHotKeys({'<shift>+9': parenthesis_autocomplete}) as h:
    h.join()

# keyboard.add_hotkey("shift + 9", parenthesis_autocomplete)


