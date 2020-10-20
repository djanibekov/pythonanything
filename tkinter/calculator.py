from tkinter import *

class Calculator(object):
    additional_buttons = ['x', '/', '-']
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.font_big = ('Verdana', 40)
        self.process = None
        self.f_number = None

    def template(self):
        self.entry = Entry(self.root, width=11, font=self.font_big, bg='light blue')
        self.entry.grid(row=0, column=0, columnspan=4)
        buttons = []
        for i in range(3):
            for j in range(4):
                if(j == 3):
                    buttons.append(Button(self.root, 
                    text=self.additional_buttons[i], 
                    width=11, height=3, 
                    bg="light gray",             
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff",
                    command=lambda op=self.additional_buttons[i]: self.button_operation(op)
                    ))
                else:
                    number = 3*(3-i)-j
                    buttons.append(Button(self.root, 
                    text=number, 
                    width=11, height=3, 
                    bg="white",
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff",
                    command=lambda number=number: self.button_add(number)))
                buttons[4*i+j].grid(row=i+1, column=j)

        button1 = Button(self.root, text=".", width=11, height=3, bg="white",             
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff")
        button2 = Button(self.root, text="0", width=11, height=3, bg="white", command=lambda: self.button_add(0),            
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff",)
        button3 = Button(self.root, text="=", width=11, height=3, bg="blue", fg="white", 
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff",
                    command=self.button_equal)
        button4 = Button(self.root, text="+", width=11, height=3, bg="light gray",
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff",
                    command=lambda: self.button_operation('+'))
        button5 = Button(self.root, text="Clear", width=51, height=3, bg="light gray",
                    highlightthickness=4, 
                    highlightcolor="#37d3ff", 
                    highlightbackground="#37d3ff",
                    command=self.clear)

        button1.grid(row=4, column=0)
        button2.grid(row=4, column=1)
        button3.grid(row=4, column=2)
        button4.grid(row=4, column=3)
        button5.grid(row=5, column=0, columnspan=4)

    def button_add(self, number):
        self.entry.insert(END, number)
        return

    def button_operation(self, operation):
        self.process = operation
        self.f_number = int(self.entry.get())
        self.entry.delete(0, END)    
        return

    def button_equal(self):
        entry = self.entry
        s_number = int(entry.get())
        entry.delete(0, END)
        if self.process == '+':
            entry.insert(0, self.f_number + s_number)
        elif self.process == '-':
            entry.insert(0, self.f_number - s_number)
        elif self.process == 'x':
            entry.insert(0, self.f_number * s_number)
        elif self.process == '/':
            entry.insert(0, self.f_number // s_number)
        return

    def clear(self):
        self.entry.delete(0, END)
        return

    def run(self):
        self.template()
        self.root.mainloop()






simple_calculator = Calculator("Simple Calculator")
simple_calculator.run()