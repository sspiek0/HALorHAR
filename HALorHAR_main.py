from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry('1500x900')
root.config(bg='white')

#переменные

Question_Counter = 0
Meter_Counter = 50

#Функции

def Button_Halal():
    global Question_Counter
    global Meter_Counter
    
    if Question_Counter==1:
        Pig.destroy()
    
    Meter_Counter+=50
    Question_Counter+=1
    root.config(bg=Colors[Question_Counter])
    Potuzno_Meter_Title['text']='РIВЕНЬ ПОТУЖНIСТÏ', Emojis[Question_Counter]
    Test_Title['text']=f'Вопрос {Question_Counter+1}/11'

    Potuzno_Meter_Image2 = PhotoImage(file='m_Potuznost_Meter.png', height=Meter_Counter)
    Potuzno_Meter.config(image='Potuzno_Meter_Image2')

    
def Button_Haram():
    global Question_Counter
    Question_Counter+=1
    root.config(bg=Colors[Question_Counter])
    Potuzno_Meter_Title['text']='РIВЕНЬ ПОТУЖНIСТÏ', Emojis[Question_Counter]
    

#Списки

Emojis = ['😊', '😄', '😃','🙂', '😐', '😑', '😒', '😠', '🤬', '👿', '💀']
Questions = []
Colors = ['#FFFFFF', '#E6E6E6', '#CCCCCC', '#B3B3B3', '#999999', '#808080',
          '#666666', '#4D4D4D', '#333333', '#000000', '#000000']

#картинки

Koran_Gif_Image = PhotoImage(file='KORAN-GIF.gif')
Potuzno_Meter_Image = PhotoImage(file='m_Potuznost_Meter.png', height=50)
Main_Test_Image = PhotoImage(file='Main-Test.png', width=1000, height=650)
Pig_Image = PhotoImage(file='Pig_Image.png')

#объекты

Koran_Gif = ttk.Label(image=Koran_Gif_Image).place(x=200,y=20)

Pig = ttk.Label(image=Pig_Image, border=0)
Pig.place(x=1050, y=640)

Main_Test = ttk.Label(image=Main_Test_Image).place(x=70,y=230)

Potuzno_Meter = ttk.Label(image=Potuzno_Meter_Image,
                          border=0)
Potuzno_Meter.place(x=1170, y=240)

Button_Haram = Button(text='Харам', width=25,
                      height=4, command=Button_Haram).place(x=200, y=750)

Button_Halal = Button(text='Халяль', width=25,
                      height=4, command=Button_Halal).place(x=700, y=750)

#тайтлы

root.title('HARorHAL')
root.resizable(False, False)
Title = ttk.Label(text='Харам или Халяль?', font=('Impact', 58),
                  foreground='white')
Title.place(x=500, y=30)
Test_Title = ttk.Label(text='Вопрос 1/11', font=('Times', 36,
                 'italic'), foreground='red')
Test_Title.place(x=490, y=200)
Potuzno_Meter_Title = ttk.Label(text='РIВЕНЬ ПОТУЖНIСТÏ ☺️', font=('Times',
                                    24, 'italic'), foreground='red')
Potuzno_Meter_Title.place(x=1100, y=200)





root.mainloop()
