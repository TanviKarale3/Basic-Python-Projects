from tkinter import*
import calendar

text=calendar.calendar(2019)
root=Tk()
root.geometry ("500x600")
root.title("CALENDAR")
label1=Label(root,text="CALENDAR",bg='dark gray',font=("times",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text=text,font="Consolas 10 bold")
l1.grid(row=2,column=1,padx=20)
root.mainloop()