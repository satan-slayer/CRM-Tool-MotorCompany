# Code Available at - https://github.com/TheStallion/Desk-Data-CRM
# Coded By SatanSlayer - Credits: Elshad Karmov, Udemy, Contributors
# Hope It Helps!!
# ----------------------------------------------------------------------------------
# Importing Libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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
main.heading("ID", text='ID')
main.heading("Model", text='Model')
main.heading("Varient", text='Varient')
main.heading("Type", text='Type')
main.heading("Color", text='Color')
main.heading("Address", text='Address')
main.heading("Total", text='Total')

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
				 'Core':'110000',
				 'Elite':'120000'},
			'Grandeor':{
					 'Core':'125000',
					 'Elite':'145000'}},
	'Luvenis':{
		  'Grandeor':{
		  		   'Elite':'210000'}},
		},
'Colors':{
	   'Luvenis':['Pacific Blue', 'Volcanic Red', 'Dusked Yellow', 'Savanqa Green', 'DarkNight Black'],
	   'Rugiet':['Savanqa Green', 'Volcanic Red', 'DarkNight Black'],
	   'Gratia':['Savanqa Green', 'Dusked Yellow', 'DarkNight Black'],
	   'Equus':['Dusked Yellow', 'Volcanic Red', 'DarkNight Black'],
		 },
}

# Functions
def add_data(data:list):
	global count
	count = 0
	for rec in data:
		if count % 2 == 0:
			main.insert(parent='', index='end', iid=count, text='', values=(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8]), tags=('evenrow',))
		else:
			main.insert(parent='', index='end', iid=count, text='', values=(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8]), tags=('oddrow',))
		count+=1

def add_button():
	global i0, i1, i2, i3, i4, i5, i6, i7, i8
	global data_list, count
	y = [i0, i1, i2, i3, i4, i5, i6, i7, i8]
	x = [i0.get(), i1.get(), i2.get(), i3.get(), i4.get(), i5.get(), i6.get(), i7.get(), i8.get()]
	for i in y:
		i.delete(0, END)
	if count % 2 == 0:
		main.insert(parent='', index='end', iid=count, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), tags=('evenrow',))
	else:
		main.insert(parent='', index='end', iid=count, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), tags=('oddrow',))
	count+=1

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
	  ["Praveen", "Varma", "11", "Gratia", "Tour", "Core", "Savanqa Green", "A-1006 Icon Trinity, Pune MH -422017", "102000"],
]
add_data(data_list)

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
l8 = Label(finput, text='Total', bg='#020010', fg='silver')
# Input - Entrys
i0 = Entry(finput)
i1 = Entry(finput)
i2 = Entry(finput)
i3 = Entry(finput)
i4 = Entry(finput)
i5 = Entry(finput)
i6 = Entry(finput)
i7 = Entry(finput)
i8 = Entry(finput)
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
l8.grid(row=1, column=6, padx=10, pady=10)
i8.grid(row=1, column=7, padx=10, pady=10)

# Buttons
b0 = Button(fbutton, text='Add Record', bg='#020010', fg='silver', relief='groove', command=add_button)
b1 = Button(fbutton, text='Remove Record', bg='#020010', fg='silver', relief='groove')
b2 = Button(fbutton, text='Update Record', bg='#020010', fg='silver', relief='groove')
b3 = Button(fbutton, text='Move Up', bg='#020010', fg='silver', relief='groove')
b4 = Button(fbutton, text='Move Down', bg='#020010', fg='silver', relief='groove')
b5 = Button(fbutton, text='Remove All', bg='#020010', fg='silver', relief='groove')
b6 = Button(fbutton, text='Remove Multiple', bg='#020010', fg='silver', relief='groove')

b0.grid(row=0, column=0, padx=20,pady=10)
b1.grid(row=0, column=1, padx=20,pady=10)
b2.grid(row=0, column=2, padx=20,pady=10)
b3.grid(row=0, column=3, padx=20,pady=10)
b4.grid(row=0, column=4, padx=20,pady=10)
b5.grid(row=0, column=5, padx=20,pady=10)
b6.grid(row=0, column=6, padx=20,pady=10)

root.mainloop()