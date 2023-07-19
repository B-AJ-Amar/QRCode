############################
#import
############################
from tkinter import *
from tkinter import ttk,messagebox
#_______________________
from os import *
#_______________________
from shutil import *
#_______________________
from datetime import *
#_______________________
from qrcode import *
#_______________________
from pyzbar import *
from pyzbar.pyzbar import *
from PIL import Image

############################
#functions
############################

def tk_center(a):
	a.update()
	sh = a.winfo_screenheight()
	sw = a.winfo_screenwidth()
	w  = a.winfo_width()
	h  = a.winfo_height()
	x  = (sw - w)/ 2
	y  = (sh - h)/ 2
	a.geometry("%dx%d+%d+%d" %(w , h , x , y))
 


def creat_qr():
    x = txt.get(1.0, END)
    y = sn.get()
    if not(y[-4:]=='.png' or y[-4:]=='.PNG'):
        y = str(y +'.png')
    print("Content : ",x)
    print("filename :",y)
    qr = make(x)
    qr.save(y)
    
def read_qr() :
    d = de.get()
    if not(d[-4:]=='.png' or d[-4:]=='.PNG'):
        d = str(d +'.png')
        
    d = decode(Image.open(d))
    print("result ==================")
    print(d[0].data.decode())
    messagebox.showinfo(title="result",message=d[0].data.decode())
############################
#window
############################
fon = 'None 10 bold'

win = Tk()
win.geometry('250x290')
win.resizable(0,0)
win.title("MyApp")
tk_center(win)
#________Notobook__________________________________

n = ttk.Notebook(win)
n.pack()

f1 = Frame(n,border=1)
n.add(f1,text='Code')

f2 = Frame(n,border=1)
n.add(f2,text='Decode')


#_____________
s_btn = ttk.Style()
s_btn.configure('TButton',font=fon)

s_lbl = ttk.Style()
s_lbl.configure('TLabel',font= fon )

#____________Frame 1________________________________
sn = StringVar()


lbl = ttk.Label(f1,text='Enter the file name:',font=fon)
ent = ttk.Entry(f1,textvariable=sn)
btn = ttk.Button(f1,text='Done',underline=2,command=creat_qr)

ltx = ttk.Label(f1,text='Enter Text:',font=fon)
txt = Text(f1,height=7,
           bd=2,
           wrap='word')

lbl.pack(pady=5,padx=5,ipady=0)
ent.pack(pady=0,padx=15,ipady=0)
ltx.pack(pady=5,padx=15,ipady=0)
txt.pack(pady=0,padx=15,ipady=0)
btn.pack(pady=10,ipady=0)
Label(f1).pack(pady=100)
Label(f1).pack()
Label(f1).pack()
Label(f1).pack()
#____________Frame 2________________________________
ff2 = Frame(f2)
ff2.pack(pady=80)
de = StringVar()

lbl2 = ttk.Label(ff2,text='Enter the file path :',font=fon)
ent2 = ttk.Entry(ff2,textvariable=de)
btn2 = ttk.Button(ff2,text='Done',underline=2,command=read_qr)


lbl2.pack(pady=5,padx=5)
ent2.pack(pady=0,padx=15)
btn2.pack(pady=10)

#_____________________________________________________
win.mainloop()
