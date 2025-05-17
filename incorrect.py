from tkinter import *
from tkinter import ttk
import os
import random
import tempfile
import base64
import zlib


def create_error_window(x, y):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', "9", "A", 'B', 'C', 'D', 'E', 'F']
    ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))
    _, ICON_PATH = tempfile.mkstemp(suffix=".ico")
    with open(ICON_PATH, "wb") as icon_file:
        icon_file.write(ICON)

    errorwin = Toplevel()
    errorwin.iconbitmap(default=ICON_PATH)
    errorwin.title("Error")
    errorwin.geometry(f"180x115+{x}+{y}")
    errorwin.resizable(False, False)
    try:
        img = PhotoImage(file="img/error.png")
        errorwin.img = img
        imglabel = ttk.Label(errorwin, image=img)
        imglabel.place(x=15, y=20)
    except Exception as e:
        print(f"Error loading image: {e}")
        imglabel = ttk.Label(errorwin, text="Image not found")
        imglabel.place(x=15, y=20)
    error_code = f"Error x{''.join(random.choices(numbers, k=8))}"
    errorlabel = ttk.Label(errorwin, text=error_code)
    errorlabel.place(x=70, y=35)
    btn = ttk.Button(errorwin, text="OK", command=errorwin.destroy)
    btn.place(x=90, y=85)


def create_multiple_error_windows(x, y, count, direction, callback):
    if count > 0:
        create_error_window(x, y)
        if direction == "nw-se":
            root.after(50, lambda: create_multiple_error_windows(x + 100, y + 100, count - 1, direction, callback))
        elif direction == "se-nw":
            root.after(50, lambda: create_multiple_error_windows(x - 100, y - 100, count - 1, direction, callback))
        elif direction == "w-e":
            root.after(50, lambda: create_multiple_error_windows(x + 100, y, count - 1, direction, callback))
        elif direction == "sw-ne":
            root.after(50, lambda: create_multiple_error_windows(x + 100, y - 100, count - 1, direction, callback))
    else:
        callback()

def create_multiple_error_windows_instant(x, y, count, direction):
    if count > 0:
        create_error_window(x, y)
        if direction == "nw-se":
            root.after(20, lambda: create_multiple_error_windows_instant(x + 100, y + 100, count - 1, direction))
        elif direction == "se-nw":
            root.after(20, lambda: create_multiple_error_windows_instant(x - 100, y - 100, count - 1, direction))
        elif direction == "w-e":
            root.after(20, lambda: create_multiple_error_windows_instant(x + 100, y, count - 1, direction))
        elif direction == "sw-ne":
            root.after(20, lambda: create_multiple_error_windows_instant(x + 100, y - 100, count - 1, direction))

def creating_instantly():
    for i in range(20):
        x = random.randint(0, 2560)
        y = random.randint(0, 1440)
        direction = random.choice(['nw-se', 'se-nw', 'w-e', 'sw-ne'])
        create_multiple_error_windows_instant(x, y, 30, direction)
        if i == 20:
            def ultimate_death():
                create_error_window(x, y)
                root.after(250, ultimate_death)

def virus():
    create_multiple_error_windows(100, 100, 20, "nw-se",
                                  lambda: create_multiple_error_windows(1720, 1080, 20, "se-nw", lambda:
                                                                         create_multiple_error_windows(0, 500, 30, "w-e", lambda:
                                                                                                                                       create_multiple_error_windows(0, 1440, 20, 'sw-ne', lambda:
                                                                                                                                                                     create_multiple_error_windows(1250, 0, 20, "nw-se", lambda:
                                                                                                                                                                                                   creating_instantly())))))


def main():
    global root
    root = Tk()
    root.title("")
    start_button = ttk.Button(root, text="Start", command=virus)
    start_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
