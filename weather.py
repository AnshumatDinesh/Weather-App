#Importing Modules Needed
import categorize
import tkinter  #For GUI
import requests #For  Importing API
import json #For Decoding API 
import categorize # Custom Module To Get Category Of Pollution
import iploc 
import iconsel
import csv
import save
from tkinter import ttk
#Making The window
default_loc=iploc.loc()
rt=tkinter.Toplevel()
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
#Importing The API For Pollution And Current Weather
api_requests=requests.get('http://api.airvisual.com/v2/city?city='+cit+'&state='+sat+'&country=India&key=d06a8ffa-6c03-4395-a8b3-6172ac02d2e0')
api1=json.loads(api_requests.content)
api2_requests=requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key})
api2=json.loads(api2_requests.content)
api3_requests=requests.get('http://api.weatherapi.com/v1/forecast.json?key=320fa44ea12c4f64891104302201909&q='+cit+'&days=1')
api3=json.loads(api3_requests.content)
#Location Data
a=api1['data']
curr=a['current']
City=a['city']
State=a['state']
Country=a['country']
Loc=a['location']
Lat=Loc['coordinates'][1]
Long=Loc['coordinates'][0]
Weather=curr['weather']
W_temp=str(Weather['tp'])+'C'
#Pollution Data
Pollution=curr['pollution']
p_AQI=Pollution['aqius']
p_main=Pollution['mainus']
w_color=categorize.categorize(p_AQI)
#Weather Data
ts=api2['location']['localtime']
b=api2['current']
W_condition=b['condition']['text']
W_feelslike=b['feelslike_c']
W_hu=b['humidity']
W_pressure=b['pressure_mb']
W_wind=b['wind_kph']
W_visi=b['vis_km']
W_uv=b['uv']
#Forecast Data
c=api3['forecast']
c1=c['forecastday']
F_h=c1[0]['day']['maxtemp_c']
F_l=c1[0]['day']['mintemp_c']
F_precp=c1[0]['day']['totalprecip_mm']
F_rain=c1[0]['day']['daily_chance_of_rain']
F_srise=c1[0]['astro']['sunrise']
F_sset=c1[0]['astro']['sunset']
hourset=int(F_sset[1])+12
#Importing The API For Six Hour Segments Weather
api4_requests=requests.get('https://api.weather.com/v1/geocode/'+str(Lat)+'/-'+str(Long)+'/forecast/intraday/3day.json?units=m&language=en-US&apiKey=dc5ea0e10f11465f9ea0e10f11e65fa6')
api4=json.loads(api4_requests.content)
#Six Hour Segment Data
frcst_hrl=api4['forecasts']
frcst_morning=frcst_hrl[2]
frcst_morning_temp=frcst_morning["temp"]
frcst_morning_condition=frcst_morning["phrase_32char"]
frcst_afternoon=frcst_hrl[3]
frcst_afternoon_temp=frcst_afternoon["temp"]
frcst_afternoon_condition=frcst_afternoon["phrase_32char"]
frcst_evening=frcst_hrl[4]
frcst_evening_temp=frcst_evening["temp"]
frcst_evening_condition=frcst_evening["phrase_32char"]
frcst_overnight=frcst_hrl[5]
frcst_overnight_temp=frcst_overnight["temp"]
frcst_overnight_condition=frcst_overnight["phrase_32char"]
#Making The Window
root1=tkinter.Toplevel()
root1.title('Weather')
root1.geometry('1300x1300')
root1.configure(bg='#262525')
root1.tk.call('wm', 'iconphoto', root1._w, tkinter.PhotoImage(file=r'bitmap.png'))
#Hover over message

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
cncrain=tkinter.Label(root,text='Chance of Rain  '+str(F_rain)+'%',font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
sunrise=tkinter.Label(root,text='Sunrise  '+F_srise,font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')
senset=tkinter.Label(root,text='Sunset  '+F_sset,font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')

l1.grid(row=7,columnspan=4)
feelslike.grid(row=8,column=0)
wind.grid(row=8,column=3)
humidity.grid(row=9,column=0)
pressure.grid(row=9,column=3)
visibility.grid(row=10,column=0)
UV.grid(row=10,column=3)
hilo.grid(row=11,column=0)
precep.grid(row=11,column=3)
cncrain.grid(row=12,column=0)
sunrise.grid(row=13,column=0)
senset.grid(row=13,column=3)
#Third Set of Data Labels
alerts_name=tkinter.Label(root,text='ALERTS',font=("Segoe UI", 30),justify='left',background='#262525',fg='#ffffff')
alerts=tkinter.Label(root,text=al,font=("Segoe UI", 20),justify='left',background='#262525',fg='#ffffff')

alerts_name.grid(row=15,column=0)
alerts.grid(row=16,column=0)
#Fourth Set of Data Labels
l2=tkinter.Label(root,text='Forecast for '+var,font=("Segoe UI", 30),justify='left',background='#262525',fg='#ffffff')
mrng=tkinter.Label(root,text='MORNING',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
mrng_temp=tkinter.Label(root,text=str(frcst_morning_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
aft=tkinter.Label(root,text='AFTERNOON',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
aft_temp=tkinter.Label(root,text=str(frcst_afternoon_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
evn=tkinter.Label(root,text='EVENING',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
evn_temp=tkinter.Label(root,text=str(frcst_evening_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
ovn=tkinter.Label(root,text='OVERNIGHT',font=("Segoe UI", 30),background='#262525',fg='#ffffff')
ovn_temp=tkinter.Label(root,text=str(frcst_evening_temp)+'C',font=("Segoe UI", 30),background='#262525',fg='#ffffff')

l2.grid(row=18,columnspan=4)
mrng.grid(row=20,column=0)
mrng_temp.grid(row=22,column=0)
aft.grid(row=20,column=1)
aft_temp.grid(row=22,column=1)
evn.grid(row=20,column=2)
evn_temp.grid(row=22,column=2)
ovn.grid(row=20,column=3)
ovn_temp.grid(row=22,column=3)
#Partitions B/W The Partitions
prtition1=tkinter.Label(root,text='____________________________________________________________________________________________________________________________________________________________________________',font=("Segoe UI", 14),fg='#ffffff',background='#262525',justify='left')
prtition2=tkinter.Label(root,text='____________________________________________________________________________________________________________________________________________________________________________',font=("Segoe UI", 14),fg='#ffffff',justify='left',background='#262525')
prtition3=tkinter.Label(root,text='____________________________________________________________________________________________________________________________________________________________________________',font=("Segoe UI", 14),fg='#ffffff',justify='left',background='#262525')

prtition1.grid(row=6,columnspan=5)
prtition2.grid(row=14,columnspan=5)
prtition3.grid(row=17,columnspan=5)
#Photo Logos
photo=iconsel.icon(W_condition,hourset)
logo=tkinter.Label(root,image=photo,bg='#262525')
logo.grid(row=4,column=3)
photo_mrng=iconsel.icon(frcst_morning_condition,hourset)
logo_mrng=tkinter.Label(root,image=photo_mrng,bg='#262525')
logo_mrng.grid(row=21,column=0)

photo_aft=iconsel.icon(frcst_afternoon_condition,hourset)
logo_aft=tkinter.Label(root,image=photo_aft,bg='#262525')
logo_aft.grid(row=21,column=1)

photo_evn=iconsel.icon(frcst_evening_condition,hourset)
logo_evn=tkinter.Label(root,image=photo_evn,bg='#262525')
logo_evn.grid(row=21,column=2)

photo_ovn=iconsel.icon(frcst_overnight_condition,hourset)
logo_ovn=tkinter.Label(root,image=photo_ovn,bg='#262525')
logo_ovn.grid(row=21,column=3)
#csv Database Link
database=tkinter.Button(root,text='DATABASE',font=("Segoe UI", 14),justify='left',background='#262525',fg='#ffffff',command= save.data)
database.grid(row=23,column=3)
W_hilo= str(F_h)+'/'+str(F_l)
with open('DATABASE.csv','a') as fil:
	fld=[ts,var,W_temp,p_AQI,W_pressure,W_hu,W_hilo,F_sset,F_srise,F_precp,F_rain,W_uv,W_condition]
	fil_w=csv.writer(fil,delimiter=',')
	fil_w.writerow(fld)
#Ending  Mainloop
root1.mainloop()

search_icon=tkinter.PhotoImage(file=r'Icon\Buttons\search.png')
search_button=tkinter.Button(rt,image=search_icon,bg='#262525',fg='#ffffff',command=lambda:driver(state_menu.get())) 
search_button.grid(row=1,column=2)
state_menu.grid(row=1,column=1) 
rt.mainloop()
main()
