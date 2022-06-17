#Importing Modules Needed
import tkinter  #For GUI
import requests #For  Importing API
import json #For Decoding API 
import categorize # Custom Module To Get Category Of Pollution
import iploc 
import iconsel
import csv
import save
import datetime
from tkinter import ttk

# converting unix UTC time to human time
def datecov(n):
	ts=datetime.datetime.fromtimestamp(
        int(str(n))
    ).strftime('%Y-%m-%d %H:%M:%S')
	ts=str(ts)
def datecovstd(n):
	ts=datetime.datetime.fromtimestamp(
        int(str(n))
    ).strftime('%H:%M')
	ts=str(ts)
def datecovhr(n):
	ts=datetime.datetime.fromtimestamp(
        int(str(n))
    ).strftime('%H')	
	ts=str(ts)	
#Making The window
default_loc=iploc.loc()
rt=tkinter.Tk()
rt.title('Weather')
rt.geometry('240x100')
rt.configure(bg='#262525')
rt.tk.call('wm', 'iconphoto', rt._w, tkinter.PhotoImage(file=r'Icon\bitmap.png'))
#Dropdown Module  
                            
st=tkinter.StringVar(rt)
st.set(default_loc)
state_menu=ttk.Combobox(rt,width = 27,state='readonly',textvariable = st)
state_menu['values']=("Rajamahendravaram,Andhra Pradesh","Tirupati,Andhra Pradesh","Visakhapatnam,Andhra Pradesh",
"Gaya,Bihar","Hajipur,Bihar","Khagaul,Bihar","Muzaffarpur,Bihar","Patna,Bihar",
"Bawana,Delhi","Delhi,Delhi","Karol Bagh,Delhi","New Delhi,Delhi","Shahdara,Delhi",
"Adalaj,Gujarat","Ahmedabad,Gujarat","Ankleshwar,Gujarat","Ghandinagar,Gujarat","Naroda,Gujarat","Sarkhej,Gujarat","Vapi,Gujarat",
"Ambala,Haryana","Bahadurgarh,Haryana","Bhiwani,Haryana","Dharuhera,Haryana","Faridabad,Haryana","Fatehabad,Haryana","Firozpur Jhirka,Haryana","Gharaunda,Haryana","Gurugram,Haryana","Hisar,Haryana","Jind,Haryana","Kaithal,Haryana","Narnaul,Haryana","Palwal,Haryana","Rohtak,Haryana","Sirsa,Haryana","Sonipat,Haryana","Thanesar,Haryana",
"Bengaluru,Karnataka","Bijapur,Karnataka","Chik Ballapur,Karnataka","Chikmagalur,Karnataka","Closepet,Karnataka","Gulbarga,Karnataka","Hoskote,Karnataka","Hubli,Karnataka","Mysore,Karnataka",
"Cochin,Kerala","Kannur,Kerala","Kollam,Kerala","Kozhikode,Kerala","Thiruvananthapuram,Kerala",
"Alandi,Maharashtra","Aurangabad,Maharashtra","Borivli,Maharashtra","Chandrapur,Maharashtra","Kalyan,Maharashtra","Lohogaon,Maharashtra","Mumbai,Maharashtra","Nagpur,Maharashtra","Pimpri,Maharashtra","Pune,Maharashtra","Thane,Maharashtra","Uran,Maharashtra","Virar,Maharashtra",
"Brajrajnagar,Odisha","Talcher,Odisha",
"Amritsar,Punjab","Jalandhar,Punjab","Khanna,Punjab","Ludhiana,Punjab","Patiala,Punjab",
"Ajmer,Rajasthan","Alwar,Rajasthan","Jaipur,Rajasthan","Jodhpur,Rajasthan","Pali,Rajasthan","Udaipur,Rajasthan",
"Chennai,Tamil Nadu","Chinnasekkadu,Tamil Nadu","Madukkarai,Tamil Nadu",
"Hyderabad,Telangana",
"Agra,Uttar Pradesh","Baraut,Uttar Pradesh","Bulandshahr,Uttar Pradesh","Dadri,Uttar Pradesh","Dasna,Uttar Pradesh","Ghaziabad,Uttar Pradesh","Hapur,Uttar Pradesh","Kanpur,Uttar Pradesh","Loni,Uttar Pradesh","Lucknow,Uttar Pradesh","Meerut,Uttar Pradesh","Moradabad,Uttar Pradesh","Muzaffarnagar,Uttar Pradesh","Noida,Uttar Pradesh","Varanasi,Uttar Pradesh",
"Asansol,West Bengal","Chakapara,West Bengal","Kolkata,West Bengal","Medinipur,West Bengal","Solap,West Bengal")

