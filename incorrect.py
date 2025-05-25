from tkinter import *
from tkinter import ttk
import os
import random

def after_second():  

    def create_window(index):
        if index < 50:
            window3 = Toplevel()
            window3.title("Пока можешь")
            width, height = 400, 200
            x = random.randint(0, 1920 - width)
            y = random.randint(0, 1080 - height)
            window3.geometry(f"{width}x{height}+{x}+{y}")
            lbl = ttk.Label(window3, text="Но это не искупит твой грех...", font=("Arial", 14), foreground="#FC0202", background="#000000")
            lbl.pack(expand=True)
            window3.config(bg='black')
            windows3.append(window3)
            window3.after(100, create_window, index + 1)
        # else:
        #     primi_nakazanye()

    windows3 = []
    create_window(0)

def after_first():
    def primi_nakazanye():
        for window2 in windows2:
            window2.destroy()
    root.after(5000, after_second)

    def create_window(index):
        if index < 50:
            window2 = Toplevel()
            window2.title("Пока можешь")
            width, height = 400, 200
            x = random.randint(0, 1920 - width)
            y = random.randint(0, 1080 - height)
            window2.geometry(f"{width}x{height}+{x}+{y}")
            lbl = ttk.Label(window2, text="Читай!", font=("Arial", 14), foreground="#FC0202", background="#000000")
            lbl.pack(expand=True)
            window2.config(bg='black')
            windows2.append(window2)
            window2.after(100, create_window, index + 1)
        else:
            primi_nakazanye()

    windows2 = []
    create_window(0)

def open_browser():
    for window in windows:
        window.destroy()
    os.system("start msedge https://quran-online.ru/1:1")
    root.after(5000, after_first)

def create_window(index):
    if index < 50:
        window = Toplevel()
        window.title("Ты врешь Аллаху")
        width, height = 400, 200
        x = random.randint(0, 1920 - width)
        y = random.randint(0, 1080 - height)
        window.geometry(f"{width}x{height}+{x}+{y}")
        lbl = ttk.Label(window, text="Зачем ты врешь что читал коран?", font=("Arial", 14), foreground="#FC0202", background="#000000")
        lbl.pack(expand=True)
        window.config(bg='black')
        windows.append(window)
        window.after(100, create_window, index + 1)
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
