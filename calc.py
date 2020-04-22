from tkinter import *
import math

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))
	return


def button_clearF():
	e.delete(0, END)


def button_addF():
	global button
	button = "add"
	first_number = e.get()
	global f_num 
	f_num = int(float(first_number))
	e.delete(0, END)

def button_subtractF():
	global button
	button = "subtract"
	first_number = e.get()
	global f_num
	f_num = int(float(first_number))
	e.delete(0, END)


def button_multiplyF():
	global button
	button = "multiply"
	first_number = e.get()
	global f_num
	f_num = int(float(first_number))
	e.delete(0, END)

def button_divideF():
	global button
	button = "divide"
	first_number = e.get()
	global f_num
	f_num = int(float(first_number))
	e.delete(0, END)


def button_equalF():
	if button == "add":
		second_number = e.get()
		e.delete(0, END)
		e.insert(0, int(float(f_num)) + int(float(second_number)))
	elif button == "subtract":
		second_number = e.get()
		e.delete(0, END)
		e.insert(0, int(float(f_num)) - int(float(second_number)))
	elif button == "multiply":
		second_number = e.get()
		e.delete(0, END)
		e.insert(0, int(float(f_num)) * int(float(second_number)))
	elif button == "divide":
		second_number = e.get()
		e.delete(0, END)
		e.insert(0, int(float(f_num)) / int(float(second_number)))

def button_sqF():
	num = e.get()
	num = int(float(num))
	new_num = math.sqrt(num)
	e.delete(0, END)
	e.insert(0, new_num)

def button_sF():
	num = e.get()
	num = int(float(num))
	new_num = num*num
	e.delete(0, END)
	e.insert(0, new_num)


#Define buttons
frame19 = LabelFrame(root, padx=5, pady=5)
frame19.grid(row=1, column=0)

framebottom = LabelFrame(root, padx=5, pady=5)
framebottom.grid(row=2, column=0)

frameside = LabelFrame(root, padx=5, pady=5)
frameside.grid(row=1, rowspan=4, column=1)

Button_1 = Button(frame19, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(frame19, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(frame19, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(frame19, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(frame19, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(frame19, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(frame19, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(frame19, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(frame19, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(framebottom, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_equal = Button(framebottom, text="=", padx=91, pady=20, command=button_equalF)
button_clear = Button(framebottom, text="Clear", padx=79, pady=20, command=button_clearF)

button_add = Button(frameside, text="+", padx=39, pady=20, command=button_addF)
button_subtract = Button(frameside, text="-", padx=39, pady=20, command=button_subtractF)
button_multiply = Button(frameside, text="*", padx=39, pady=20, command=button_multiplyF)
button_divide = Button(frameside, text="/", padx=39, pady=20, command=button_divideF)
button_s = Button(frameside, text="x²", padx=39, pady=20, command=button_sF)
button_sq = Button(frameside, text="√", padx=39, pady=20, command=button_sqF)

#put buttons on the screen
Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2,)
button_add.grid(row=4, column=0)
button_equal.grid(row=5,column=1, columnspan=2,)

button_subtract.grid(row=1, column=0)
button_multiply.grid(row=2, column=0)
button_divide.grid(row=3, column=0)
button_sq.grid(row=6, column=0)
button_s.grid(row=5, column=0)

root.mainloop()