from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
# from tkcalendar import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import csv
import os
from random import randint as _id
from datetime import date as day
#from mydatabase import *
from icon import*


#relif = flat, groove, raised, ridge, solid, or sunken
#Button(room,text="Submit",width=0,command=lambda:print('hello')).grid()
#Label(room,text="").grid(columnspan= 1 ,padx=20,pady=20)



# ____________WINDOW_____________
room =Tk()
#room.wm_focusmodel(ACTIVE)
room.title("Admin Window")
room.iconbitmap("Icon.ico")
room.geometry('800x420')
#room.attributes("-alpha",0.5)
#room.maxsize(width=1000,height=440)
#room.minsize(width=700, height=400)
room.resizable(0,0)
#room.configure(background="black")
#____TITLE____
fr_title = LabelFrame(room,border=0)
Label(fr_title,text="Welcome   to   Icecreem   Parlor",
	bg='black',
	fg="orange",pady=10,
	font=("Reckoner",24)
	).pack(fill=X)
##fr2.grid(column=0,row=0,sticky=N,columnspan=2) #NOW pack rocks
fr_title.pack(fill=X,side=TOP)
#____________WINDOW END___________

# __FIELDS__
fields = {
	1:["S.No.","Name","Item","Price","Date of purchase"],
	2:["E_ID","Name","Salary","Date of Joining"],
	3:["P_ID","Item_Name","Quantity","Price","Batch No."],
	4:["No.","Item_Name","Price","Quantity"]
}

#_____________"MODULE" buttons__________
fr_right = LabelFrame(room,relief="solid")
fr_right.pack(side=LEFT,fill=BOTH)

im = Button(fr_right,text="Import Data",width=20,border=3)
im.grid(column=0 ,row=1,sticky=W)

cu = Button(fr_right,text="Customer Management",width=20,border=3)
cu.grid(column=0 ,row=2,sticky=W)

em = Button(fr_right,text="Employee Management",width=20,border=3)
em.grid(column=0 ,row=3,sticky=W)

pr = Button(fr_right,text="Product Management",width=20,border=3)
pr.grid(column=0 ,row=4,sticky=W)

bi = Button(fr_right,text="Bill Management",width=20,border=3)
bi.grid(column=0,row=5,sticky=W)

ex = Button(fr_right,text="EXIT",width=0,border=3,command=room.destroy)
ex.grid(column=0,sticky=S)

##fr1.grid(column=0 ,row=1,sticky=W,ipady=100)
#_____________"MODULE"(Buttons)END__________



