from tkinter import *
from tkinter import ttk
from math import floor, ceil
import codecs
import winsound
from random import randint
from tkinter.messagebox import showwarning, askyesno


root = Tk()

screen_x = root.winfo_screenwidth()
screen_y = root.winfo_screenheight()

window_x = floor(screen_x*0.8)
window_y = floor(screen_y*0.8)

root.geometry(f'{window_x}x{window_y}+{floor(0.1*screen_x)}+{floor(0.1*screen_y)}')
root.title('HALorHAR.exe')
root.resizable(0,0)

#--functions

colors = ['#F00000', '#000000', '#FFFFFF']
window_titles=['YOU MADE A MISTAKE', 'your punishment is here ', 'HELP ME '*20, 'ALLAH WON\'T FORGIVE YOU', '911 '*100, 'GOD SAVE ME', '33'*100]

max_diff = floor(window_y*0.6)
current_question=1
questions = codecs.open('questions (3).txt', 'r', 'utf_8_sig').read().split('/')

#--virus------------------------------------------------------

def shake_screen():
    root.configure(bg=colors[randint(0,2)])
    x=randint(floor(0.1*screen_x), floor(0.11*screen_x))
    y=randint(floor(0.1*screen_y), floor(0.11*screen_y))
    root.geometry(f'{window_x}x{window_y}+{x}+{y}')
    root.update()
    root.after(25, shake_screen)

def change_titles():
    root.title(window_titles[randint(0,6)])
    root.after(2000, change_titles)

def delete_all():
    for child in root.winfo_children()[:-3]:
        child.destroy()
        root.after(25)
        root.update()

def last_msg():
    root.configure(bg='#FFFFFF')
    result = askyesno(title='不要转身', message='大屠杀还没有结束。..')

    if result or not result: root.destroy()

def fuck_computer():
    root.iconphoto(False, PhotoImage(file='img/eye.png'))
    root.configure(bg='#F00000')


    for child in root.winfo_children():
        try:
            child['text']='لقد أهانت القرآن والإسلام'
        except:
            continue
    for child in main.winfo_children():
        try:
            child['text']='لقد أهانت القرآن والإسلام'
        except:
            continue

    change_titles()
    
    eye_img = Label(image=eye)
    eye_img.place(relx=.15, rely=.5, anchor=CENTER)

    eye_img = Label(image=eye)
    eye_img.place(relx=.85, rely=.5, anchor=CENTER)
    
    last_message= Label(text='在地狱里燃烧', fg='red', bg='#000000', font=('Times', floor(window_x/20*1.3)),
                        height=2)
    last_message.place(rely=.5, relx=.5, anchor=CENTER)

    root.after(6000, delete_all)
    root.after(6000, shake_screen)
    root.after(6100, end)
    root.after(6200, total_end)
    root.after(18000, last_msg)
    
#-----------------------------------------------

def btn_hal():
    if questions[current_question-1][-1]=='l':
        correct = Label(main, image=smaller_correct_img)
        correct.place(rely=.55, relx=.5, anchor=CENTER)
        root.after(100, correct_snd)
        root.after(1000, continue_test)
        root.after(1000, lambda: correct.destroy())
    else:
        correct = Label(main, image=incorrect_img)
        correct.place(rely=.55, relx=.5, anchor=CENTER)
        root.after(100, incorrect_snd)
        root.after(4000, lambda: correct.destroy())

        btn1.configure(text='you', state=DISABLED)
        btn2.configure(text='fucked up :)', state=DISABLED)
        root.after(5000, fuck_computer)
        root.after(5500, pre_fuck)

def btn_har():
    if questions[current_question-1][-1]=='r':
        correct = Label(main, image=smaller_correct_img)
        correct.place(rely=.55, relx=.5, anchor=CENTER)
        root.after(100, correct_snd)
        root.after(1000, continue_test)
        root.after(1000, lambda: correct.destroy())
    else:
        correct = Label(main, image=incorrect_img)
        correct.place(rely=.55, relx=.5, anchor=CENTER)
        root.after(100, incorrect_snd)
        root.after(4000, lambda: correct.destroy())

        btn1.configure(text='you', state=DISABLED)
        btn2.configure(text='fucked up :)', state=DISABLED)
        root.after(5000, fuck_computer)
        root.after(5500, pre_fuck)

