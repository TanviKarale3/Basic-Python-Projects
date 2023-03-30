from tkinter import*
class Mywin(Tk):
    def __init__(self):
        super().__init__()
        data="Email Slicer"
        fnt="TimesRoman 40 bold"
        self.Lbl=Label(self,text=data,font=fnt)
        self.Lbl.pack()
win=Mywin()
win.configure(background="Red",cursor="cross")
win.geometry("500x300")
win.mainloop()
emailID = input("Enter the email id: ")
username = emailID[:emailID.index('@')]
#print(username)
domain = emailID[emailID.index('@')+1:]
print("Username = "+username)
print("Domain name = "+domain)