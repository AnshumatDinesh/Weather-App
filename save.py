import tkinter
import os#saving data to a external csv file
import csv
def data():
	sav=tkinter.Toplevel()
	sav.geometry('250x100')
	sav.configure(bg='#262525')
	sav.tk.call('wm', 'iconphoto', sav._w, tkinter.PhotoImage(file=r'Icon\bitmap.png'))	
	def open_save():
		path=r'Database.csv'
		os.system(path)
	def delete_data():
		with open('DATABASE.csv','w') as fil:
			fld=['timestamp','Location','Temperature','AQI','Pressure','Humidity','High/Low','Sunset','Sunrise','Precipitation',
			'UV index','Condition']
			fil_w=csv.writer(fil,delimiter=',')
			fil_w.writerow(fld)

	open_button=tkinter.Button(sav,text='Open Save File',font=("Segoe UI", 18),padx=40,justify='left'
	,background='#262525',fg='#ffffff',command=open_save)

	delete_button=tkinter.Button(sav,text='Delete Save File',font=("Segoe UI", 18),padx=36,justify='left'
	,background='#262525',fg='#ffffff',command=delete_data)
	
	open_button.grid(row=1,column=0)
	delete_button.grid(row=2,column=0)
	sav.mainloop()