def continue_test():
    global current_question, max_diff
    current_question+=1

    if current_question == 5:
        showwarning(title='立即停止！', message='棺材里安装了一个摄像头，尸体继续移动')
    elif current_question == 9:
        showwarning(title='立即关闭程序', message='最后一次断头台处决是在1977年9月10日进行的。')
    if current_question!=11:
        q_text['text']=questions[current_question-1][2:-1]
        diff_meter['height']+=floor(max_diff*(1/10))
        Percent['text']=f'Пройдено {ceil(current_question/11*100)}%'
        q_num['text']=f'Вопрос {current_question}/11'
    else:
        q_num['text']='Вопрос ???/11'
        Percent['text']='Тобi пизда'
        q_text['text']=questions[current_question-1][2:-1]
        root.configure(bg='#000000')
        btn1.configure(text='allah', state=DISABLED)
        btn2.configure(text='666', state=DISABLED)
        root.after(10, winsound.Beep(400, 2000))
        root.after(6000, fuck_computer)
        root.after(6500, pre_fuck)

#sounds

def correct_snd():
    winsound.PlaySound('audio/correct.wav', winsound.SND_FILENAME)

def incorrect_snd():
    winsound.PlaySound('audio/wrong.wav', winsound.SND_FILENAME)

def pre_fuck():
    winsound.PlaySound('audio/children-die.wav', winsound.SND_FILENAME)

def end():
    winsound.PlaySound('audio/better-sonic-exe-laugh.wav', winsound.SND_FILENAME)

def total_end():
    winsound.PlaySound('audio/konkonse-boosted.wav', winsound.SND_ASYNC)

#images

root.iconphoto(False, PhotoImage(file='img/logo.png'))

eye = PhotoImage(file='img/eye.png')
correct_img = PhotoImage(file='img/correct.png')
incorrect_img = PhotoImage(file='img/error.png')
smaller_correct_img = correct_img.subsample(15,15)

#widgets

title = Label(text='Халяль или Харам?', font=('Impact', floor(window_x/30*1.3)),
              background='#000000',
               foreground='#FFFFFF')
title.place(anchor=CENTER, relx=0.5, rely=0.1)


#--main-Test

main = Frame(width=floor(0.65*window_x), height=floor(0.7*window_y), bg='grey')
main.place(anchor=W, relx=.025, rely=.62)

q_num = Label(text='Вопрос 1/11', font=('Times', floor(window_x/80*1.3),
                                        'italic'), foreground='#F00000', background='#000000')
q_num.place(relx=.35, rely=.28, anchor=CENTER)


q_text = Label(main,text=questions[0][:-1], font=('Times',floor(window_x/100*1.3), 'italic'),
               width=floor(window_x/100)*6, justify='center',
               height=5, wraplength=floor(window_x/100)*36, bg='#000000', fg='#FFFFFF')
q_text.place(relx=.5, rely=.2, anchor=CENTER)

btn1 = Button(main, text='Халяль', font=('Courier New', 12, 'italic'), width=floor(window_x*0.25*0.1), height=2, command=btn_hal)
btn1.place(anchor=W, relx=.07, rely=.8)

btn2 = Button(main, text='Харам', font=('Courier New', 12, 'italic'), width=floor(window_x*0.25*0.1), height=2, command=btn_har)
btn2.place(anchor=E, relx=.93, rely=.8)
#--difficulty-level

diff_title = Label(text='Рiвень потужности', font=('Times', floor(window_x/80*1.3),
                                        'italic'), foreground='#F00000', background='#000000')
diff_title.place(relx=.85, rely=.28, anchor=CENTER)

diff_meter = Frame(width=floor(window_x*0.1), height=max_diff//11, bg='green')
diff_meter.place(anchor=S, rely=0.96, relx=.85)

diff_1 = Label(text='<-- iзи', font=('Times', floor(window_x/100*1.3), 'italic'), fg='white', bg='#000000')
diff_1.place(rely=0.85, relx=.9, anchor=W)

diff_2 = Label(text='<-- среднi', font=('Times', floor(window_x/100*1.3), 'italic'), fg='white', bg='#000000')
diff_2.place(rely=0.65, relx=.9, anchor=W)

diff_3 = Label(text='<-- сложнi', font=('Times', floor(window_x/100*1.3), 'italic'), fg='white', bg='#000000')
diff_3.place(rely=0.45, relx=.9, anchor=W)

diff_4 = Label(text='<-- крiтичнi', font=('Times', floor(window_x/100*1.3), 'italic'), fg='white', bg='#000000')
diff_4.place(rely=0.35, relx=.9, anchor=W)


#--percent-of-done

Percent = Label(text=f'Пройдено 0%', bg='#000000', fg='white', font=('Times', floor(window_x/70*1.3)))
Percent.place(relx=0.5, rely=0.19, anchor=CENTER)
root.mainloop()
