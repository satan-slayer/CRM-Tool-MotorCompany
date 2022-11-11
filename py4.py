# Code Available at - https://github.com/TheStallion/Desk-Data-CRM
# Coded By SatanSlayer - Credits: Elshad Karmov, Udemy, Contributors
# Hope It Helps!!
# ----------------------------------------------------------------------------------
# Importing Libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from tkinter.simpledialog import askstring


# Create DataBase
db = sqlite3.connect('stallion.db')
c = db.cursor()
c.execute("""CREATE TABLE if not exists bookings (
	first_name text, 
	last_name text, 
	id integer, 
	model text, 
	varient text, 
	type text, 
	color text,
	address text, 
	total integer)""")
db.commit()

# Create Tkinter
root = Tk()
root.title('Desk-Data-CRM')
root.geometry("1310x500")
root.config(bg='#020010')
# Theme
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background='#020010', foreground='#a5feff', rowhieght=25, fieldbackground="#080040")
style.map("Treeview", bg=[('selected', '#0f29ff')])

# Framing
ftree = Frame(root)
ftree.pack(pady=10)
finput = LabelFrame(root, text='Record', bg='#020010', fg='silver')
finput.pack(fill='both', expand='yes', padx=10)
fbutton = LabelFrame(root, text='Actions', bg='#020010', fg='silver')
fbutton.pack(fill='both', expand='yes', padx=10, pady=10)

# Scrollbar
scroll = Scrollbar(ftree)
scroll.pack(side=RIGHT, fill=Y)

#TreeView
main = ttk.Treeview(ftree, yscrollcommand=scroll.set, selectmode='extended')
main.pack()
scroll.config(command=main.yview)
main.tag_configure('oddrow', background='#33c3cc', foreground='black')
main.tag_configure('evenrow', background='white', foreground='black')


# TreeView - Columns [FN, LN, ID, Model, Varient, Type, Total]
main['columns'] = ("First Name", "Last Name", "ID", "Model", "Varient", "Type", "Color", "Address", "Total")
main.column("#0", width=0, stretch=NO)
main.column("First Name", anchor=CENTER, width=140)
main.column("Last Name", anchor=CENTER, width=140)
main.column("ID", anchor=CENTER, width=90)
main.column("Model", anchor=CENTER, width=140)
main.column("Varient", anchor=CENTER, width=140)
main.column("Type", anchor=CENTER, width=140)
main.column("Color", anchor=CENTER, width=140)
main.column("Address", anchor=CENTER, width=190)
main.column("Total", anchor=CENTER, width=160)

# TreeView - Headings [FN, LN, ID, Model, Varient, Type, Address, Total]
main.heading("#0", text='')
main.heading("First Name", text='First Name')
main.heading("Last Name", text='Last Name')
main.heading("ID", text='UID')
main.heading("Model", text='Model')
main.heading("Varient", text='Varient')
main.heading("Type", text='Type')
main.heading("Color", text='Color')
main.heading("Address", text='Address')
main.heading("Total", text='Total-[USD]')

# Fake Data 
main1={
'Cars':['Luvenis', 'Rugiet', 'Gratia', 'EXLUSIVE-Equus'],
'Varients':['Tour', 'Race', 'Grandeor'], 
'Types':['Core', 'Elite'],
'Price':{
	'Equus':{
			'Tour':{
				 'Core':'105000',
				 'Elite':'130000'},
			'Race':{
				 'Core':'125000',
				 'Elite':'140000'},
			'Grandeor':{
					 'Core':'135000',
					 'Elite':'155000'}},
	'Rugiet':{
			'Tour':{
				 'Core':'100000',
				 'Elite':'125000'},
			'Race':{
				 'Core':'120000',
				 'Elite':'135000'},
			'Grandeor':{
					 'Core':'130000',
					 'Elite':'150000'}},
	'Gratia':{
			'Tour':{
				 'Core':'102000',
				 'Elite':'114000'},
			'Race':{
				 'Core':'116000',
				 'Elite':'120000'},
			'Grandeor':{
					 'Core':'125000',
					 'Elite':'145000'}},
	'Luvenis':{
		  'Tour':{
			   'Core':'179000',
			   'Elite':'182000'},
		  'Race':{
			   'Core':'190000',
			   'Elite':'200000'},
		  'Grandeor':{
		  		   'Core':'205000',
		  		   'Elite':'210000'},},
		},
'Colors':{
	   'Luvenis':['Pacific Blue', 'Volcanic Red', 'Dusked Yellow', 'Savanqa Green', 'DarkNight Black'],
	   'Rugiet':['Savanqa Green', 'Volcanic Red', 'DarkNight Black'],
	   'Gratia':['Savanqa Green', 'Dusked Yellow', 'DarkNight Black'],
	   'Equus':['Dusked Yellow', 'Volcanic Red', 'DarkNight Black'],
		 },
}

