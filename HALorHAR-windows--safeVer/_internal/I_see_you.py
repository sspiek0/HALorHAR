from tkinter import *
from tkinter import ttk
from math import floor
from random import randint
import subprocess
import winsound
from tkinter.messagebox import showwarning
import getpass
import os

parent_folder = os.path.dirname(__file__)
print(parent_folder)
root = Tk()
root_avaible = True
Mc_root_win = None
desc = None
button_cancel = None
eye = PhotoImage(file=f'{parent_folder}/img/eye (3).png')
eye_for_mc = PhotoImage(file=f'{parent_folder}/img/eye (3).png').subsample(3,3)
eye_right = PhotoImage(file=f'{parent_folder}/img/eye-right.png').subsample(4,4)

koefficent = 0.1
screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()

window_x = floor(screen_x*0.8)
window_y = floor(screen_y*0.8)

titles=["DON'T DO IT. "*5, "PLEASE "*5, "I BEG YOU "*5, "DON'T ACCEPT THIS!!! "*5, "IT IS A TRAP!! "*5,]
btn1=None
btn2=None
#------------------------------------------------------------------------------------
def Mc_def_collapse():
    global Mc_root_win, desc
    winsound.PlaySound(f'{parent_folder}/audio/lags.wav', winsound.SND_ASYNC)
    Mc_root_win.configure(bg='#B30707')
    for obj in Mc_root_win.winfo_children():
        obj.configure(bg='#B30707', fg='#000000')
    desc['text']='Программа: HALorHAR.exe\nИздатель: '+'LET ME SEE YOU '*2
    for i in range(50):
        if i%2!=0:
            Mc_root_win.configure(bg='#000000')
            for obj in Mc_root_win.winfo_children():
                obj.configure(bg='#000000', fg='#B03707')
            Mc_root_win.update()
        else:
            Mc_root_win.configure(bg='#B30707')
            for obj in Mc_root_win.winfo_children():
                obj.configure(bg='#B30707', fg='#000000')
            Mc_root_win.update()

        desc['text']='Программа: '+'HA '*(i//2)+'\nИздатель: '+'LET ME SEE YOU '*3
        Mc_root_win.after(100)
        Mc_root_win.update()
    winsound.PlaySound(f'{parent_folder}/audio/lags.wav', winsound.SND_ASYNC)
    desc['text']='Программа: NO ESCAPE??\nИздатель: tspy doy\'e kuoh lbvue ehl czcpze.. <VIGENERE: allah>'

    Mc_root_win.after(5000, Mc_root_win.destroy)

def on_closing():
    global root_avaible, button_cancel

    root_avaible = False

    root.destroy()

    button_cancel.configure(text='n0 3sCAp3..', state=DISABLED, foreground='#FFFFFF')
    desc.configure(text='Программа: HALorHAR.exe\nИздатель: h3Lp M3!!!11')
    Mc_root_win.after(3000, Mc_def_collapse)

def on_closing_main():
    showwarning(title="don't try to run.", message="tspy doy'e kuoh lbvue ehl czcpze.. <VIGENERE: allah>")

def McDef():
    global eye, root_avaible, Mc_root_win, desc, button_cancel

    winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS+winsound.SND_ASYNC)
    Mc_root = Tk()
    Mc_root.title('Windows Security Notification')
    Mc_root.iconbitmap(f'{parent_folder}/img/Microsoft-Defender.ico')
    Mc_root.geometry(f'{floor(screen_x*0.7)}x{floor(screen_y*0.7)}+{floor(screen_x*.15)}+{floor(screen_y*.15)}')
    Mc_root.resizable(0,0)
    Mc_root.configure(bg="#2258DE")
    Mc_root.overrideredirect(True)

    Title = Label(Mc_root, text='Система Windows защитила ваш компьютер', wraplength=floor(screen_x*0.5),
                  font=('Segoe UI', floor(floor(screen_x*0.7)//30*1.3)), background='#2258DE', fg="#FFFFFF",
                  justify=LEFT, anchor=W, padx=floor(screen_x*0.7)*0.05)
    Title.pack(side=TOP, pady=floor(screen_y*0.5)*.05, fill=X)

    Desc = Label(Mc_root, text='Программа HALorHAR.exe пытается получить доступ к сетевым ресурсам вашего компьютера.',
                  wraplength=floor(screen_x*0.5),
                  font=('Segoe UI', floor(floor(screen_x*0.7)//60*1.3)), background='#2258DE', fg="#FFFFFF",
                  justify=LEFT, anchor=W, padx=floor(screen_x*0.7)*0.05)
    Desc.pack(side=TOP, pady=floor(screen_y*0.5)*0.03, fill=X)

    Button_cancel = Button(Mc_root, text='Отмена', font=('Segoe UI', floor(floor(screen_x*0.7)//70*1.3)),
                           background="#93B2E9", width=20, relief=SOLID, borderwidth=0,
                           foreground="#FFFFFF", command=on_closing)
    Button_cancel.pack(anchor=E, pady=floor(screen_y*0.5)*0.05, side=BOTTOM, padx=[0,floor(screen_y*0.5)*0.07], expand=0)

    More_info = Button(Mc_root, text='Подробнее', font=('Segoe UI', floor(floor(screen_x*0.7)//70*1.3), 'underline'),
                      bg='#2258DE', fg='#FFFFFF', relief=SOLID, justify=LEFT,
                      border=0, command=on_closing)
    More_info.pack(side=TOP, pady=floor(screen_y*0.5)*0.03, anchor=W, padx=floor(screen_x*0.7)*0.05)
    Mc_root_win = Mc_root
    desc=More_info
    button_cancel=Button_cancel

def on_closing_with():
    showwarning(title="<DON'T EVEN TRY.>", message='棺材里的尸体继续移动')

def with_Mc_def():
    global window_x, window_y, eye_right, eye_for_mc

    currect_dialog = 0
    dialog=['Oh, what do we have here', 'looks like your dumb system tries to protect your computer',
            'i don\'t want the fun to end.', f'Have fun, {getpass.getuser()}']
    dialog_audio=[f'{parent_folder}/audio/Oh what.wav', f'{parent_folder}/audio/Looks like.wav', f'{parent_folder}/audio/I dont want.wav',
                  f'{parent_folder}/audio/Have fun.wav']
    eye_root = Tk()
    eye_root.geometry(f'{floor(window_x*.4)}x{floor(window_y*.5)}+0+{floor(window_y*.5)}')
    eye_root.title(f'to {getpass.getuser()}')
    eye_root.configure(background='#000000')
    eye_root.resizable(0,0)
    eye_root.protocol('WM_DELETE_WINDOW', on_closing_with)
    eye_for_mc = PhotoImage(file=f'{parent_folder}/img/eye (3).png', master=eye_root).subsample(3,3)
    eye_right = PhotoImage(file=f'{parent_folder}/img/eye-right.png', master=eye_root).subsample(4,4)

    eye_root.iconphoto(False, eye_for_mc)

    for i in range(10):
        if i%2==0:
            eye_root.configure(background='#F00000')
        else:
            eye_root.configure(background='#000000')
        eye_root.after(50)
        eye_root.update()
        
    eye1 = Label(eye_root, image=eye_for_mc, border=0)
    eye2 = Label(eye_root, image=eye_for_mc, border=0)

    eye1.place(anchor=CENTER, relx=.2, rely=.6)
    eye2.place(anchor=CENTER, relx=.8, rely=.6)

    text = Label(eye_root, text=dialog[currect_dialog],  font=('Courier New', 14, 'bold'), fg='#F00000', 
                 bg='#000000', wraplength=floor(window_x*.4*.9))
    text.place(relx=0.5, rely=.15, anchor=CENTER)
    eye_root.update()
    winsound.PlaySound(dialog_audio[currect_dialog], winsound.SND_ASYNC)
    currect_dialog+=1
    eye_root.after(4000)
    text['text']=dialog[currect_dialog]
    winsound.PlaySound(dialog_audio[currect_dialog], winsound.SND_ASYNC)
    eye1['image']=eye_right
    eye2['image']=eye_right
    currect_dialog+=1
    eye_root.update()
    eye_root.after(4000)
    text['text']=dialog[currect_dialog]
    winsound.PlaySound(dialog_audio[currect_dialog], winsound.SND_ASYNC)
    currect_dialog+=1
    eye_root.update()
    eye_root.after(4000)
    text['text']=dialog[currect_dialog]
    winsound.PlaySound(dialog_audio[currect_dialog], winsound.SND_ASYNC)
    eye1['image']=eye_for_mc
    eye2['image']=eye_for_mc
    eye_root.update()
    eye_root.after(3000)
    for i in eye_root.winfo_children():
        i.destroy()
    eye_root.configure(bg='#F00000')
    eye_root.update()
    eye_root.after(100, winsound.Beep(800, 3000))
    eye_root.after(3100, eye_root.destroy)

def turn_on_camera():
    subprocess.run(['start', 'microsoft.windows.camera:'], shell=True)
    root_avaible=False
    root.after(6000, lambda: root.withdraw())
    root.after(8000, McDef)
    root.after(11000, with_Mc_def) 
def change_titles():
    if root_avaible:
        root.title(titles[randint(0,4)])
        root.after(500, change_titles)
    else:
        return
    
change_titles()

def result_y():
    global text, btn1, btn2

    btn1.destroy()
    btn2.destroy()

    text.config(text="Thanks, bozo.")
    winsound.PlaySound(f"{parent_folder}/audio/That's to bad (2).wav", winsound.SND_ASYNC)
    

    root.after(2000, epileptic)
    root.after(2000, shake_screen)
    root.after(4500, turn_on_camera)

def result_n():
    global text, btn1, btn2

    btn1.destroy()
    btn2.destroy()

    text.config(text="That's to bad..")
    winsound.PlaySound(f"{parent_folder}/audio/That's to bad (2).wav", winsound.SND_ASYNC)
    
    root.after(2000, epileptic)
    root.after(2000, shake_screen)
    root.after(4500, turn_on_camera)

def shake_screen():
    global koefficent
    if root_avaible:
        x=floor(floor(screen_x*0.1))
        x1=floor(floor(screen_x*koefficent))

        y=floor(floor(screen_y*0.1))
        y1=floor(floor(screen_y*koefficent))

        root.geometry(f'{window_x}x{window_y}+{randint(x, x1)}+{randint(y, y1)}')
        koefficent+=.0002
        root.after(25, shake_screen)
    else:
        return
    
def epileptic():  
    for i in range(500):
        if root_avaible:
            if i%2!=0:
                root.configure(bg='#000000')

                root.update()
            else:
                root.configure(bg='#FFFFFF')
                root.update()
            root.after(10)

#-----------------------------------------------------------------------

def button1_appear():
    global btn1

    button1=Button(text='YES', background='#000000', fg='#FFFFFF', relief=FLAT,
            font=('Courier New', 20, 'bold'), command=result_y)
    button1.pack(fill=X, side=BOTTOM, pady=floor(window_y*0.05))
    root.after(500, winsound.PlaySound(f'{parent_folder}/audio/Beep (2).wav', winsound.SND_FILENAME+winsound.SND_ASYNC))
    root.after(1400, button2_appear)

    btn1=button1
def button2_appear():
    global btn2

    button2=Button(text='NO', background='#000000', fg='#FFFFFF', relief=FLAT,
            font=('Courier New', 20, 'bold'),  command=result_n)
    button2.pack(fill=X, side=BOTTOM)

    btn2=button2
#------------------------------------------------------------

root.geometry(f"{window_x}x{window_y}+{floor(screen_x*0.1)}+{floor(screen_y*0.1)}")
root.configure(bg='#000000')
root.iconphoto(False, eye)
root.protocol('WM_DELETE_WINDOW', on_closing_main)

text = Label(text='can i see your face?', font=('Courier New', 35, 'bold'), fg='#F00000', bg='#000000')
text.place(relx=.5, rely=.2, anchor=CENTER)

eye_label1 = Label(image=eye, border=0)
eye_label2 = Label(image=eye, border=0)

eye_label1.place(rely=.5, relx=.2, anchor=CENTER)
eye_label2.place(rely=.5, relx=.8, anchor=CENTER)
#-------------------------------------------------------------

root.after(2000, button1_appear)
root.mainloop()
