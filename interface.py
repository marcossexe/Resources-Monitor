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

label_text = tk.Label(window); label_text.pack()
label_cpu = tk.Label(window); label_cpu.pack()
label_cpu_temp = tk.Label(window ); label_cpu_temp.pack()
label_total = tk.Label(window ); label_total.pack()
label_total2 = tk.Label(window ); label_total2.pack()

def memory():
	text = lib.display_memory()
	label_text.config(text =f"Free Memory: {text}")
	window.after(1000,memory)
def cpu():
	value = lib.display_cpu_usage()
	label_cpu.config(text =f"CPU Activity: {value:.1f}%")
	window.after(1000, cpu)	
	
def cpu_temp():
	value = lib.display_cpu_temp()
	label_cpu_temp.config(text =f"CPU Temperatur:{value}")
	window.after(1000, cpu_temp) 
def count_proc():
	total = lib_proc.count_proc()
	label_total.config(text =f"Total Processes: {total}")
	
	

def count_active_proc():
	total = lib_proc.count_active_proc()
	label_total2.config(text =f"Total Active  Processes: {total}")
	
memory()
cpu()
cpu_temp()
count_proc()
count_active_proc()
window.mainloop()