state_menu.grid(row=1,column=0)

#Getting City And State Name From Dropdown Menu
var=st.get()
l=len(var)
for i in var:
	if i==',':
		ind=var.index(i)
		global cit
		global sat
		cit=var[0:ind]
		sat=var[ind+1:l]
def driver(st):
#Importing The API For Pollution And Current Weather
	api_requests=requests.get('http://api.airvisual.com/v2/city?city='+cit+'&state='+sat+'&country=India&key=8b66e194-162e-4ff6-b2a5-c3241a6f4d56')
	api1=json.loads(api_requests.content)
	api3_requests=requests.get('http://api.weatherapi.com/v1/forecast.json?key=320fa44ea12c4f64891104302201909&q='+cit+'&days=1')
	api3=json.loads(api3_requests.content)
#Location Data
	b=api1['data']
	curr=b['current']
	City=b['city']
	State=b['state']
	ts=curr['weather']['ts']
	Country=b['country']
	Loc=api1['data']['location']
	Lat=Loc['coordinates'][1]
	Long=Loc['coordinates'][0]
	api2_requests=requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+str(Lat)+'&lon='+str(Long)+'&units=metric&appid=beee5ff2df0480052e233fe82dce2a8d')
	api2=json.loads(api2_requests.content)
	a=api2
#Pollution Data
	Pollution=curr['pollution']
	p_AQI=Pollution['aqius']
	p_main=Pollution['mainus']
	w_color=categorize.categorize(p_AQI)
#Weather Data
	a=api2['current']
	W_temp=a['temp']
	W_condition=a['weather'][0]['description']
	W_feelslike=a['feels_like']
	W_hu=a['humidity']
	W_pressure=a['pressure']
	W_wind=a['wind_speed']
	W_visi=a['visibility']
	W_uv=a['uvi']
#Forecast Data
	c=api2['daily']
	c1=api3['forecast']['forecastday']
	F_h=c[0]['temp']['max']
	F_l=c[0]['temp']['min']
	F_precp=c[0]['pop']
	F_srise=c1[0]['astro']['sunrise']
	F_sset=c1[0]['astro']['sunset']
	z=int(F_sset[0:1])
	hourset=z+12
#Six Hour Segment Data
	frcst_hrl=api2['hourly']
	frcst_morning=frcst_hrl[0]
	frcst_morning_dt= datecovstd(frcst_morning['dt'])
	frcst_morning_temp=frcst_morning["temp"]
	frcst_morning_condition=frcst_morning["weather"][0]['description']
	frcst_morning_pop=frcst_morning["pop"]
	frcst_afternoon=frcst_hrl[4]
	frcst_afternoon_dt= datecovstd(frcst_afternoon['dt'])
	frcst_afternoon_temp=frcst_afternoon["temp"]
	frcst_afternoon_condition=frcst_afternoon["weather"][0]['description']
	frcst_afternoon_pop=frcst_afternoon["pop"]
	frcst_evening=frcst_hrl[6]
	frcst_evening_dt= datecovstd(frcst_evening['dt'])
	frcst_evening_temp=frcst_evening["temp"]
	frcst_evening_condition=frcst_evening["weather"][0]['description']
	frcst_evening_pop=frcst_evening["pop"]
	frcst_overnight=frcst_hrl[10]
	frcst_overnight_dt= datecovstd(frcst_overnight['dt'])
	frcst_overnight_temp=frcst_overnight["temp"]
	frcst_overnight_condition=frcst_overnight["weather"][0]['description']
	frcst_overnight_pop=frcst_overnight["pop"]
