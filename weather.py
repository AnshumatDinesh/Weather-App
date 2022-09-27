import tkinter
import csv
from tkinter import ttk
import requests
import json
import os

def clse(rt):
    rt.destroy()
def icon(c):
	if c=='01d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\01d@2x.png")
		return photo
	if c=='02d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\02d@2x.png")
		return photo
	if c=='03d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\03d@2x.png")
		return photo
	if c=='04d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\04d@2x.png")
		return photo
	if c=='09d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\09d@2x.png")
		return photo
	if c=='10d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\10d@2x.png")
		return photo
	if c=='11d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\11d@2x.png")
		return photo
	if c=='13d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\13d@2x.png")
		return photo
	if c=='50d':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\50d@2x.png")
		return photo
	if c=='01n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\01n@2x.png")
		return photo
	if c=='02n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\02n@2x.png")
		return photo
	if c=='03n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\03n@2x.png")
		return photo
	if c=='04n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\04n@2x.png")
		return photo
	if c=='09n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\09n@2x.png")
		return photo
	if c=='10n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\10n@2x.png")
		return photo
	if c=='11n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\11n@2x.png")
		return photo
	if c=='13n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\13n@2x.png")
		return photo
	if c=='50n':
		photo = tkinter.PhotoImage(file = r"Icon\New Icon\50n@2x.png")
		return photo
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
def categorize(n):  # to categorise AQ
    if n in range(0, 51):
        w_color = '#60ff00'
    elif n in range(51, 101):
        w_color = '#efff08'
    elif n in range(101, 151):
        w_color = '#ffbb00'
    elif n in range(151, 201):
        w_color = '#ff0000'
    elif n in range(201, 301):
        w_color = '#5010ff'
    elif n > 301:
        w_color = '#c50000'
    return w_color


