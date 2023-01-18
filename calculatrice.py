
from tkinter import *

history = []


def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


def equals():

    global equation_text

    try:
        total = str(eval(equation_text))
        history.append(equation_text + " = " + total)
        equation_label.set(total)

        equation_text = total
    except:
        equation_label.set("error")

        equation_text = ""


def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


def show_history():
    global history
    print(history)


window = Tk()
window.title("Calculatrice")
window.geometry("400x400")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=(
    'consolas', 20), bg="white", width=17, height=1)
label.pack()

frame = Frame(window)
frame.pack()


button1 = Button(frame, text=1, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(1))
button1.grid(row=0, column=0)


button2 = Button(frame, text=2, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(2))
button2.grid(row=0, column=1)


button3 = Button(frame, text=3, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(3))
button3.grid(row=0, column=2)


button4 = Button(frame, text=4, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(4))
button4.grid(row=1, column=0)


button5 = Button(frame, text=5, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(5))
button5.grid(row=1, column=1)


button6 = Button(frame, text=6, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(7))
button7.grid(row=2, column=0)


button8 = Button(frame, text=8, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(8))
button8.grid(row=2, column=1)


button9 = Button(frame, text=9, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=1, width=5, font=35,
              bg="#2d7fa7", command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=1, width=5, font=35,
               bg="#2d7fa7", command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='x', height=1, width=5, font=35,
                  bg="#2d7fa7", command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='÷', height=1, width=5, font=35,
                bg="#2d7fa7", command=lambda: button_press('/'))
divide.grid(row=3, column=3)

racine = Button(frame, text=' √', height=1, width=5, font=35,
                bg="#2d7fa7", command=lambda: button_press('**.5'))
racine.grid(row=4, column=1)

equal = Button(frame, text='=', height=1, width=5,
               font=35, bg="red", command=equals)
equal.grid(row=4, column=3)

decimal = Button(frame, text='.', height=1, width=5, font=35,
                 bg="#99928a", command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

percentage = Button(frame, text='%', height=1, width=5, font=35,
                    bg="#2d7fa7", command=lambda: button_press('*100/'))
percentage.grid(row=4, column=0)

history_btn = Button(frame, text="H", command=show_history,
                     height=1, width=5, font=35, bg="#2d7fa7")
history_btn.grid(row=4, column=2)

clear = Button(frame, text='C', height=1, width=5, font=35, command=clear)
clear.grid(row=3, column=2)
clear.pack

window.mainloop()