class wind:
	fr_mod = LabelFrame(room,border=4)	# fr_mod ----> frame on RIGHT the entire thing!! ALL PLAY IS HERE!!
	fr_mod.pack(side= RIGHT, expand = True, fill  =BOTH)

	fr_options = LabelFrame(fr_mod,border=0)
	fr_options.pack(side= TOP , fill=X)	# fr_options ----> keeps   "Listbox"  ___DATA  Changing___ functions

	fr_box = LabelFrame(fr_mod , border=0)		# keeps LISTBOX with Scrollbar...
	fr_box.pack(side=TOP , expand = True, fill = BOTH)
	
	fr1 = LabelFrame(fr_mod,border=2,pady= 15,padx=20)
	fr1.pack(side=BOTTOM,expand=True, fill = X )		# 	TO grid ENTRY	Widgets	(basically one which is destroyed )
	reaper = list()					#####    LIST of instanses
	sow = list()

	def __init__(self , fields = ["S.No.","Name","Field1","Field2"] , name = None , date_field = None, item_field = None):
		self.name = name
		self.fields = fields
		self.date_field = date_field
		self.item_field = item_field
		self.generator = []			# keeps entry widgets
		wind.reaper += [self]		# _________ keeping track of objects that use this class (I know there is a function for this but I don't remember)
		wind.sow += [name]

	def dest(self):
		self.generator = []			# __________ I destroy everything on clicking one of those customer,bill ,etc button____ (labels are recreated wasting memory)
		for i in wind.fr1.winfo_children(): i.destroy()					###   winfo_children() >>> gives all things in the frame

	@staticmethod
	def destall():
		for done in wind.reaper:			# _________ MAJOR flaw ____ function is good but its reason... dest() above shall tell
			done.dest()
	
	def calendar(self,event):		# ___________ Open a calendar_____
		window = Toplevel()
		window.wm_attributes("-toolwindow",True)
		#window.overrideredirect(True)
		#window.wm_transient()
		cal = Calendar(window,cursor = "hand2", selectmode="day",
			year=day.today().year, month=day.today().month , day= day.today().day )
		cal.pack()
		def done():	# __ destroy window after selection, so didn't use lambda'
			self.generator[ self.date_field - 1 ].delete(0, END)
			dat = cal.get_date().split("/")
			dat[0],dat[1],dat[2] = "20"+dat[2], dat[0], dat[1]
			dat = "-".join(dat)
			self.generator[ self.date_field - 1 ].insert( 0,  dat)
			window.destroy()
		Button(window,text="Done!", command = done).pack()
	def draw_func(self):
		wind.fr1.config(text= self.name)
		#Label(wind.fr1,text='ENTER  DATA').grid(sticky=N,pady=2,row=0,column=0,columnspan=4)
		Label(wind.fr1,text="  DATA   MANAGEMENT",fg="white",
		font=("Reckoner",18),bg="black"
		).grid(sticky=N,pady=2,row=0,column=0,columnspan=8,ipadx= 20)

		div = int(len(self.fields)/2)
		for i,val in enumerate(self.fields):			# _____________ <<---- here dividing fields entry widget (creating 4 columns(label,entry  label,entry))
			if i < div:
				a = Label(wind.fr1,text=val)
				a.grid(row=1+i ,column=0 ,pady=3,padx=20)
				b = Entry(wind.fr1,width=12)
				b.grid(row=1+i ,column=1 ,pady=3,padx=20)
				self.generator.append(b)
			else:
				a = Label(wind.fr1,text=val)
				a.grid(row=1+ i - div ,column=2 ,pady=3,padx=20)
				b = Entry(wind.fr1,width=12)
				b.grid(row=1+i - div ,column=3 ,pady=3,padx=20)
				self.generator.append(b)
		if self.date_field != None: self.date_get()
		if self.item_field != None: self.item_get()
		self.generator[0].insert(0, _id(1000,9999))

		submit_button = Button(wind.fr1,text= "Submit", width = 0, command = self.data_reape)
		submit_button.grid(sticky=S,columnspan=4,pady =20)

	def date_get(self):# ______________ <<----- here for auto-date entery
		if self.date_field <= len(self.fields):
			roco = (self.generator[ self.date_field - 1 ].grid_info()["row"] , self.generator[ self.date_field - 1 ].grid_info()["column"])
			self.generator[self.date_field-1].destroy()
			del self.generator[self.date_field-1]
			global img
			img = Combobox(wind.fr1,width=10,height=5,value="")
			img.grid(row=roco[0],column=roco[1])
