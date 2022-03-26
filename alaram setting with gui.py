



# --------------------------PART 1----------------
from tkinter import*
from PIL import Image, ImageTk
from os import *
from datetime import *
from time import *
from tkinter import messagebox

# ------------PART 4----------------
def clear():                        #---------This function is called in line no.47---------------
    entry_year.delete(0,END)
    entry_month.delete(0,END)
    entry_day.delete(0,END)
    
    entry_hour.delete(0,END)
    entry_minute.delete(0,END)
    entry_second.delete(0,END)

# -------------PART 3-------------

def run():                        #-------------------This function is called in line no.127------------
    txt_year.get()
    txt_month.get()
    txt_day.get()

    txt_hour.get()
    txt_minute.get()
    txt_second.get()
    
    if txt_year.get()=='' or txt_month.get()==''or txt_day.get()=='':
        messagebox.showerror('Error','All entries are to be filled.')
        
    elif txt_hour.get()=='' or txt_minute.get()==''or txt_second.get()=='':
        messagebox.showerror('Error','All entries are to be filled.',parent = root)
    


    else:
        n = 1
        while n>0:
            try:
                if localtime().tm_hour == int(txt_hour.get()) and localtime().tm_min == int(txt_minute.get()) and localtime().tm_sec == int(txt_second.get()):
                    clear()
                    startfile('"E:\Songs\Aerosmith - Amazing.mp3"')
                    break

                else:
                    n += 1
        
            except Exception as es:
                messagebox.showerror('Error',f'Error due to{str(es)}',parent=root)
                break


# ---------------PART 2--------------Creation of the User Interface...........
root = Tk()
root.geometry('1350x600')
root.config(bg='grey')


image = Image.open('E:\\clock for gui.jpg') # Image varies along with the devices and drives.
photo = ImageTk.PhotoImage(image)
l1 = Label(root, image=photo)
l1.place(x=0,y=0)

head = Label(root, text='Set Alaram:',font=('times new roman',25),fg='dark orange',bg='black',borderwidth=6,relief=SUNKEN)
head.place(x=970+40+20,y=25)

l2 = Label(root,text='Set Date:',font='comiscanms 20 bold',fg='black',bg='gray')
l2.place(x=820,y=150)

l4 = Label(root,text='Set Time:',font='comiscanms 20 bold',fg='black',bg='gray')
l4.place(x=820,y=250)

# -------------Creating the entries for date input-------------
txt_year = StringVar()
entry_year = Entry(root,borderwidth=3,relief=SUNKEN,width=5,font='comiscanms 18 bold',textvariable=txt_year)
entry_year.place(x=960,y=150)

l5 = Label(root, font='comiscanms 10 bold',text='YY')
l5.place(x=980,y=120)

txt_month = StringVar()
entry_month = Entry(root,borderwidth=3,relief=SUNKEN,width=5,font='comiscanms 18 bold',textvariable=txt_month)
entry_month.place(x=1060,y=150)

l6 = Label(root, font='comiscanms 10 bold',text='MM')
l6.place(x=1080,y=120)

txt_day = StringVar()
entry_day = Entry(root,borderwidth=3,relief=SUNKEN,width=5,font='comiscanms 18 bold',textvariable=txt_day)
entry_day.place(x=1160,y=150)


l7 = Label(root, font='comiscanms 10 bold',text='DD')
l7.place(x=1180,y=120)

# ------------Creating the entries for time input-------------

txt_hour = StringVar()
entry_hour = Entry(root,borderwidth=3,relief=SUNKEN,width=5,font='comiscanms 18 bold',textvariable=txt_hour)
entry_hour.place(x=960,y=220+30)


l8 = Label(root, font='comiscanms 10 bold',text='HH')
l8.place(x=980,y=220)

txt_minute = StringVar()
entry_minute = Entry(root,borderwidth=3,relief=SUNKEN,width=5,font='comiscanms 18 bold',textvariable=txt_minute)
entry_minute.place(x=1060,y=250)

l9 = Label(root, font='comiscanms 10 bold',text='MM')
l9.place(x=1080,y=220)

txt_second = StringVar()
entry_second = Entry(root,borderwidth=3,relief=SUNKEN,width=5,font='comiscanms 18 bold',textvariable=txt_second)
entry_second.place(x=1160,y=250)

l10 = Label(root, font='comiscanms 10 bold',text='SS')
l10.place(x=1180,y=220)


but = Button(root,text='Run',font=('times new roman',25),bg='black',fg='orange',width=7,command=run)
but.place(x=970+40+20,y=340)



root.mainloop() #-------------------End of Part 2--------------


