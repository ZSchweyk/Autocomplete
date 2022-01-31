from pynput.keyboard import Key, Controller, HotKey, KeyCode
from pynput import keyboard
import time

c = Controller()


def press(button):
    c.press(button)
    c.release(button)


# def shift_autocomplete(boolean, char):
#     if boolean:
#         with c.pressed(Key.shift_r):
#             press(char)
#     else:
#         press(char)
#     c.release(Key.shift_l)
#     press(Key.left)

def parenthesis():
    with c.pressed(Key.shift_r):
        press("0")
    c.release(Key.shift_l)
    press(Key.left)


write_ending_square_bracket = True


def curly_brackets():
    global write_ending_square_bracket
    with c.pressed(Key.shift_r):
        press("]")
    c.release(Key.shift_l)
    press(Key.left)
    write_ending_square_bracket = False


def square_brackets():
    global write_ending_square_bracket
    if write_ending_square_bracket:
        press("]")
        c.release(Key.shift_l)
        press(Key.left)
    else:
        write_ending_square_bracket = True


write_ending_double_quote = True


def double_quote():
    global write_ending_double_quote
    with c.pressed(Key.shift_r):
        press("'")
    c.release(Key.shift_l)
    press(Key.left)
    write_ending_double_quote = False


write_ending_single_quote = True


def single_quote():
    global write_ending_double_quote
    if write_ending_double_quote:
        press("'")
        c.release(Key.shift_l)
        press(Key.left)
    else:
        write_ending_double_quote = True


with keyboard.GlobalHotKeys(
        {
            "<shift>+9": parenthesis,

            "<shift>+[": curly_brackets,

            # DO NOT UNCOMMENT THIS LINE.
            "[": square_brackets,

            "<shift>+'": double_quote,

            # DO NOT UNCOMMENT THIS LINE.
            "'": single_quote,

        }
) as h:
    h.join()

# keyboard.add_hotkey("shift + 9", parenthesis_autocomplete)