# Functions
def add_data():
	global count
	data_list=[["Robert", "Clive", "1", "Rugiet", "Race", "Elite", "Volcanic Red", "h4-101 st. LA -32001", "135000"],
	  ["William", "Cornwails", "2", "Gratia", "Tour", "Elite", "Savanqa Green", "A13-Regy st. NY -54599", "114000"],
	  ["Lucy", "Lester", "3", "Equus", "Grandoer", "Elite", "Dusked Yellow", "23 WillTowr NV -13256", "155000"],
	  ["Adam", "Groy", "4", "Gratia", "Grandoer", "Core", "Dusked Yellow", "g13-trin st. DC -10087", "125000"],
	  ["Ali", "Rizan", "5", "Luvenis", "Grandoer", "Elite", "DarkNight Black", "Range Halls, RC st. NY -12980", "210000"],
	  ["Gordon", "Ramsey", "6", "Gratia", "Race", "Core", "Savanqa Green", "x3-Lonson st. TN -47283", "110000"],
	  ["Sharuk", "Khan", "7", "Equus", "Grandoer", "Elite", "Dusked Yellow", "Range Halls, RC st. IL -98072", "155000"],
	  ["Hurucio", "Pagani", "8", "Rugiet", "Grandoer", "Elite", "Volcanic Red", "y8-Lebro st. HV -67856", "150000"],
	  ["Letro", "Heneno", "9", "Equus", "Race", "Core", "Dusked Yellow", "y19-st. DC -21313", "105000"],
	  ["Dwayne", "Johnson", "10", "Rugiet", "Grandoer", "Elite", "Volcanic Red", "y6-Rebo st. NY -13123", "150000"],
	  ["Praveen", "Varma", "11", "Gratia", "Tour", "Core", "Savanqa Green", "a6-Trinity st. MO-53901", "102000"],
		]
	count = 0
	for rec in data_list:
		c.execute("INSERT INTO bookings VALUES (:first_name, :last_name, :id, :model, :varient, :type, :color, :address, :total)",
					{
					'first_name':rec[0],
					'last_name':rec[1],
					'id':rec[2],
					'model':rec[3],
					'varient':rec[4],
					'type':rec[5],
					'color':rec[6],
					'address':rec[7],
					'total':rec[8],
					},
					
					)
		db.commit()

