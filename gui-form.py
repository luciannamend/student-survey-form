import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

class myForm (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("College")
        self.initialize_form()

    def initialize_form(self):

        style = Style()
        style.configure('BW.TLabel', background='#E6E6FA')

        self.frame = Frame(self, width=800, height=800, style="BW.TLabel")
        self.frame.grid()
        self.frame['padding'] = (20, 30)
        self.frame['borderwidth'] = 20
        self.frame['relief'] = 'sunken'


        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        # ================================= TITLE ============================================
        title_text = 'Student Survey'
        self.lbl_title = Label(self.frame, text=title_text, font=('Lucida font',16), style="BW.TLabel")
        self.lbl_title.grid(column=1, row=0, sticky=(W))

        # ================================= ENTRY NAME =======================================
        self.lbl_full_name = Label(self.frame, text='Full name:', style="BW.TLabel")
        self.lbl_full_name.grid(column=0, row=1, sticky=(W, E))

        self.username = StringVar(value='Lucianna Mendonca')
        self.name = Entry(self.frame, textvariable=self.username)
        self.name.grid(column=1, row=1, sticky=W)

        # ================================= RADIOBUTTON RESIDENCY =============================
        Label(self.frame, text='Residency:', style="BW.TLabel").grid(column=0, row=2, sticky=(W))

        self.residency = StringVar(value='dom')
        panel = Frame(self.frame)
        panel.grid(column=1, row=2, rowspan=2, sticky=(W, E))
        Radiobutton(panel, text='Domestic', variable=self.residency, value='dom').grid(column=0, row=0, sticky=W)
        Radiobutton(panel, text='International', variable=self.residency, value='intl').grid(column=0, row=1, sticky=W)
        
        # ================================= COMBOBOX PROGRAMS ==================================
        Label(self.frame, text='Program:', style="BW.TLabel").grid(column=0, row=4, sticky=(W, E))
        
        self.program = StringVar()
        self.combo = Combobox(self.frame, textvariable=self.program)
        self.combo['values']= ('AI', 'Gaming', 'Health', 'Software')
        self.combo.grid(column=1, row=4, sticky=(W, E))
        self.combo.current(2)        

        # ================================= CHECKBUTTON COURSES ================================
        Label(self.frame, text='Courses:', style="BW.TLabel").grid(column=0, row=6, sticky=(W))

        panel = Frame(self.frame, style="BW.TLabel") 
        panel.grid(column=1, row=6, rowspan=4, sticky=(W))

        self.comp100 = StringVar(value='COMP100')
        self.comp213 = StringVar()
        self.comp120 = StringVar()

        Checkbutton(panel, text='Programming I', variable=self.comp100, onvalue='COMP100', offvalue='').grid(column=0, row=1, sticky=W)
        Checkbutton(panel, text='Web Page Design', variable=self.comp213, onvalue='COMP213', offvalue='').grid(column=0, row=2, sticky=W)
        Checkbutton(panel, text='Software Engineering', variable=self.comp120, onvalue='COMP120', offvalue='').grid(column=0, row=3, sticky=W)

        # ================================== BUTTONS ==========================================
        self.reset_button = Button(self.frame, text='Reset', command=self.reset_form)
        self.reset_button.grid(column=0, row=15, sticky=(W, E))

        self.ok_button = Button(self.frame, text='Ok', command=self.read_form)
        self.ok_button.grid(column=1, row=15)

        self.exit_button = Button(self.frame, text='Exit', command=self.quit)
        self.exit_button.grid(column=2, row=15, sticky=(W, E))

    # ================================= FUNCTIONS ============================================
    def reset_form(self):
        response = messagebox.askyesno(title='Reset Form', message='Are you sure you want to reset the form?')
        if response:
            self.username.set('Lucianna Mendonca')
            self.residency.set('dom')
            self.program.set('Health')
            self.comp100.set('COMP100')
            self.comp213.set('')
            self.comp120.set('')

    def read_form(self):
        message =f'{self.username.get()}\n{self.program.get()}\n{self.residency.get()}\n{self.comp100.get()} {self.comp120.get()} {self.comp213.get()}'
        messagebox.showinfo(title='Form Information', message=message)


if __name__ == "__main__":
    app = myForm()
    app.mainloop()