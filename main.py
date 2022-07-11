import tkinter as tk

# Calculation and Display Change Functions

#Changes/adds to the display number at top of calculator
def button_press(button_num):
    if display['text'] == '0':
        display['text'] = str(button_num)
    else:
        display['text'] = display['text'] + str(button_num)
    secondary_display['text'] += str(button_num)

#sets first num to be used in math operation & resets the display to 0 for next input, sets what the math operation will be.
#Checks if first num has already been set, if so it runs equals_button function before continuing with is normal function.
def calc_button(symbol):
    global num1, symbol_pressed, display
    if num1 == 0:
        num1 = float(display['text'])
        display['text'] = '0'
        symbol_pressed = symbol
        secondary_display['text'] = str(num1) + " " + symbol_pressed
    elif num1 > 0:
        equals_button()
        display['text'] = '0'
        symbol_pressed = symbol
        secondary_display['text'] = str(num1) + " " + symbol_pressed
        

#Sets second num to be used in math operation & performs math operation based on calc_button perviously selected.
def equals_button():
    global num1, num2, symbol_pressed
    num2 = float(display['text'])
    if symbol_pressed == '*':
        display['text'] = str(num1 * num2)
        secondary_display['text'] = str(num1) + " " + symbol_pressed + str(num2)
        num1 = num1 * num2
    elif symbol_pressed == '/':
        display['text'] = str(num1 / num2)
        secondary_display['text'] = str(num1) + " " + symbol_pressed + str(num2)
        num1 = num1 / num2
    elif symbol_pressed == '+':
        display['text'] = str(num1 + num2)
        secondary_display['text'] = str(num1) + " " + symbol_pressed + str(num2)
        num1 = num1 + num2
    elif symbol_pressed == '-':
        display['text'] = str(num1 - num2)
        secondary_display['text'] = str(num1) + " " + symbol_pressed + str(num2)
        num1 = num1 - num2
    symbol_pressed = ''

#Resets and clears all previous entered info
def clear_button():
    global num1, num2, symbol_pressed, display
    num1 = 0
    num2 = 0
    symbol_pressed = ''
    display['text'] = '0'


# setting global variables:


num1 = 0
num2 = 0
symbol_pressed = ''
num_is_stored = False



# intit window


window = tk.Tk()
window.geometry('400x400')


display = tk.Label(text='0')
display.grid(column=0,
             row=1,
             columnspan=4)

secondary_display = tk.Label(text='')
secondary_display.grid(column=0,
                        row=0,
                        columnspan=4,
                        sticky='E')

button1 = tk.Button(text='1', command=lambda: button_press(1))
button1.grid(column=0,
             row=2,
             sticky='nsew')

button2 = tk.Button(text='2', command=lambda: button_press(2))
button2.grid(column=1,
             row=2,
             sticky='nsew')

button3 = tk.Button(text='3', command=lambda: button_press(3))
button3.grid(column=2,
             row=2,
             sticky='nsew')

button4 = tk.Button(text='4', command=lambda: button_press(4))
button4.grid(column=0,
             row=3,
             sticky='nsew')

button5 = tk.Button(text='5', command=lambda: button_press(5))
button5.grid(column=1,
             row=3,
             sticky='nsew')

button6 = tk.Button(text='6', command=lambda: button_press(6))
button6.grid(column=2,
             row=3,
             sticky='nsew')

button7 = tk.Button(text='7', command=lambda: button_press(7))
button7.grid(column=0,
             row=4,
             sticky='nsew')

button8 = tk.Button(text='8', command=lambda: button_press(8))
button8.grid(column=1,
             row=4,
             sticky='nsew')

button9 = tk.Button(text='9', command=lambda: button_press(9))
button9.grid(column=2,
             row=4,
             sticky='nsew')

button0 = tk.Button(text='0', command=lambda: button_press(0))
button0.grid(column=1,
             row=5,
             sticky='nsew')

plus_button = tk.Button(text='+', command=lambda: calc_button('+'))
plus_button.grid(column=3,
                 row=2,
                 sticky='nsew')

minus_button = tk.Button(text='-', command=lambda: calc_button('-'))
minus_button.grid(column=3,
                  row=3,
                  sticky='nsew')

multiplication_button = tk.Button(text='*', command=lambda: calc_button('*'))
multiplication_button.grid(column=3,
                           row=4,
                           sticky='nsew')

division_button = tk.Button(text='/', command=lambda: calc_button('/'))
division_button.grid(column=3,
                     row=5,
                     sticky='nsew')

equal_button = tk.Button(text='=', command=equals_button)
equal_button.grid(column=2,
                  row=5,
                  sticky='nsew')

c_button = tk.Button(text='C', command=clear_button)
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