#print(img.winfo_pathname(img))
			self.generator.insert(int(self.date_field-1), img)
			self.generator[self.date_field-1].set(day.today())
			self.generator[self.date_field-1].bind("<Button-1>",self.calendar)
		else:return
	def item_get(self):
		b = "source/item.txt"
		try:	
			with open(b) as f:
				item_list = f.readlines()
		except FileNotFoundError:
			open(b,"w+")
			item_list = ["No Item"]
		roco = (self.generator[self.item_field-1].grid_info()["row"],self.generator[self.item_field-1].grid_info()["column"])
		self.generator[self.item_field-1].destroy()
		del self.generator[self.item_field-1]
		item_box = Combobox(wind.fr1,width=9,height=5,value=item_list)#,command= self.item_given)
		item_box.grid(row=roco[0],column=roco[1])
		self.generator.insert(int(self.item_field-1), item_box)
	# def item_given(self,event):
	# 	item_var.set("")
	# 	if event == "":
	# 		self.generator[self.item_field-1].delete(0,END)
	# 	else:
	# 		self.generator[self.item_field-1].delete(0,END)
	# 		self.generator[self.item_field-1].insert(0,event)

	def data_reape(self):
		xyz = list()
		for data in self.generator:		#  ________________________ self.generator has entry fields_____ .get() to extract is here!!_____
			xyz += [str(data.get())]
		if "" in xyz:
			mb.showerror('Field missing',"Fill all fields!!")
		else:
			try:
				sql_saver(self.name, self.fields , xyz)	# _________ SAVE DATA ____ (Name of Table , Fields in table , xyz = Values of fields)
				for i in self.generator: i.delete(0, END)
				self.generator[0].insert(0, _id(1000,9999))
				if self.date_field != None:
					self.generator[ self.date_field - 1 ].insert( 0,  day.today())
			except mysql.connector.errors.IntegrityError:
				mb.showerror("Primary Key reapeted","S.No./ID already Exists")

	@staticmethod
	def list_box_draw():
		for i in wind.fr_box.winfo_children(): i.destroy()
		
		# ____________ Scrollbar _____________
		x = Scrollbar(wind.fr_box, orient= HORIZONTAL)
		y = Scrollbar(wind.fr_box, orient= VERTICAL)
		y.pack(side=RIGHT, fill= Y)
		x.pack(side = BOTTOM, fill= X)
		#		__________________________  LISTBOX as     (data_box)________________________________
		data_box = Listbox(wind.fr_box, height = 5,width = 20, selectmode = EXTENDED, 
		yscrollcommand = y.set , xscrollcommand = x.set)
		data_box.pack(side= LEFT, expand = True, fill= BOTH)
		
		x.config(command = data_box.xview)
		y.config(command = data_box.yview)
		
		# __________________ DATA FILLER/ DATA FETCHER (fill data in listbox)________________
		def fill(event):
			global ch
			ch = display.get()
			if ch == "Display":
				search_name.config(value=[""])
				search_name.current(0)
				data_box.delete(0, END)
				return
			else:
				search_name.config(value=field_find())
				search_name.current(0)
				data_box.delete(0, END)
				data = sql_limited( ch, 5 )
				for da in data:
					data_box.insert(END , str(da))
				#idea---> ch is also name of database, 5 is number of records that will be returned to data
				#Data Fetching function to return data!!
		def fillall():
			conf = mb.askquestion("WARNING!","Show all? For a big table this could crash the Application.")
			print(conf)
			if conf == "no":return
			try:
				if ch == "Display":
					data_box.delete(0, END)
					return
				else:
					data_box.delete(0, END)
					data = sql_showall( ch )		#   ______   showall(name) should return all records of {name} table
					for da in data:
						data_box.insert(END , str(da))
			except:
				mb.showerror("An Error Occured","Make sure a field has been selected")

		# ______________ Drop Down Box_________
		display = StringVar()
		display.set("Display")
		
		option = OptionMenu(wind.fr_options, display , "Display",*wind.sow, command=fill)
		option.pack(side=LEFT)
		Button(wind.fr_options,text="Show All", width=0,command= fillall).pack(side=LEFT)

		def field_find():
			for inst in wind.reaper:
				if inst.name == ch:return inst.fields
		
		# _______________ SEARCH BAR... ____________________
		def search_given():
			col = search_name.get()
			name = display.get()
			num = search_entry.get()
			if name == "Display":return
			try:
				data = sql_search(name, col, num)
				data_box.delete(0, END)
				if data == None or data == []:mb.showinfo("Not Found!!",f"{col} '{num}' not found in {name}")
				for da in data:
					data_box.insert(END , str(da))
			except mysql.connector.errors.ProgrammingError:
				mb.showerror("Not Supported! Module Error",
					"Sorry but Database connecting module can't process this!")
			except ValueError:
				mb.showerror("Search Error",
					"Provide a Positive Integer!")

		def delete_se():
			name = display.get()
			rec = list()
			for da in reversed(data_box.curselection()):
				id_cr = data_box.get(da).split(",")
				id_cr = id_cr[0].split("(")
				rec += [int(id_cr[1])]
			if rec == []:return
			conf = mb.askokcancel("WARNING!",f"This will Delete: {rec}")
			if conf == 1 :
				sql_delete(name, rec)
				mb.showinfo("Success!",f"Deleted: {rec}")
				fill("e")

		search_name = Combobox(wind.fr_options,width=10, value=[""])
		search_name.pack(side=RIGHT)

		search_entry = Entry(wind.fr_options,width=20)
		search_entry.pack(side=RIGHT)

		#search_entry.bind("<Key>", search_given)
		Button(wind.fr_options, width=0,text="Search",command= search_given).pack(side=RIGHT,padx=20)

		# _______________ DELETE BUTTON ______________
		delete_button = Button(wind.fr_options, text="Delete selected",width=0,command=delete_se)
		delete_button.pack(side=LEFT)


