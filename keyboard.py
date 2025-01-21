from pynput import keyboard
from pynput.keyboard import Controller

# Initialize the keyboard controller
kb_controller = Controller()

i = -1
word = "word-"
wordLength = len(word)-1
lastKey = ""


def on_press(key):
    global i
    global wordLength
    global lastKey

    key_str = str(key).replace("'", "")

    # key != keyboard.Key.backspace and key != keyboard.Key.ctrl_l and key != keyboard.Key.ctrl_r
    if key_str != word[i] and i <= wordLength and not key_str.startswith("Key") and key_str != lastKey:

        if i >= wordLength:
            i = -1
        i += 1

        try:
            print(f"Key pressed: {key}")
            print("lastkey", lastKey)
            lastKey = key
            kb_controller.press(keyboard.Key.backspace)
            kb_controller.release(keyboard.Key.backspace)
            # Simulate pressing the word[i] key
            kb_controller.press(word[i])
            kb_controller.release(word[i])
            print(f"Simulated pressing {word[i]}")

            if word[i+1] == "-":
                print("space detected")
                kb_controller.press(keyboard.Key.space)
                kb_controller.release(keyboard.Key.space)

        except Exception as e:
            print(f"Error: {e}")

    else:
        if key == keyboard.Key.space:
            kb_controller.press(keyboard.Key.backspace)
            kb_controller.release(keyboard.Key.backspace)

        print("blocked stack overflow or key")


def on_release(key):
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False


# Listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
