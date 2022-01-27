from pynput.keyboard import Key, Controller, HotKey
from pynput import keyboard
import time
# import keyboard

c = Controller()

def press(button):
    c.press(button)
    c.release(button)


def parenthesis_autocomplete():
    with c.pressed(Key.shift):
        press("9")
        press("0")

    # c.press(Key.shift)
    # press("9")
    # press("0")
    # c.release(Key.shift)
    press(Key.left)



with keyboard.GlobalHotKeys({'shift+9': parenthesis_autocomplete}) as h:
    h.join()

# keyboard.add_hotkey("shift + 9", parenthesis_autocomplete)