cus = wind(fields[1],"Customer", 5,3)
emp = wind(fields[2],"Employee" , 4)
pro = wind(fields[3],"Product",item_field=2)
bil = wind(fields[4],"Bill",item_field=2)

wind.list_box_draw()
cus.draw_func()
#________________FUNCTIONS_____________
def import_func():
	ch = mb.askokcancel("Confirm","All fields in csv should be in same order.")
	if ch == True:
		b = filedialog.askopenfilename(initialdir="", title="Select Database",filetypes=(("CSV type","*.csv"),("All types","*.*")))
		if b != tuple():
			#im = Button(fr_right,text="Import Data",width=20,border=3,relief="groove",state= "disabled").grid(column=0 ,row=1,sticky=W)
			name = b.split("/")
			local = { i.lower() + ".csv" for i in wind.sow}
			if name[-1].lower() in local:
				name = name[-1].split(".")
				try:
					with open(b,"r") as f:
						csv_r = csv.reader(f)
						val = [i for i in csv_r]
						sql_importer(name[0], val[0] , val[1:])
					mb.showinfo("Done!","Data imported successfully!!")
				except:
					mb.showwarning("WARNING!", "An error occured. Data import unsuccessful!")
			else:
				mb.showinfo("Check File Name", f"Make sure name is of format {local}")
		else:return

def cus_func():
	cus.destall()
	cus.draw_func()
#	print(cus.generator)
#	print('\n\n')
def emp_func():
	cus.destall()
	emp.draw_func()
#	print('_______EMP______\n',emp.generator,'\n_________END________\n\n')
def pro_func():
	pro.destall()
	pro.draw_func()
def bil_func():
	bil.destall()
	bil.draw_func()

def csv_save(obj):
	da = sql_showall( obj.name)
	with open(f"{obj.name}"+".csv","w+") as f:
		csv_w = csv.writer(f,delimiter=",")
		csv_w.writerow(obj.fields)
		for i in da:
			csv_w.writerow(i)
def open_file():
	old = os.getcwd()
	os.chdir("source")
	os.startfile("item.txt")
	os.chdir(old)

# _______________FUNC END______________

# ______________MENU___________
men = Menu(room)
room.config(menu=men)


filemenu = Menu(men, tearoff=0)

open_menu = Menu(filemenu,tearoff=0)
open_menu.add_command(label="Items file",command=open_file)
filemenu.add_cascade(label="Open",menu=open_menu)


save_menu = Menu(filemenu,tearoff=0)
save_option = Menu(save_menu,tearoff=0)

save_option.add_command(label=wind.reaper[0].name, command=lambda: csv_save(wind.reaper[0]))
save_option.add_command(label=wind.reaper[1].name, command=lambda: csv_save(wind.reaper[1]))
save_option.add_command(label=wind.reaper[2].name, command=lambda: csv_save(wind.reaper[2]))
save_option.add_command(label=wind.reaper[3].name, command=lambda: csv_save(wind.reaper[3]))

save_menu.add_cascade(label="CSV file",menu=save_option)
filemenu.add_cascade(label="Save as...",menu=save_menu)


filemenu.add_separator()
filemenu.add_command(label="Exit",command=room.destroy)
men.add_cascade(label="File",menu=filemenu)

# edit_menu = Menu(men,tearoff=0)
men.add_command(label="Help",command=lambda:os.startfile("Help.txt"))
# men.add_cascade(label="Edit",menu=edit_menu)

# _____________ MENU END___________________


im.config(command=import_func)
cu.config(command=cus_func)
em.config(command=emp_func)
pr.config(command=pro_func)
bi.config(command=bil_func)

room.mainloop()
