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
data=[["Robert", "Clive", "1", "Rugiet", "Race", "Elite", "Volcanic Red", "h4-101 st. LA -32001", "135000"],
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

global count
count = 0
for rec in data:
	if count % 2 == 0:
		main.insert(parent='', index='end', iid=count, text='', values=(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8]), tags=('evenrow',))
	else:
		main.insert(parent='', index='end', iid=count, text='', values=(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8]), tags=('oddrow',))
	count+=1

root.mainloop()