from tkinter import *
from tkinter import ttk
import os
import random

def after_first():
    def primi_nakazanye():
        for window2 in windows2:
            window2.destroy()
    

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
        open_browser()

windows = []
root = Tk()
root.geometry("0x0")
create_window(0)

mainloop()
