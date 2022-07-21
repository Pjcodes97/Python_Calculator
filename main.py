from tkinter import *
from tkinter.ttk import *
#Global variable to adjust Calculator after first eval is performed
is_result = False

# Calculation and Display Change Functions

#Changes/adds to both display numbers at the top of the calculator
def button_press(button_num):
    global is_result
    if is_result == False:
        if display['text'] == '0':
            display['text'] = str(button_num)
        else:
            display['text'] = display['text'] + str(button_num)
        secondary_display['text'] += str(button_num)
    elif is_result == True:
        display['text'] = str(button_num)
        secondary_display['text'] = str(button_num)
        is_result = False

    

#Creates equation in secondary display to be evaluated by equals_button function, resets display for next number.
def calc_button(symbol):
    global is_result, secondary_display, display
    is_result = False
    secondary_display['text'] += str(symbol)
    display['text'] = '0'

    
        

#Evals equation created in secondary display and returns the result in both displays for future operations.
def equals_button():
    global display, secondary_display, is_result
    try:
        result = eval(secondary_display['text'])
        display['text'] = str(result)
        secondary_display['text'] = str(result)
        is_result = True
    except ZeroDivisionError:
        print("Can't divide by Zero")
        display['text'] = "ERROR CAN'T DIVIDE BY ZERO"
    

    

#Resets and clears all previous entered info
def clear_button():
    global display, secondary_display
    display['text'] = '0'
    secondary_display['text'] = ''


# intit window
window = Tk()
window.geometry('400x400')


display = Label(text='0')
display.grid(column=0,
             row=1,
             columnspan=4)

secondary_display = Label(text='')
secondary_display.grid(column=0,
                        row=0,
                        columnspan=4,
                        sticky='E')

button1 = Button(text='1', command=lambda: button_press(1))
button1.grid(column=0,
             row=2,
             sticky='nsew')

button2 = Button(text='2', command=lambda: button_press(2))
button2.grid(column=1,
             row=2,
             sticky='nsew')

button3 = Button(text='3', command=lambda: button_press(3))
button3.grid(column=2,
             row=2,
             sticky='nsew')

button4 = Button(text='4', command=lambda: button_press(4))
button4.grid(column=0,
             row=3,
             sticky='nsew')

button5 = Button(text='5', command=lambda: button_press(5))
button5.grid(column=1,
             row=3,
             sticky='nsew')

button6 = Button(text='6', command=lambda: button_press(6))
button6.grid(column=2,
             row=3,
             sticky='nsew')

button7 = Button(text='7', command=lambda: button_press(7))
button7.grid(column=0,
             row=4,
             sticky='nsew')

button8 = Button(text='8', command=lambda: button_press(8))
button8.grid(column=1,
             row=4,
             sticky='nsew')

button9 = Button(text='9', command=lambda: button_press(9))
button9.grid(column=2,
             row=4,
             sticky='nsew')

button0 = Button(text='0', command=lambda: button_press(0))
button0.grid(column=1,
             row=5,
             sticky='nsew')

plus_button = Button(text='+', command=lambda: calc_button('+'))
plus_button.grid(column=3,
                 row=2,
                 sticky='nsew')

minus_button = Button(text='-', command=lambda: calc_button('-'))
minus_button.grid(column=3,
                  row=3,
                  sticky='nsew')

multiplication_button = Button(text='*', command=lambda: calc_button('*'))
multiplication_button.grid(column=3,
                           row=4,
                           sticky='nsew')

division_button = Button(text='/', command=lambda: calc_button('/'))
division_button.grid(column=3,
                     row=5,
                     sticky='nsew')

equal_button = Button(text='=', command=equals_button)
equal_button.grid(column=2,
                  row=5,
                  sticky='nsew')

c_button = Button(text='C', command=clear_button)
c_button.grid(column=0,
              row=5,
              sticky='nsew')

#establish rows in list then make all rows responsive (except for first row with secondary_display button, taken care of seperately)
rows = [1, 2, 3, 4, 5]
for row in rows:
    window.rowconfigure(row, weight=2)

#establish columns in list then make all columns responsive
columns = [0, 1, 2, 3]
for column in columns:
    window.columnconfigure(column, weight=2)

window.rowconfigure(0, weight=1)

window.mainloop()
