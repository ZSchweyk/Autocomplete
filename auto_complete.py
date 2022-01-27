from pynput.keyboard import Key, Controller, HotKey, KeyCode
from pynput import keyboard
import time
# import keyboard

c = Controller()

def press(button, num):
    for i in range(num):
        c.press(button)
        c.release(button)

def on_press(key):
    try:
        key_code = key.vk
    except AttributeError:
        key_code = key.value.vk

    if key_code == 40:
        # press(Key.backspace, 1)

        with c.pressed(Key.shift):
            # press("9", 1)
            press("0", 1)
        c.release(Key.shift)
        press(Key.left, 1)


with keyboard.Listener(
        on_press=on_press,
        ) as listener:
    listener.join()





















# c = Controller()
#
# def press(button):
#     c.press(button)
#     c.release(button)
#
#
# def parenthesis_autocomplete():
#     with c.pressed(Key.shift):
#         press("9")
#         press("0")
#
#     # c.press(Key.shift)
#     # press("9")
#     # press("0")
#     # c.release(Key.shift)
#     press(Key.left)
#
#
#
# with keyboard.GlobalHotKeys({'shift+9': parenthesis_autocomplete}) as h:
#     h.join()













# keyboard.add_hotkey("shift + 9", parenthesis_autocomplete)


