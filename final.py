# Calculator
from tkinter import *
import tkinter.font as tkFont

class Calculator():

    def __init__(self):
        self.expression = ""
    
    def press(self, num):       
 
    # concatenation of string
        self.expression = self.expression + str(num)
 
    # update the expression by using set method
        self.equation.set(self.expression)

    def equalpress(self):
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.
    
        # Put that code inside the try block
        # which may generate the error
        try:
            
            # eval function evaluate the expression
            # and str function convert the result
            # into string
            total = str(eval(self.expression))
    
            self.equation.set(total)
    
            # initialize the expression variable
            # by empty string
            self.expression = ""
    
        # if error is generate then handle
        # by the except block
        except:
    
            self.equation.set(" error ")
            self.expression = ""
    def clear(self):
        self.expression = ""
        self.equation.set("")



    def drive(self):
        gui = Tk()

        f1 = tkFont.Font(size = 36, family = "Arial")
        f2 = tkFont.Font(size = 24, family = "Arial")
 
        # set the background colour of GUI window
        gui.configure(background="#c5b8a5")
    
        # set the title of GUI window
        gui.title("Calculator")
        
        # StringVar() is the variable class
        # we create an instance of this class
        self.equation = StringVar()
    
        # create the text entry box for
        # showing the expression .
        self.expression_field = Entry(gui, textvariable = self.equation, bd = 10, font = f1 )
    
        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        self.expression_field.grid(columnspan=4, ipadx=70)
    
        # create a Buttons and place at a particular
        # location inside the root window .
        # when user press the button, the command or
        # function affiliated to that button is executed .

        button1 = Button(gui, text=' 1 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(1), height=2, width=5, font = f2)

        button2 = Button(gui, text=' 2 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(2), height=2, width=5, font = f2)

        button3 = Button(gui, text=' 3 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(3), height=2, width=5, font = f2)

        button4 = Button(gui, text=' 4 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(4), height=2, width=5, font = f2)     

        button5 = Button(gui, text=' 5 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(5), height=2, width=5, font = f2)

        button6 = Button(gui, text=' 6 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(6), height=2, width=5, font = f2)

        button7 = Button(gui, text=' 7 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(7), height=2, width=5, font = f2)

        button8 = Button(gui, text=' 8 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(8), height=2, width=5, font = f2)

        button9 = Button(gui, text=' 9 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(9), height=2, width=5, font = f2)

        button0 = Button(gui, text=' 0 ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press(0), height=2, width=5, font = f2)

        plus = Button(gui, text=' + ', fg='black', bg='#c5b8a5',
                    command=lambda: self.press("+"), height=2, width=5, font = f2)   

        minus = Button(gui, text=' - ', fg='black', bg='#c5b8a5',
                    command=lambda: self.press("-"), height=2, width=5, font = f2)

        multiply = Button(gui, text=' * ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press("*"), height=2, width=5, font = f2)
    
        divide = Button(gui, text=' / ', fg='black', bg='#c5b8a5',
                        command=lambda: self.press("/"), height=2, width=5, font = f2)
    
        equal = Button(gui, text=' = ', fg='black', bg='#c5b8a5',
                    command=self.equalpress, height=2, width=5, font = f2)
    
        clear = Button(gui, text='AC', fg='black', bg='#c5b8a5',
                    command=self.clear, height=2, width=5, font = f2)
    
        Decimal= Button(gui, text='.', fg='black', bg='#c5b8a5',
                        command=lambda: self.press('.'), height=2, width=5, font = f2)

        button1.grid(row=2, column=0, sticky = NE + SW)
    
        button2.grid(row=2, column=1, sticky = NE + SW)
    
        button3.grid(row=2, column=2, sticky = NE + SW)
    
        button4.grid(row=3, column=0, sticky = NE + SW)
        
        button5.grid(row=3, column=1, sticky = NE + SW)

        button6.grid(row=3, column=2, sticky = NE + SW)

        button7.grid(row=4, column=0, sticky = NE + SW)
    
        button8.grid(row=4, column=1, sticky = NE + SW)
    
        button9.grid(row=4, column=2, sticky = NE + SW)
    
        button0.grid(row=5, column=0, sticky = NE + SW)
    
        plus.grid(row=2, column=3, sticky = NE + SW)
       
        minus.grid(row=3, column=3, sticky = NE + SW)

        multiply.grid(row=4, column=3, sticky = NE + SW)

        divide.grid(row=5, column=3, sticky = NE + SW)

        equal.grid(row=5, column=2, sticky = NE + SW)
    
        clear.grid(row=5, column='1', sticky = NE + SW)
    
        Decimal.grid(row=6, column=0, sticky = NE + SW)

        gui.mainloop()
    
cal = Calculator()
cal.drive()



