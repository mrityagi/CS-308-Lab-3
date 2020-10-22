from tkinter import *
from tkinter.ttk import * 
from ttkthemes import themed_tk as tk
from tkinter.filedialog import askopenfilename as opf


global Load_file_path 
global keywords_file_path 

Load_file_path = ""
keywords_file_path = ""
	
def get_path(keyword):
	global Load_file_path 
	global keywords_file_path 
	if keyword:
		keywords_file_path = opf()	
	else:
		Load_file_path = opf() 

		
		
	
def edit_file(path):
		window = Tk()
		window.title("Editor")
		text = Text(window, padx=5, pady=5)
		text.pack()
		if path == "":
			text.insert(END,"Please select the File")
			exit = Button(window, text="Exit", command=lambda: window.destroy()).pack()	
		else:
			file = open(path)
			for line in file:
				text.insert(END,line)
			file.close()
				
			save = Button(window, text="Save", command=lambda: save()).pack()
			
			def save():
				file = open(path, "w")
				new = text.get(1.0,END)
				file.write(new)
				file.close()
				window.destroy()
		

	
def make_gui():
    box = tk.ThemedTk() 
    box.get_themes()
    box.set_theme("radiance")
    box.columnconfigure(0, weight=1)
    box.rowconfigure(0, weight=1)
    box.geometry('400x500')
    box.title("LAP_3_GUI")
    style = Style() 
    style.configure('TButton', font = ('calibri', 20, 'bold'), borderwidth = '4') 
    btn1 = Button(box, text="Load File", command=lambda: get_path(False),)
    btn1.grid(column=0, row=0, pady = 10)
    btn3 = Button(box, text="Edit File", command=lambda: edit_file(Load_file_path))
    btn3.grid(column=0, row=2, pady = 10)
	
	
    box.mainloop()
	
if __name__=="__main__":
	make_gui()
	
