from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tm
import inflect
from selenium import webdriver as wd
import time


class StartFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("200x100")
        master.resizable(width=False,height=False)

        self.EmailDomainSetupButton = ttk.Button(master,width = 28,text = "Company Email Domain Setup",command = self.OpenEmailDomainSetupFrame).pack(pady=4)
        self.EmailDomainSetupButton = ttk.Button(master,state = DISABLED,text = "Company Formation Setup",command = self.OpenFormationsWindow).pack(pady = 4)
        self.EmailDomainSetupButton = ttk.Button(master,state = DISABLED,text = "PAYE Registration").pack(pady = 4)
                                                                                

    def OpenEmailDomainSetupFrame(self):
        self.master.destroy()
        root = Tk()
        NextWin = EmailDomainSetupFrame(root)
        root.mainloop()

    def OpenFormationsWindow(self):
        self.master.destroy()
        root = Tk()
        #NextWin = WebFormFrame(root)
        NextWin = FormationsWindow(root)
        root.mainloop()
        

class EmailDomainSetupFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("419x290")
        #master.resizable(width = 0,height = 0)
        Choice = tk.IntVar()

        self.IndivFrame = ttk.Frame(master,width=40,height=40)
        self.IndivFrame.pack()
        self.IndivRadio = ttk.Radiobutton(self.IndivFrame,variable=Choice,value=1,command = self.IndivRadioCmd)
        self.IndivRadio.pack(side=LEFT,anchor = N,padx = 5,pady = 5)
        self.IndivLabel = Label(self.IndivFrame,text = "Individual")
        self.IndivLabel.pack(side = LEFT,anchor = N,padx = 0,pady = 5)
        self.IndivEntry = ttk.Entry(self.IndivFrame,width=10,state=DISABLED)
        self.IndivEntry.pack(side = LEFT,anchor = N,padx = 5,pady = 5)
        self.RunButton = ttk.Button(self.IndivFrame,text = "Run",command = self.CreateEmails)
        self.RunButton.pack(side = LEFT,anchor = N,padx = 10,pady = 5)

        self.RangeFrame = ttk.Frame(master)
        self.RangeFrame.pack()
        self.RangeRadio = ttk.Radiobutton(self.RangeFrame,variable=Choice,value=2,command = self.RangeRadioCmd).pack(side = LEFT,anchor = N,padx = 5,pady = 5)
        self.RangeRadioLabel = Label(self.RangeFrame,text = "Range")
        self.RangeRadioLabel.pack(side = LEFT,anchor = N,pady = 5)
        self.RangeRadioEntry1 = ttk.Entry(self.RangeFrame,width=5,state = DISABLED)
        self.RangeRadioEntry1.pack(side = LEFT,anchor = N,padx = 4,pady = 5)
        self.RangeSepLabel = Label(self.RangeFrame,text = "-")
        self.RangeSepLabel.pack(side = LEFT,anchor = N,pady = 5)
        self.RangeRadioEntry2 = ttk.Entry(self.RangeFrame,width=5,state=DISABLED)
        self.RangeRadioEntry2.pack(side = LEFT,anchor = N,pady = 5)
        self.ReturnButton = ttk.Button(self.RangeFrame,text = "Return",command = self.ReturnToStart)
        self.ReturnButton.pack(side = LEFT,anchor = N,padx = 13,pady = 5)
             
        self.tree = ttk.Treeview(master,columns = ("Record #","EmailAddress","Status","Time Taken"), show = 'headings')
        self.tree.pack(side=LEFT) 
        self.tree.column("Record #",width=50)
        self.tree.column("EmailAddress",width=220)
        self.tree.column("Status",width = 80)
        self.tree.column("Time Taken",width = 50)
        self.tree.heading("Record #",text="#")
        self.tree.heading("EmailAddress",text="Email Address Created")
        self.tree.heading("Status",text="Status")
        self.tree.heading("Time Taken",text="Time")
        
        vsb = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT,fill="y")
        self.tree.configure(yscrollcommand=vsb.set)
        
    def ReturnToStart(self):
        self.master.destroy()
        root = Tk()
        StartFrame(root)
        root.mainloop()

    def RangeRadioCmd(self):
        self.RangeRadioEntry1.config(state = ACTIVE)
        self.RangeRadioEntry2.config(state = ACTIVE)
        self.IndivEntry.config(state=DISABLED)
        
    def IndivRadioCmd(self):
        self.RangeRadioEntry1.config(state = DISABLED)
        self.RangeRadioEntry2.config(state = DISABLED)
        self.IndivEntry.config(state=ACTIVE)

    def CreateEmails(self):
        
        driver = wd.Chrome(executable_path=r"C:\Users\valom\chromedriver.exe")
        driver.get("https://login.one.com/cp/")
        driver.find_element_by_name("displayUsername").send_keys("accounts@apsnational.co.uk")
        driver.find_element_by_name("password1").send_keys("Leicester123")
        driver.find_element_by_class_name("oneButton").click()
        driver.get("https://www.one.com/admin/create-account.do")

        LB = int(self.RangeRadioEntry1.get())
        #UB = int(self.RangeRadioEntry2.get())
        #for n in range(LB,UB+1):
        Prefix = self.getWordInEmail(LB).replace("-","")

        driver.find_element_by_id("name").send_keys("calm")

        


class FormationsWindow(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("300x300")
        
        #self.MenuLabel = Label(master,text = "Menu")
        #self.FormationButton = Button(master,text = "Formations Registration")
        #self.FormationButton.pack()

        canvas = Canvas(master,highlightthickness=4)
        
        #self.OneCom = Button(canvas, text = "One Email upload",command = self.FormationsScreen)
        #self.OneCom.pack()

        self.label_username = Label(canvas, text="Username")
        self.label_password = Label(canvas, text="Password")

        self.entry_username = Entry(canvas)
        self.entry_password = Entry(canvas, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        #self.RecordSheet = Me(self)
        #self.RecordSheet.grid(row = 5)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        #self.pack()

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")
            
class WebFormFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("300x300")
        self.RecordSheet = Listbox(master)
        self.RecordSheet.insert(END,"a list entry")
        
        BtnCanvas = Canvas(master).pack(side = LEFT,anchor = N,pady = 5)
        self.ContactDetailsBtn = Button(Canvas,text = "Contact Details").pack()
        self.AddressDetailsBtn = Button(Canvas,text = "Address Details").pack()
        
        self.RecordSheet.grid(column = 1,row = 0)
        #self.AddressDetailsBtn.grid(row = 1)
        #self.ContactDetailsBtn.grid(row = 0,padx = 5,pady = 5)
        
    def ContactAddressSelect(self):
        root = Tk()
        ContactAddressFrame(root)
        root.mainloop()

class ContactAddressFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry("300x300")
        Firstname = StringVar()
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        
    


root = Tk()
Window = StartFrame(root)
root.mainloop()
