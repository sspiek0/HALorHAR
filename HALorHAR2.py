from tkinter import *
from tkinter import ttk
import tkSnack
from tkinter.messagebox import showinfo
import math

root = Tk()
screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()
x_size = math.floor(screen_x*0.55)
y_size = math.floor(screen_y*0.6)

root.geometry(f'{x_size}x{y_size}+{math.floor(screen_x*.5-x_size/2)}+{math.floor(screen_y*0.5-y_size/2)}')
root.resizable(0,0)
root.title('HALorHAR.exe')

root.iconphoto(False, PhotoImage(file='img/logo.png'))
root.config(bg='#FFFFFF')

diff_meter = 50
question_counter = 0
questions=open('questions (1).txt', 'r').read().split('/')
    

def continue_test():
    global question_counter, diff_meter
    pydub.play('audio/error')
    diff_meter+=50
    question_counter+=1
    question_number['text']=f'Вопрос {question_counter+1}/11'
    question_label['text']=questions[question_counter][:-1]

    diff_img.config(file='img/m_Potuznost_Meter.png', height=diff_meter)

def fuck_computer():
    if question_counter!=10:
        root.config(bg='#F00000')
    
def btn_hal():
    global questions, question_counter
    if questions[question_counter][-1]=='l' and question_counter!=10:
        continue_test()
    else:
        fuck_computer()

def btn_har():
    global questions, question_counter
    if questions[question_counter][-1]=='r' and question_counter!=10:
        continue_test()
    else:
        fuck_computer()

#images

diff_img = PhotoImage(file='img/m_Potuznost_Meter.png', height=50)
koran_img = PhotoImage(file='img/KORAN-GIF.gif')

#widgets

title = Label(text=' Халяль или Харам? ', font=('Impact', 58),
                  foreground='white', background='black')
title.place(relx=.5, anchor=CENTER, rely=.1)

#----
main_frame = Frame(borderwidth=5, bg='grey',
                 width=math.floor(x_size*.7), height=math.floor(y_size*.7))
main_frame.place(relx=.025, rely=.25)

question_number = Label(text=f'Вопрос {question_counter+1}/11', font=('Times', 36, 'italic'),
                 foreground='red', bg='#000000')
question_number.place(anchor=CENTER,
                     x=math.floor(main_frame['width']/2+x_size*.025),
                     rely = .25)


question_label = Label(main_frame, text=questions[question_counter][:-2],
                        justify=CENTER, wraplength=600, height=4,
                       width = 40, font=('Times', 36, 'italic'),
                       bg='#000000')
question_label.place(anchor= CENTER, relx=.5, rely=.2)

btn_hal = Button(main_frame, text='Халяль', width=20,
                 font=('Courier New', 24), height=3, command=btn_hal)
btn_har = Button(main_frame, text='Харам', width=20,
                 font=('Courier New', 24), height=3, command=btn_har)

btn_hal.place(anchor=CENTER, rely=.8, relx=.25)
btn_har.place(anchor=CENTER, rely=.8, relx=.75)
#----

diff_level = Label(text='Рiвень потужностi', font=('Times', 36, 'italic'), foreground='red',
                   bg='#000000')
diff_level.place(relx=.75, rely=.2)

diff_img_label = Label(image=diff_img, border=0)
diff_img_label.place(relx=.82, rely=.30)

koran_holder = Label(image=koran_img)
koran_holder.place(relx=.05, rely=.005)

root.mainloop()