def calculate_total():
	global total
	m = model_chosen.get()
	v = varient_chosen.get()
	t = type_chosen.get()
	if m == 'Equus':
		if v == 'Tour':
			if t == 'Core':
				total = 105000
			elif t == 'Elite':
				total = 130000
		elif v == 'Race':
			if t == 'Core':
				total = 125000
			elif t == 'Elite':
				total = 140000
		elif v == 'Grandoer':
			if t == 'Core':
				total = 135000
			elif t == 'Elite':
				total = 155000

	elif m == 'Rugiet':
		if v == 'Tour':
			if t == 'Core':
				total = 100000
			elif t == 'Elite':
				total = 125000
		elif v == 'Race':
			if t == 'Core':
				total = 120000
			elif t == 'Elite':
				total = 135000
		elif v == 'Grandoer':
			if t == 'Core':
				total = 130000
			elif t == 'Elite':
				total = 150000
	elif m == 'Gratia':
		if v == 'Tour':
			if t == 'Core':
				total = 102000
			elif t == 'Elite':
				total = 114000
		elif v == 'Race':
			if t == 'Core':
				total = 116000
			elif t == 'Elite':
				total = 120000
		elif v == 'Grandoer':
			if t == 'Core':
				total = 125000
			elif t == 'Elite':
				total = 145000
	elif m == 'Luvenis':
		if v == 'Tour':
			if t == 'Core':
				total = 179000
			elif t == 'Elite':
				total = 182000
		elif v == 'Race':
			if t == 'Core':
				total = 190000
			elif t == 'Elite':
				total = 200000
		elif v == 'Grandoer':
			if t == 'Core':
				total = 205000
			elif t == 'Elite':
				total = 210000
	else:
		total = 0

	return total

def query():
	global records, count
	c.execute("SELECT rowid, * FROM bookings")
	records = c.fetchall()
	count = 0
	for item in main.get_children():
		main.delete(item)

	for rec in records:
		if count % 2 == 0:
			main.insert(parent='', index='end', iid=count, text='', values=(rec[1], rec[2], rec[0], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9]), tags=('evenrow',))
		else:
			main.insert(parent='', index='end', iid=count, text='', values=(rec[1], rec[2], rec[0], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9]), tags=('oddrow',))
		count+=1

def add_button(e):
	global i0, i1, i2, color_chosen, i7, i8, model_chosen, varient_chosen, type_chosen
	global data_list, count
	total = calculate_total()
	inputs = [i0, i1, i2, i7]
	x = [i0.get(), i1.get(), i2.get(), model_chosen.get(), varient_chosen.get(), type_chosen.get(), color_chosen.get(), i7.get()]
	c.execute("INSERT INTO bookings VALUES (:first_name, :last_name, :id, :model, :varient, :type, :color, :address, :total)",
					{
					'first_name':x[0],
					'last_name':x[1],
					'id':x[2],
					'model':x[3],
					'varient':x[4],
					'type':x[5],
					'color':x[6],
					'address':x[7],
					'total':total,
					}
					)
	db.commit()
	query()

def search_records(id_to_search):
	global s
	for item in main.get_children():
		main.delete(item)
	c.execute('SELECT rowid, * FROM bookings WHERE oid like ' + id_to_search)
	rec = c.fetchall()
	try:
		x = rec[0]
		count2 = 0
		if count2 % 2 == 0:
			main.insert(parent='', index='end', iid=count, text='', values=(x[1], x[2], x[0], x[4], x[5], x[6], x[7], x[8], x[9]), tags=('evenrow',))
		else:
			main.insert(parent='', index='end', iid=count, text='', values=(x[1], x[2], x[0], x[4], x[5], x[6], x[7], x[8], x[9]), tags=('oddrow',))
		count2+=1
		s.destroy()
	except:
		s.destroy()
		query()
		messagebox.showinfo('Lookup NA', 'The ID you searched for Does not exist...')

def lookup_records():
	global s
	s = Toplevel(root)
	s.title('Search')
	s.geometry('540x130')
	s.config(bg='#020010')

	fsearch = LabelFrame(s, text='ID', bg='#020010', fg='silver', padx=20, pady=10)
	fsearch.pack(fill='both', padx=20, pady=10)

	sentry= Entry(fsearch, font=('Helvetica', 20))
	sentry.grid(row=0, column=0, padx=20, pady=10)


	sbutton = Button(fsearch, text='Search', bg='#020010', fg='silver', relief='groove', command=lambda: search_records(sentry.get()))
	sbutton.grid(row=0, column=1, padx=20, pady=10)

