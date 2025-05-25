from tkinter import *
from tkinter import ttk
import os
import random
import tempfile, base64, zlib


def create_error_window(x, y):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', "9", "A", 'B', 'C', 'D', 'E', 'F']

    ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))

    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, "wb") as icon_file:
        icon_file.write(ICON)

    errorwin = Toplevel()  # Use Toplevel instead of Tk for the error window
    errorwin.iconbitmap(default=ICON_PATH)
    errorwin.title("Error")
    errorwin.geometry(f"180x115+{x}+{y}")
    errorwin.resizable(False, False)

    # Keep a reference to the image
    img = PhotoImage(file="img/error.png")
    errorwin.img = img  # Store the image in the window to prevent garbage collection
    imglabel = ttk.Label(errorwin, image=img)
    imglabel.place(x=15, y=20)

    error_code = f"Error x{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}"
    errorlabel = ttk.Label(errorwin, text=error_code)
    errorlabel.place(x=70, y=35)

    btn = ttk.Button(errorwin, text="OK")
    btn.place(x=90, y=85)


def virus():
    x1 = 100
    y1 = 100
    for i in range(10):
        create_error_window(x1, y1)
        x1 += 100
        y1 += 100

def after_second():  
    def death():
        for window3 in windows3:
            window3.destroy()
        root.after(1000, virus)
    def create_window(index):
        if index < 50:
            window3 = Toplevel()
            window3.title("Пока можешь")
            width, height = 400, 200
            x = random.randint(0, 2560 - width)
            y = random.randint(0, 1440 - height)
            window3.geometry(f"{width}x{height}+{x}+{y}")
            lbl = ttk.Label(window3, text="Но это не искупит твой грех...", font=("Arial", 14), foreground="#FC0202", background="#000000")
            lbl.pack(expand=True)
            window3.config(bg='black')
            windows3.append(window3)
            window3.after(100, create_window, index + 1)
        else:
            death()

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
            x = random.randint(0, 2560 - width)
            y = random.randint(0, 1440 - height)
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
        x = random.randint(0, 2560 - width)
        y = random.randint(0, 1440 - height)
        window.geometry(f"{width}x{height}+{x}+{y}")
        lbl = ttk.Label(window, text="Зачем ты врешь что читал коран?", font=("Arial", 14), foreground="#FC0202", background="#000000")
        lbl.pack(expand=True)
        window.config(bg='black')
        windows.append(window)
        window.after(100, create_window, index + 1)
    else:
        open_browser()

windows = []
root = Tk()
root.geometry("0x0")
create_window(0)

mainloop()