#Making The Window
	root1=tkinter.Toplevel()
	root1.title('Weather')
	root1.geometry('1300x1300')
	root1.configure(bg='#262525')
	root1.tk.call('wm', 'iconphoto', root1._w, tkinter.PhotoImage(file=r'Icon/bitmap.png'))
#Creating A Scrollbar Using A Canvas
	main_frame=tkinter.Frame(root1)
	main_frame.pack(fill='both',expand=1)
	main_frame.configure(bg='#262525')
	my_canvas=tkinter.Canvas(main_frame)
	my_canvas.pack(side='left',fill='both',expand=1)
	my_canvas.configure(bg='#262525')
	myscrollbar=tkinter.ttk.Scrollbar(main_frame,orient='vertical',command=my_canvas.yview)
	myscrollbar.pack(side='right',fill='y')


	my_canvas.configure(yscrollcommand=myscrollbar.set)
	my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
	root=tkinter.Frame(my_canvas)
	root.configure(bg='#262525')

	my_canvas.create_window((0,0),window=root,anchor='nw')
#First Set of Data Labels
	city_name=tkinter.Label(root,text=City,font=("Segoe UI", 70),justify='left',background='#262525',fg='#ffffff')
	AQI_name=tkinter.Label(root,text='AQI',font=("Segoe UI", 30),justify='left',background='#262525',fg='#ffffff')
	AQI_val=tkinter.Label(root,text=p_AQI,relief="ridge",font=("Segoe UI", 30),background=w_color,justify='left')
	state_name=tkinter.Label(root,text=State+','+Country,font=("Segoe UI", 30),justify='left',background='#262525',fg='#ffffff')
	temp=tkinter.Label(root,text=W_temp,font=("Segoe UI", 30),justify='left',background='#262525',fg='#ffffff')
	condition=tkinter.Label(root,text=W_condition,font=("Segoe UI", 18),justify='left',background='#262525',fg='#ffffff')

	city_name.grid(row=2,column=0)
	AQI_name.grid(row=2,column=2)
	AQI_val.grid(row=2,column=3)
	state_name.grid(row=3,column=0)
	temp.grid(row=3,column=3)
	condition.grid(row=5,column=3)