def remove():
	response = messagebox.askyesno('DELETE BOOKINGS', 'You are about to delete bookings, \nthis proccess is non-reversable. \n Do you wish to proceed??')
	if response == 1:
		selected = main.selection()
		ids = []
		for record in selected:
			id_item = main.item(record, 'values')[2]
			ids.append(id_item)
			c.execute("DELETE FROM bookings WHERE oid=" + id_item)
			db.commit()
			main.delete(record)
		clear()
		query()

def clear():
	i1.delete(0, END)
	i0.delete(0, END)
	i2.delete(0, END)
	model_chosen.set('')
	varient_chosen.set('')
	type_chosen.set('')
	color_chosen.set('')
	i7.delete(0, END)

def select(e):
	selected = main.focus()
	values = main.item(selected, 'values')
	i0.delete(0, END)
	i0.insert(0, values[0])
	i1.delete(0, END)
	i1.insert(0, values[1])
	i2.delete(0, END)
	i2.insert(0, values[2])
	model_chosen.set(values[3])
	varient_chosen.set(values[4])
	type_chosen.set(values[5])
	color_chosen.set(values[6])
	i7.delete(0, END)
	i7.insert(0, values[7])
	print(values[5])

def edit():
	selected = main.selection()[0]
	total = calculate_total()
	y = [i0.get(), i1.get(), i2.get(), model_chosen.get(), varient_chosen.get(), type_chosen.get(), color_chosen.get(), i7.get(),]
	main.item(selected, values=(y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], total))
	c.execute("""UPDATE bookings SET
			first_name = :first,
			last_name = :last,
			model = :model,
			varient = :varient,
			type = :type,
			color = :color,
			address = :address,
			total = :total

			WHERE oid = :oid""",
			{
			'first':y[0],
			'last':y[1],
			'model':y[3],
			'varient':y[4],
			'type':y[5],
			'color':y[6],
			'address':y[7],
			'total':total,
			'oid':y[2]
			}
			)
	db.commit()
	i1.delete(0, END)
	i0.delete(0, END)
	i2.delete(0, END)
	model_chosen.set('')
	varient_chosen.set('')
	type_chosen.set('')
	color_chosen.set('')
	i7.delete(0, END)
	query()

def remove_all():
	response = messagebox.askyesno('DELETE BOOKINGS', 'You are about to delete ALL bookings, \nthis proccess is non-reversable and can be regretted. \n Do you wish to proceed??')
	if response == 1:
		password = askstring('PassCode', 'Enter password:', show='*')
		x = messagebox.showinfo('Enter PassCode', 'PassCode input: {}'.format(password))
		if password == 'TheStallion@1234.ForeverMotors':
			messagebox.showinfo('PassCode Correct', 'PassCode Verified, Deleting all Bookings')
			for item in main.get_children():
				main.delete(item)
			c.execute("DROP TABLE bookings")
		else:

			messagebox.showinfo('PassCode Incorrect', 'PassCode Incorrect, Failed Deleting all Bookings')

def move(direction):
	if direction == 'up':
		selected = main.selection()
		for i in selected:
			main.move(i, main.parent(i), main.index(i)-1)
	else:
		selected = main.selection()
		for i in reversed(selected):
			main.move(i, main.parent(i), main.index(i)+1)

