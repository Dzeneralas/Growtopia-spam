import pyautogui
from random import randrange as rd
from tkinter import *
pyautogui.FAILSAFE = False
colours = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'b', 'w', 'p', 'o', '^', '$', '#', '@', '!', 'q', 'e', 'c', 'r', 't', 'a', 's']
run = False
def start():
   global run
   run=True
   window.after(2000, spam)
def stop():
   global run
   run=False
def spam():
    if run:
        pyautogui.press("enter")
        if rcl.get():
            pyautogui.typewrite(''.join([f" `{colours[rd(0, 26)]}{wrd}" for wrd in txtfld.get().split()])[1:])
        else:
            pyautogui.typewrite(f"{txtfld.get()}")
        pyautogui.press("enter")
        window.after(interval.get(), spam)
window = Tk()
rcl = BooleanVar()
btn=Button(window, text="Start spamming", fg='green', command=start)
btn.place(x=94, y=85)
stopbtn=Button(window, text="Stop spamming", fg = 'red', command=stop)
stopbtn.place(x=94, y=115)
txtfld=Entry(window, bd=2)
txtfld.place(x=80, y=40)
txtfld.insert(0, 'Sell in PEU3')
interval = Entry(window, bd=2)
interval.place(x=80, y=60)
interval.insert(0, '5300')
txl = Label(window, text = 'Spam text')
txl.place(x=20, y=40)
txl = Label(window, text = 'Interval')
txl.place(x=20, y=60)
main = Label(window, text = 'Growtopia spam')
main.place(x=80, y=10)
clr = Checkbutton(text='Random colors', variable = rcl, onvalue = rcl.set(True), offvalue = rcl.set(False))
clr.place(x=80, y=160)
window.title('Growtopia simple spam')
window.geometry("300x200+10+10")
window.mainloop()