#Second Set of Data Labels
	l1=tkinter.Label(root,text='Weather Today in '+var,font=("Segoe UI", 34),justify='left',background='#262525',fg='#ffffff')
	feelslike=tkinter.Label(root,text='Feels Like  '+str(W_feelslike)+'C',font=("Segoe UI", 20),justify='left',fg='#ffffff',background='#262525')
	humidity=tkinter.Label(root,text='Humidity  '+str(W_hu)+'%',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	pressure=tkinter.Label(root,text='Pressure  '+str(W_pressure)+'mb',font=("Segoe UI", 20),justify='left',fg='#ffffff',background='#262525')
	wind=tkinter.Label(root,text='Wind  '+str(W_wind)+'Kmph',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	visibility=tkinter.Label(root,text='Visibility  '+str(W_visi)+'Km',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	UV=tkinter.Label(root,text='UV Index  '+str(W_uv)+' of 10',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	hilo=tkinter.Label(root,text='High/Low  '+str(F_h)+'/'+str(F_l)+'C',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	precep=tkinter.Label(root,text='Precipitation  '+str(F_precp)+' mm',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	sunrise=tkinter.Label(root,text='Sunrise  '+str(F_srise),font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
	senset=tkinter.Label(root,text='Sunset  '+str(F_sset),font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')

	l1.grid(row=7,columnspan=4)
	feelslike.grid(row=8,column=0)
	wind.grid(row=8,column=3)
	humidity.grid(row=9,column=0)
	pressure.grid(row=9,column=3)
	visibility.grid(row=10,column=0)
	UV.grid(row=10,column=3)
	hilo.grid(row=11,column=0)
	precep.grid(row=11,column=3)
	sunrise.grid(row=13,column=0)
	senset.grid(row=13,column=3)
#third Set of Data Labels
	l2=tkinter.Label(root,text='Forecast for '+var,font=("Segoe UI", 30),justify='left',background='#262525',fg='#ffffff')
	mrng=tkinter.Label(root,text='5 Hour Ago',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	mrng_temp=tkinter.Label(root,text=str(frcst_morning_temp)+'°C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	mrng_pop=tkinter.Label(root,text=str(frcst_morning_pop)+'%',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	aft=tkinter.Label(root,text="An Hour Ago",font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	aft_temp=tkinter.Label(root,text=str(frcst_afternoon_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	aft_pop=tkinter.Label(root,text=str(frcst_afternoon_pop)+'%',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	evn=tkinter.Label(root,text='An hour Later',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	evn_temp=tkinter.Label(root,text=str(frcst_evening_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	evn_pop=tkinter.Label(root,text=str(frcst_evening_pop)+'%',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	ovn=tkinter.Label(root,text='5 Hour Later',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	ovn_temp=tkinter.Label(root,text=str(frcst_overnight_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
	ovn_pop=tkinter.Label(root,text=str(frcst_overnight_pop)+'%',font=("Segoe UI", 30),background='#262525',fg='#ffffff')

	l2.grid(row=18,columnspan=4)
	mrng.grid(row=20,column=0)
	mrng_temp.grid(row=22,column=0)
	mrng_pop.grid(row=23,column=0)
	aft.grid(row=20,column=1)
	aft_temp.grid(row=22,column=1)
	aft_pop.grid(row=23,column=1)
	evn.grid(row=20,column=2)
	evn_temp.grid(row=22,column=2)
	evn_pop.grid(row=23,column=2)
	ovn.grid(row=20,column=3)
	ovn_temp.grid(row=22,column=3)
	ovn_pop.grid(row=23,column=3)
#Partitions B/W The Partitions
	prtition1=tkinter.Label(root,text='____________________________________________________________________________________________________________________________________________________________________________',font=("Segoe UI", 14),fg='#ffffff',background='#262525',justify='left')
	prtition3=tkinter.Label(root,text='____________________________________________________________________________________________________________________________________________________________________________',font=("Segoe UI", 14),fg='#ffffff',justify='left',background='#262525')

	prtition1.grid(row=6,columnspan=5)
	prtition3.grid(row=17,columnspan=5)
#Photo Logos
	photo=iconsel.icon(a['weather'][0]['icon'])
	logo=tkinter.Label(root,image=photo,bg='#262525')
	logo.grid(row=4,column=3)
	photo_mrng=iconsel.icon(frcst_morning["weather"][0]['icon'])
	logo_mrng=tkinter.Label(root,image=photo_mrng,bg='#262525')
	logo_mrng.grid(row=21,column=0)

	photo_aft=iconsel.icon(frcst_afternoon["weather"][0]['icon'])
	logo_aft=tkinter.Label(root,image=photo_aft,bg='#262525')
	logo_aft.grid(row=21,column=1)

	photo_evn=iconsel.icon(frcst_evening["weather"][0]['icon'])
	logo_evn=tkinter.Label(root,image=photo_evn,bg='#262525')
	logo_evn.grid(row=21,column=2)

	photo_ovn=iconsel.icon(frcst_overnight["weather"][0]['icon'])
	logo_ovn=tkinter.Label(root,image=photo_ovn,bg='#262525')
	logo_ovn.grid(row=21,column=3)
#csv Database Link
	database=tkinter.Button(root,text='DATABASE',font=("Segoe UI", 14),justify='left',background='#262525',fg='#ffffff',command= save.data)
	database.grid(row=24,column=3)
	W_hilo= str(F_h)+'/'+str(F_l)
	with open('DATABASE.csv','a') as fil:
		fld=[ts,var,W_temp,p_AQI,W_pressure,W_hu,W_hilo,F_sset,F_srise,F_precp,W_uv,W_condition]
		fil_w=csv.writer(fil,delimiter=',')
		fil_w.writerow(fld)
#Ending  Mainloop
	root1.mainloop()

search_icon=tkinter.PhotoImage(file=r'Icon\Buttons\search.png')
search_button=tkinter.Button(rt,image=search_icon,bg='#262525',fg='#ffffff',command=lambda:driver(state_menu.get())) 
search_button.grid(row=1,column=2)
state_menu.grid(row=1,column=1) 
rt.mainloop()