class locator:
    '''This object fetches the users location via their public ip adress '''

    def __init__(self) -> None:
        self.location = {  # This dictionary stores the data of the loction
            "City": "",
            "State": ""
        }
        # This boolean tells us wheather the loction has been fetched successfully or not
        self.status = False
        pass

    def get_loc(self):
        '''This method gets the loction and stores it into the loction dictionary attribute if the locator'''
        loc_req = requests.get('https://ipinfo.io/')
        if(loc_req.status_code == 200):
            self.status = True  # Updating the status to true if the statur code is successful
        loc_json = json.loads(loc_req.content)
        city = loc_json['city']
        state = loc_json['region']
        stlst = ["Andhra Pradesh", "Bihar", "Delhi", "Gujarat", "Haryana", "Karnataka", "Kerala", "Maharashtra", 'Odisha',
                 "Punjab", "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh", "West Bengal"]
        if state in stlst:
            self.location["City"] = city
            self.location["State"] = state
            if state == "Andhra Pradesh":
                if self.location["City"]+","+self.location["State"] not in ["Rajamahendravaram,Andhra Pradesh", "Tirupati,Andhra Pradesh", "Visakhapatnam,Andhra Pradesh"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Bihar":
                if self.location["City"]+","+self.location["State"] not in ["Gaya,Bihar", "Hajipur,Bihar", "Khagaul,Bihar", "Muzaffarpur,Bihar", "Patna,Bihar"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Delhi":
                if self.location["City"]+","+self.location["State"] not in ["Bawana,Delhi", "Delhi,Delhi", "Karol Bagh,Delhi", "New Delhi,Delhi", "Shahdara,Delhi"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Gujarat":
                if self.location["City"]+","+self.location["State"] not in ["Adalaj,Gujarat", "Ahmedabad,Gujarat", "Ankleshwar,Gujarat", "Ghandinagar,Gujarat", "Naroda,Gujarat", "Sarkhej,Gujarat", "Vapi,Gujarat"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Haryana":
                if self.location["City"]+","+self.location["State"] not in ["Ambala,Haryana", "Bahadurgarh,Haryana", "Bhiwani,Haryana", "Dharuhera,Haryana", "Faridabad,Haryana", "Fatehabad,Haryana", "Firozpur Jhirka,Haryana", "Gharaunda,Haryana", "Gurugram,Haryana", "Hisar,Haryana", "Jind,Haryana", "Kaithal,Haryana", "Narnaul,Haryana", "Palwal,Haryana", "Rohtak,Haryana", "Sirsa,Haryana", "Sonipat,Haryana", "Thanesar,Haryana"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Karnataka":
                if self.location["City"]+","+self.location["State"] not in ["Bengaluru,Karnataka", "Bijapur,Karnataka", "Chik Ballapur,Karnataka", "Chikmagalur,Karnataka", "Closepet,Karnataka", "Gulbarga,Karnataka", "Hoskote,Karnataka", "Hubli,Karnataka", "Mysore,Karnataka"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Kerala":
                if self.location["City"]+","+self.location["State"] not in ["Cochin,Kerala", "Kannur,Kerala", "Kollam,Kerala", "Kozhikode,Kerala", "Thiruvananthapuram,Kerala"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Maharashtra":
                if self.location["City"]+","+self.location["State"] not in ["Alandi,Maharashtra", "Aurangabad,Maharashtra", "Borivli,Maharashtra", "Chandrapur,Maharashtra", "Kalyan,Maharashtra", "Lohogaon,Maharashtra", "Mumbai,Maharashtra", "Nagpur,Maharashtra", "Pimpri,Maharashtra", "Pune,Maharashtra", "Thane,Maharashtra", "Uran,Maharashtra", "Virar,Maharashtra"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Odisha":
                if self.location["City"]+","+self.location["State"] not in ["Brajrajnagar,Odisha", "Talcher,Odisha"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Punjab":
                if self.location["City"]+","+self.location["State"] not in ["Amritsar,Punjab", "Jalandhar,Punjab", "Khanna,Punjab", "Ludhiana,Punjab", "Patiala,Punjab"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Rajasthan":
                if self.location["City"]+","+self.location["State"] not in ["Ajmer,Rajasthan", "Alwar,Rajasthan", "Jaipur,Rajasthan", "Jodhpur,Rajasthan", "Pali,Rajasthan", "Udaipur,Rajasthan"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Tamil Nadu":
                if self.location["City"]+","+self.location["State"] not in ["Chennai,Tamil Nadu", "Chinnasekkadu,Tamil Nadu", "Madukkarai,Tamil Nadu"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Telangana":
                if self.location["City"]+","+self.location["State"] not in ["Hyderabad,Telangana"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "Uttar Pradesh":
                if self.location["City"]+","+self.location["State"] not in ["Agra,Uttar Pradesh", "Baraut,Uttar Pradesh", "Bulandshahr,Uttar Pradesh", "Dadri,Uttar Pradesh", "Dasna,Uttar Pradesh", "Ghaziabad,Uttar Pradesh", "Hapur,Uttar Pradesh", "Kanpur,Uttar Pradesh", "Loni,Uttar Pradesh", "Lucknow,Uttar Pradesh", "Meerut,Uttar Pradesh", "Moradabad,Uttar Pradesh", "Muzaffarnagar,Uttar Pradesh", "Noida,Uttar Pradesh", "Varanasi,Uttar Pradesh"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
            elif state == "West Bengal":
                if self.location["City"]+","+self.location["State"] not in ["Asansol,West Bengal", ",West Bengal", "Chakapara,West Bengal", "Kolkata,West Bengal", "Medinipur,West Bengal", "Solap,West Bengal"]:
                    self.location["City"] = ""
                    self.location["State"] = ""
        else:
            self.location["City"] = ""
            self.location["State"] = ""

    def get_string(self):
        '''Returns the string in a format of City,State or if the location is not supported ---Select--- '''
        if(not self.status):
            self.get_loc()
        if(self.location["City"] == ""):
            return "---Select---"
        return self.location["City"]+","+self.location["State"]

    def set_loc(self, loc_string, win):
        self.location["City"] = loc_string.split(',')[0]
        self.location["State"] = loc_string.split(',')[1]
        clse(win)


def selection(locator1):
    rt = tkinter.Tk()
    rt.title('Weather')
    rt.geometry('240x100')
    rt.configure(bg='#262525')
    rt.tk.call('wm', 'iconphoto', rt._w,
               tkinter.PhotoImage(file=r'Icon\bitmap.png'))
    st = tkinter.StringVar(rt)
    st.set(locator1.get_string())
    state_menu = ttk.Combobox(rt, width=27, state='readonly', textvariable=st)
    state_menu['values'] = ("Rajamahendravaram,Andhra Pradesh", "Tirupati,Andhra Pradesh", "Visakhapatnam,Andhra Pradesh",
                            "Gaya,Bihar", "Hajipur,Bihar", "Khagaul,Bihar", "Muzaffarpur,Bihar", "Patna,Bihar",
                            "Bawana,Delhi", "Delhi,Delhi", "Karol Bagh,Delhi", "New Delhi,Delhi", "Shahdara,Delhi",
                            "Adalaj,Gujarat", "Ahmedabad,Gujarat", "Ankleshwar,Gujarat", "Ghandinagar,Gujarat", "Naroda,Gujarat", "Sarkhej,Gujarat", "Vapi,Gujarat",
                            "Ambala,Haryana", "Bahadurgarh,Haryana", "Bhiwani,Haryana", "Dharuhera,Haryana", "Faridabad,Haryana", "Fatehabad,Haryana", "Firozpur Jhirka,Haryana", "Gharaunda,Haryana", "Gurugram,Haryana", "Hisar,Haryana", "Jind,Haryana", "Kaithal,Haryana", "Narnaul,Haryana", "Palwal,Haryana", "Rohtak,Haryana", "Sirsa,Haryana", "Sonipat,Haryana", "Thanesar,Haryana",
                            "Bengaluru,Karnataka", "Bijapur,Karnataka", "Chik Ballapur,Karnataka", "Chikmagalur,Karnataka", "Closepet,Karnataka", "Gulbarga,Karnataka", "Hoskote,Karnataka", "Hubli,Karnataka", "Mysore,Karnataka",
                            "Cochin,Kerala", "Kannur,Kerala", "Kollam,Kerala", "Kozhikode,Kerala", "Thiruvananthapuram,Kerala",
                            "Alandi,Maharashtra", "Aurangabad,Maharashtra", "Borivli,Maharashtra", "Chandrapur,Maharashtra", "Kalyan,Maharashtra", "Lohogaon,Maharashtra", "Mumbai,Maharashtra", "Nagpur,Maharashtra", "Pimpri,Maharashtra", "Pune,Maharashtra", "Thane,Maharashtra", "Uran,Maharashtra", "Virar,Maharashtra",
                            "Brajrajnagar,Odisha", "Talcher,Odisha",
                            "Amritsar,Punjab", "Jalandhar,Punjab", "Khanna,Punjab", "Ludhiana,Punjab", "Patiala,Punjab",
                            "Ajmer,Rajasthan", "Alwar,Rajasthan", "Jaipur,Rajasthan", "Jodhpur,Rajasthan", "Pali,Rajasthan", "Udaipur,Rajasthan",
                            "Chennai,Tamil Nadu", "Chinnasekkadu,Tamil Nadu", "Madukkarai,Tamil Nadu",
                            "Hyderabad,Telangana",
                            "Agra,Uttar Pradesh", "Baraut,Uttar Pradesh", "Bulandshahr,Uttar Pradesh", "Dadri,Uttar Pradesh", "Dasna,Uttar Pradesh", "Ghaziabad,Uttar Pradesh", "Hapur,Uttar Pradesh", "Kanpur,Uttar Pradesh", "Loni,Uttar Pradesh", "Lucknow,Uttar Pradesh", "Meerut,Uttar Pradesh", "Moradabad,Uttar Pradesh", "Muzaffarnagar,Uttar Pradesh", "Noida,Uttar Pradesh", "Varanasi,Uttar Pradesh",
                            "Asansol,West Bengal", "Chakapara,West Bengal", "Kolkata,West Bengal", "Medinipur,West Bengal", "Solap,West Bengal")
    state_menu.grid(row=1, column=0)
    search_icon = tkinter.PhotoImage(file=r'Icon\Buttons\search.png')
    search_button = tkinter.Button(rt, image=search_icon, bg='#262525',
                                   fg='#ffffff', command=lambda: locator1.set_loc(state_menu.get(), rt))
    search_button.grid(row=1, column=2)
    state_menu.grid(row=1, column=1)
    rt.mainloop()


class reporter:
    def __init__(self, locator1) -> None:
        self.loc = locator1
        self.data = {
            "loc": [],
            "timestamp": "",
            "P_AQI": "",
            "W_temp": "",
            "W_condition": "",
            "W_feelslike": "",
            "W_humidity": "",
            "W_pressure": "",
            "W_wind": "",
            "W_visi": "",
            "W_uv": "",
            "F_high": "",
            "F_low": "",
            "F_precip": "",
            "F_rain": "",
            "F_srise": "",
            "F_sset": "",
            "F_mor": {
                "Temp": "",
                "Condition": ""},
            "F_aft": {
                "Temp": "",
                "Condition": ""},
            "F_even": {
                "Temp": "",
                "Condition": ""},
            "F_ovn": {
                "Temp": "",
                "Condition": ""}
        }
        self.photo={
            "photo":"",
            "ph_mrg":"",
            "ph_aft":"",
            "ph_even":"",
            "ph_ovn":""
        }
        pass

    def load_data(self):
        # loading data from pollution api
        loader1_req = requests.get('http://api.airvisual.com/v2/city?city=' +
                                   self.loc.location["City"]+'&state='+self.loc.location["State"]+'&country=India&key=8b66e194-162e-4ff6-b2a5-c3241a6f4d56')
        load1 = json.loads(loader1_req.content)
        self.data["loc"] = load1["data"]["location"]["coordinates"]
        self.data["timestamp"] = load1["data"]["current"]["pollution"]["ts"]
        self.data["P_AQI"] = load1["data"]["current"]["pollution"]["aqius"]
        # loading data from weather api
        loader2_req = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+str(
            self.data["loc"][1])+'&lon='+str(self.data["loc"][0])+'&units=metric&appid=beee5ff2df0480052e233fe82dce2a8d')
        load2 = json.loads(loader2_req.content)
        self.data["W_temp"] = load2['current']['temp']
        self.data["W_condition"] = load2['current']['weather'][0]['description']
        self.data["W_feelslike"] = load2['current']['feels_like']
        self.data["W_humidity"] = load2['current']['humidity']
        self.data["W_pressure"] = load2['current']['pressure']
        self.data["W_wind"] = load2['current']['wind_speed']
        self.data["W_visi"] = load2['current']['visibility']
        self.data["W_uv"] = load2['current']['uvi']
        # forecast data
        self.data["F_high"] = load2['daily'][0]['temp']['max']
        self.data["F_low"] = load2['daily'][0]['temp']['min']
        self.data["F_precip"] = load2['daily'][0]['pop']
        #sunrise and sunset
        loader3_requests = requests.get(
            'http://api.weatherapi.com/v1/forecast.json?key=320fa44ea12c4f64891104302201909&q='+self.loc.location["City"]+'&days=1')
        load3 = json.loads(loader3_requests.content)
        self.data["F_srise"] = load3['forecast']['forecastday'][0]['astro']['sunrise']
        self.data["F_sset"] = load3['forecast']['forecastday'][0]['astro']['sunset']
        # Sameday forecasts
        self.data["F_mor"]["Temp"] = load2['hourly'][0]["temp"]
        self.data["F_mor"]["Condition"] = load2['hourly'][0]["pop"]
        self.data["F_aft"]["Temp"] = load2['hourly'][4]["temp"]
        self.data["F_aft"]["Condition"] = load2['hourly'][4]["pop"]
        self.data["F_even"]["Temp"] = load2['hourly'][6]["temp"]
        self.data["F_even"]["Condition"] = load2['hourly'][6]["pop"]
        self.data["F_ovn"]["Temp"] = load2['hourly'][10]["temp"]
        self.data["F_ovn"]["Condition"] = load2['hourly'][10]["pop"]
        #photo
        self.photo["photo"]= load2['current']['weather'][0]['icon']
        self.photo["p_mrg"]= load2['hourly'][0]["weather"][0]['icon']
        self.photo["p_aft"]= load2['hourly'][4]["weather"][0]['icon']
        self.photo["p_even"]= load2['hourly'][6]["weather"][0]['icon']
        self.photo["p_ovn"]= load2['hourly'][10]["weather"][0]['icon']