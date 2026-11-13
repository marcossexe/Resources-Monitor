import tkinter as tk
import ctypes
from time import time
window = tk.Tk( )
lib = ctypes.CDLL("./libfunctions.so")
lib_proc = ctypes.CDLL("./libproc.so")
lib_proc.count_proc.restype = ctypes.c_int
lib_proc.count_active_proc.restype = ctypes.c_int
lib.display_memory.restype = ctypes.c_char_p
lib.display_cpu_usage.restype = ctypes.c_double
lib.display_cpu_temp.restype = ctypes.c_int
window.title("Hardware Monitor")
window.geometry("500x300")
window.resizable("False", "False" )
window.configure(bg ="gray")
canvas = tk.Canvas(window, width= 500, height=50, bg= "black"  )
canvas.place(x= 0, y=250)
cpu_data =[]
counter =0
var = 0
fonts = "courier"

frame_mem = tk.Frame(window, padx =5, pady=2, bg="green" , relief= "raised", width=245)
frame_mem.grid(column= 0, row=0)
label_text = tk.Label(frame_mem, fg="green"); label_text.pack()
def get_memory():
	free = lib.display_memory()
	label_text.config(text=free, font = fonts)
	
	window.after(500, get_memory)
	
		
x0, y0, x1, y1 = 0, 50 , 8, 50 
##################################################################################

framecpu = tk.Frame(window, padx= 5, pady=2, bg="black",relief = "raised", width=245)
framecpu.place(x= 175, y= 225)
label_cpu_act= tk.Label(framecpu); label_cpu_act.pack()	

def get_cpu():
	value = lib.display_cpu_usage()
	global cpu_data
	cpu_data.append(value)
	global counter
	y_coordinatte = cpu_data[counter]
	label_cpu_act.config(fg = "green", text="CPU USAGE " + f"{value:.2f}" + "%")
	global x0, x1, y0, y1
	x0 , y0, x1, y1 = x0+8  ,50 ,x1+8, 50 - (y_coordinatte /2)
	canvas.create_rectangle( x0, y0, x1, y1,fill="#00fd00")
	
	
	counter = counter +1
	if  counter == 50:
		canvas.delete("all")
		counter=0
		cpu_data = []
		var = 0
		x0,y0, x1, y1= 0, 50, 8, 50
		  
		

	
	
	window.after(200, get_cpu)
	
########################################################################################

frame_temp = tk.Frame(window, padx =5, pady=2,relief = "raised", bg="green", width = 245)
frame_temp.grid(column=1, row=0)
label_cpu_temp = tk.Label(frame_temp, fg= "green"); label_cpu_temp.pack()	


def get_cpu_temp():
	value = lib.display_cpu_temp()
	label_cpu_temp.config(text="CPU Temperature " +str(value)+ "C°" )
	window.after(500, get_cpu_temp)
#######################################################################################

def count_proc():
	total = lib_proc.count_proc()
	
	label_total = tk.Label(frame2,text="Processes " + str(total), fg = "green" ,bg="white").grid()
frame2 = tk.Frame(window, padx =5, pady=2, bg="green",width = 245, relief= "raised" )
frame2.grid(column=0, row=1)	
	

def count_active_proc():
	total = lib_proc.count_active_proc()
	frame3 = tk.Frame(window, padx =5, pady=2, bg="green", width= 245, relief= "raised")
	frame3.grid(column=1, row=1)
	label_total2 = tk.Label(frame3,text = "Active Processes " + str(total), fg="green" ).grid(column= 0, row=1)




	


get_memory()
get_cpu_temp()

get_cpu()

count_proc()
count_active_proc()
window.mainloop()


