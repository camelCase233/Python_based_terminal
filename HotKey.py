from pynput import keyboard
from Main import run

cmd = [{keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('b')}]
track = set()

def execute():
    window = run()
    window.mainloop()

def on_press(key):
    if any([key in z for z in cmd]):
        track.add(key)
        if any(all(k in track for k in z) for z in cmd):
            execute()


def on_release(key):
    if any([key in z for z  in cmd]):
        track.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()