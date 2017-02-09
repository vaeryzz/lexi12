import Tkinter as tk
import os

'''
Organize code
increase font size
add option to edit entry
display part of speech & examples


'''

class Lexicon:
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.filename = "lexi12.txt"
		self.name = []
		self.meaning = {}
		
		self.buffer5 = tk.Frame(self.parent, height=2, bg="black")
		self.buffer5.pack(fill=tk.X)
		
		self.main_frame = tk.Frame(parent)
		self.main_frame.pack(expand=1, fill=tk.BOTH)
		
		self.buffer6 = tk.Frame(self.parent, height=2, bg="black")
		self.buffer6.pack(fill=tk.X)
		
		self.buffer = tk.Frame(self.main_frame, width=2, bg="black")
		self.buffer.pack(side=tk.LEFT, fill=tk.Y)
		
		self.mf_listbox = tk.Frame(self.main_frame, bg="black", width=50, highlightbackground="black", highlightthickness=2)
		self.mf_listbox.pack(side=tk.LEFT, expand=0, fill=tk.Y)
		
		#self.mf_listbox.focus_set()
		#self.buffer1 = tk.Frame(self.main_frame, width=1, bg="black")
		#self.buffer1.pack(side=tk.LEFT, fill=tk.Y)
		
		self.mf_display = tk.Frame(self.main_frame, height=100, width=175, bg="black", highlightbackground="black", highlightthickness=5)
		self.mf_display.pack(expand=1, side=tk.LEFT, fill=tk.BOTH)
		
		#self.buffer2 = tk.Frame(self.main_frame, width=1, bg="black")
		#self.buffer2.pack(side=tk.LEFT, fill=tk.Y)
		
		self.word_name = tk.Label(self.mf_display, text="Word", bg="black", fg="white", font="Tahoma 24", anchor=tk.W, padx=5)
		self.word_name.pack(fill=tk.X)
		
		self.display = tk.Label(self.mf_display, text="Meaning", padx=10, pady=20, anchor=tk.NW, justify=tk.LEFT, wraplength=250, font="Tahoma 14")
		self.display.pack(expand=1, fill=tk.BOTH)
		
		self.searchbar = tk.Frame(self.mf_listbox, bg="black", height=25)
		self.searchbar.pack(expand=0, side=tk.TOP, fill=tk.X)
		self.searchbar.propagate(0)

		self.search_entry = tk.Entry(self.searchbar, width=15, font="Tahoma 10")
		#self.parent.bind("<Shift_L>", self.entry_focus)
		self.parent.bind("<BackSpace>", self.entry_focus)
		self.search_entry.pack(expand=0, side=tk.LEFT, fill=tk.BOTH)
		
		self.search_button = tk.Button(self.searchbar, text=">", command=lambda:self.search(), font="Tahoma 10", relief=tk.FLAT, width=3, bg="black", fg="white")
		self.parent.bind("<Return>", self.search)
		self.search_button.pack(expand=0, side=tk.RIGHT, fill=tk.X)
		
		self.listbox = tk.Listbox(self.mf_listbox, activestyle="none", selectbackground="black", selectforeground="white", font="Tahoma 12", width=15)
		
		#for items in range(100):
		#for i in range(len(self.name)):
		#	self.listbox.insert(tk.END,self.name[i])
		#	print names
		
		self.listbox.bind("<<ListboxSelect>>", self.curselet)
		self.listbox.pack(expand=1, fill=tk.Y)
		
		#self.listbox.focus_set()
		self.entry_focus()
		
		self.load_words()
		
		self.parent.bind("<Control-s>", self.quit)
		
	
	def quit(self, *args):
		self.parent.quit()
	
	def entry_focus(self, *args):
		self.search_entry.focus_set()
	
	def search(self, *args):
		try:
			word = self.search_entry.get()
		except:
			word = ""
		if word != "":
			self.listbox.delete(0,tk.END)
			count=0
			for names in self.name:
				if names.startswith(word):
					self.listbox.insert(tk.END, names)
					count+=1
			if count==0:
				self.word_name.config(text=word)
				self.display.config(text="word not found")
			else:
				self.listbox.select_set(0)
				self.curselet()
				self.listbox.focus_set()
		else:
			self.listbox.delete(0,tk.END)
			for names in self.name:
				self.listbox.insert(tk.END, names)
			self.listbox.select_set(0)
			self.curselet()	
			self.listbox.focus_set()
				
	def curselet(self, *args):
		#print self.listbox.curselection()
		value = self.listbox.get(self.listbox.curselection())
		self.word_name.config(text=value)
		self.display.config(text=self.meaning[value])
		

	
	def load_words(self):
		with open(self.filename, "r") as txtr:
			#file_txt = txtr.read()
			#for line in file_txt:
			for line in txtr:
				if line != "":
					ab = line.split("##")
					self.name.append(ab[0])
					self.meaning[ab[0]]=ab[1]
					#print ab
					#print self.name
					#print self.meaning[ab[0]]
			self.name.sort()
			for i in range(len(self.name)):
				self.listbox.insert(tk.END, self.name[i])
		self.listbox.select_set(0)
		self.curselet()
		self.search()
		'''
		try:	
			with open(self.filename, "r") as txtr:
				#file_txt = txtr.read()
				#for line in file_txt:
				for line in txtr:
					print line
					name1, meaning1 = line.strip("##\n")
					self.name.append(name1)
					self.meaning[name1]=meaning1
					print name1
					print meaning1
		except:
			f1 = open(self.filename, "w")
			f1.close()
		'''

	
def center(win):
	win.update_idletasks()
	width = win.winfo_width()
	height = win.winfo_height()
	x = (win.winfo_screenwidth() // 2) - (width // 2)
	y = (win.winfo_screenheight() // 2) - (height // 2)
	win.geometry('{}x{}+{}+{}'.format(width, height, x+450, y+170))
	
if __name__ == "__main__":
	root = tk.Tk()
	root.title("lexi12")
	root.geometry("425x300")
	root.wm_attributes("-topmost", True)
	center(root)
	app = Lexicon(root)
	root.mainloop()


