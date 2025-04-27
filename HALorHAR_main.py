from tkinter import*
from tkinter import ttk
import random

root = Tk()
root.geometry('1500x900')
root.config(bg='white')
root.iconphoto(False, PhotoImage(file='img/logo.png'))

#переменные

Question_Counter = 0
Meter_Counter = 75

#Функции

def Button_Halal():
    global Question_Counter
    global Meter_Counter
    if Question_Counter<10:         

        if Question_Counter==1:
            Pig.destroy()
    
        Meter_Counter+=50
        Question_Counter+=1
        root.config(bg=Colors[Question_Counter])
        Potuzno_Meter_Title['text']=f'РIВЕНЬ ПОТУЖНIСТÏ {Emojis[Question_Counter]}'
        Test_Title['text']=f'Вопрос {Question_Counter+1}/11'

        Potuzno_Meter_Image['file']='img/m_Potuznost_Meter.png'
        Potuzno_Meter_Image['height']=Meter_Counter
        Potuzno_Meter['image']=Potuzno_Meter_Image
    else:
        Message = ttk.Label(text='d0N\'† †®¥ †0 r6N', font=('Courier New',
            random.randint(30,70)), foreground='red', background='black')
        Message.place(x=random.randint(0,1300), y=random.randint(0,900))

    
def Button_Haram():
    global Question_Counter
    global Meter_Counter
    if Question_Counter<10:         

        if Question_Counter==1:
            Pig.destroy()
    
        Meter_Counter+=50
        Question_Counter+=1
        root.config(bg=Colors[Question_Counter])
        Potuzno_Meter_Title['text']=f'РIВЕНЬ ПОТУЖНIСТÏ {Emojis[Question_Counter]}'
        Test_Title['text']=f'Вопрос {Question_Counter+1}/11'

        Potuzno_Meter_Image['file']='img/m_Potuznost_Meter.png'
        Potuzno_Meter_Image.config(height=Meter_Counter)
        Potuzno_Meter['image']=Potuzno_Meter_Image
        Potuzno_Meter['background']=Colors[Question_Counter]
    else:
        Message = ttk.Label(text='d0N\'† †®¥ †0 r6N', font=('Courier New',
            random.randint(30,70)), foreground='red', background='#000000')
        Message.place(x=random.randint(0,1300), y=random.randint(0,900))

    

#Списки

Emojis = ['😊', '😄', '😃','🙂', '😐', '😑', '😒', '😠', '🤬', '👿', '💀']
Questions = {}
Question_Images = []
Colors = ['#FFFFFF', '#E6E6E6', '#CCCCCC', '#B3B3B3', '#999999', '#808080',
          '#666666', '#4D4D4D', '#333333', '#000000', '#000000']

#картинки

Koran_Gif_Image = PhotoImage(file='img/KORAN-GIF.gif')
Potuzno_Meter_Image = PhotoImage(file='img/m_Potuznost_Meter.png', height=50)
Main_Test_Image = PhotoImage(file='img/Main-Test.png', width=1000, height=650)
Pig_Image = PhotoImage(file='img/Pig_Image.png')

#объекты

Koran_Gif = ttk.Label(image=Koran_Gif_Image, border=0).place(x=200,y=20)

Pig = ttk.Label(image=Pig_Image, border=0)
Pig.place(x=1050, y=640)

Main_Test = ttk.Label(image=Main_Test_Image).place(x=70,y=230)

Potuzno_Meter = ttk.Label(image=Potuzno_Meter_Image,
                          border=0)
Potuzno_Meter.place(x=1170, y=240)

Button_Haram = Button(text='Харам', width=25,
    height=2, command=Button_Haram, font=('Courier New', 24))

Button_Haram.place(x=100, y=750)

Button_Halal = Button(text='Халяль', width=25,
    height=2, command=Button_Halal, font=('Courier New', 24))
Button_Halal.place(x=625, y=750)

#тайтлы

root.title('HARorHAL')
root.resizable(False, False)
Title = ttk.Label(text='Харам или Халяль?', font=('Impact', 58),
                  foreground='white', background='#000000', padding=8)
Title.place(x=500, y=30)
Test_Title = ttk.Label(text='Вопрос 1/11', font=('Times', 36,
                 'italic'), foreground='red', background='#000000')
Test_Title.place(x=490, y=200)
Potuzno_Meter_Title = ttk.Label(text='РIВЕНЬ ПОТУЖНIСТÏ ☺️', font=('Times',
        24, 'italic'), padding=2,foreground='red', background='#000000')
Potuzno_Meter_Title.place(x=1100, y=200)





root.mainloop()