# Input
# Input - Labels
l0 = Label(finput, text='First-Name', bg='#020010', fg='silver')
l1 = Label(finput, text='Last-Name', bg='#020010', fg='silver')
l2 = Label(finput, text='ID', bg='#020010', fg='silver')
l3 = Label(finput, text='Model', bg='#020010', fg='silver')
l4 = Label(finput, text='Varient', bg='#020010', fg='silver')
l5 = Label(finput, text='Type', bg='#020010', fg='silver')
l6 = Label(finput, text='Color', bg='#020010', fg='silver')
l7 = Label(finput, text='Address', bg='#020010', fg='silver')
# Input - Entry
varient_chosen = StringVar()
model_chosen = StringVar()
type_chosen = StringVar()
color_chosen = StringVar()
models = ["Equus", "Rugiet", "Gratia", "Luvenis"]
varients = ["Tour", "Race", "Grandoer"]
types = ["Core", "Elite"]
color = ['Pacific Blue', 'Volcanic Red', 'Dusked Yellow', 'Savanqa Green', 'DarkNight Black', 'CUSTOM']
i0 = Entry(finput)
i1 = Entry(finput)
i2 = Entry(finput)
i3 = OptionMenu(finput, model_chosen, *models)
i3.config(bg='#020010', fg='silver', relief='groove', width=15)
i3["menu"].config(bg='#020010', fg='silver', relief='groove')
i4 = OptionMenu(finput, varient_chosen, *varients)
i4.config(bg='#020010', fg='silver', relief='groove', width=15)
i4["menu"].config(bg='#020010', fg='silver', relief='groove')
i5 = OptionMenu(finput, type_chosen, *types)
i5.config(bg='#020010', fg='silver', relief='groove', width=15)
i5["menu"].config(bg='#020010', fg='silver', relief='groove')
i6 = OptionMenu(finput, color_chosen, *color)
i6.config(bg='#020010', fg='silver', relief='groove', width=15)
i6["menu"].config(bg='#020010', fg='silver', relief='groove')
i7 = Entry(finput)
# Input - Griding
l0.grid(row=0, column=0, padx=5)
i0.grid(row=0, column=1, padx=5)
l1.grid(row=0, column=2, padx=5)
i1.grid(row=0, column=3, padx=5)
l2.grid(row=0, column=4, padx=5)
i2.grid(row=0, column=5, padx=5)
l3.grid(row=0, column=6, padx=5)
i3.grid(row=0, column=7, padx=5)
l4.grid(row=0, column=8, padx=5)
i4.grid(row=0, column=9, padx=5)

l5.grid(row=1, column=0, padx=10, pady=10)
i5.grid(row=1, column=1, padx=10, pady=10)
l6.grid(row=1, column=2, padx=10, pady=10)
i6.grid(row=1, column=3, padx=10, pady=10)
l7.grid(row=1, column=4, padx=10, pady=10)
i7.grid(row=1, column=5, padx=10, pady=10)

# Buttons
b0 = Button(fbutton, text='Add Record', bg='#020010', fg='silver', relief='groove', command=lambda: add_button('Event_Fake_Input'))
b2 = Button(fbutton, text='Remove Record', bg='#020010', fg='silver', relief='groove', command=remove)
b1 = Button(fbutton, text='Update Record', bg='#020010', fg='silver', relief='groove', command=edit)
b3 = Button(fbutton, text='Move Up', bg='#020010', fg='silver', relief='groove', command=lambda: move('up'))
b4 = Button(fbutton, text='Move Down', bg='#020010', fg='silver', relief='groove', command=lambda: move('down'))
b5 = Button(fbutton, text='Remove All', bg='#020010', fg='silver', relief='groove', command=remove_all)
b6 = Button(fbutton, text='Clear Entry', bg='#020010', fg='silver', relief='groove', command=clear)

b0.grid(row=0, column=0, padx=20,pady=10)
b1.grid(row=0, column=1, padx=20,pady=10)
b2.grid(row=0, column=2, padx=20,pady=10)
b5.grid(row=0, column=3, padx=20,pady=10)
b6.grid(row=0, column=4, padx=20,pady=10)
b3.grid(row=0, column=5, padx=20,pady=10)
b4.grid(row=0, column=6, padx=20,pady=10)

main.bind('<ButtonRelease-1>', select)


query()

# Menu
menu = Menu(root, bg='#020010', fg='silver')
root.config(menu=menu)
options = Menu(menu, tearoff=0, bg='#020010', fg='silver')
menu.add_cascade(label='Options', menu=options)
options.add_command(label='Exit', command=root.destroy)
search = Menu(menu, tearoff=0, bg='#020010', fg='silver')
menu.add_cascade(label='Search', menu=search)
search.add_command(label='Search', command=lookup_records)
search.add_separator()
search.add_command(label='Clear', command=query)

root.mainloop()

db.close()