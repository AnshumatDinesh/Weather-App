import requests
import json #getting automatic location through IP
def loc():
	ip_loc=requests.get('https://ipinfo.io/')
	iploc=json.loads(ip_loc.content)
	city=iploc['city']
	state=iploc['region']
	stlst=["Andhra Pradesh","Bihar","Delhi","Gujarat","Haryana","Karnataka","Kerala","Maharashtra",'Odisha',
	"Punjab","Rajasthan","Tamil Nadu","Telangana","Uttar Pradesh","West Bengal"]
	if state in stlst:
		if state=="Andhra Pradesh":
			loc=city+','+state
			if loc not in ["Rajamahendravaram,Andhra Pradesh","Tirupati,Andhra Pradesh","Visakhapatnam,Andhra Pradesh"]:
				loc='--Select---'
		elif state=="Bihar":
			loc=city+','+state
			if loc not in ["Gaya,Bihar","Hajipur,Bihar","Khagaul,Bihar","Muzaffarpur,Bihar","Patna,Bihar"]:
				loc='--Select---'
		elif state=="Delhi":
			loc=city+','+state
			if loc not in ["Bawana,Delhi","Delhi,Delhi","Karol Bagh,Delhi","New Delhi,Delhi","Shahdara,Delhi"]:
				loc='--Select---'
		elif state=="Gujarat":
			loc=city+','+state
			if loc not in ["Adalaj,Gujarat","Ahmedabad,Gujarat","Ankleshwar,Gujarat","Ghandinagar,Gujarat","Naroda,Gujarat","Sarkhej,Gujarat","Vapi,Gujarat"]:
				loc='--Select---'
		elif state=="Haryana":
			loc=city+','+state
			if loc not in ["Ambala,Haryana","Bahadurgarh,Haryana","Bhiwani,Haryana","Dharuhera,Haryana","Faridabad,Haryana","Fatehabad,Haryana","Firozpur Jhirka,Haryana","Gharaunda,Haryana","Gurugram,Haryana","Hisar,Haryana","Jind,Haryana","Kaithal,Haryana","Narnaul,Haryana","Palwal,Haryana","Rohtak,Haryana","Sirsa,Haryana","Sonipat,Haryana","Thanesar,Haryana"]:
				loc='--Select---'
		elif state=="Karnataka":
			loc=city+','+state
			if loc not in ["Bengaluru,Karnataka","Bijapur,Karnataka","Chik Ballapur,Karnataka","Chikmagalur,Karnataka","Closepet,Karnataka","Gulbarga,Karnataka","Hoskote,Karnataka","Hubli,Karnataka","Mysore,Karnataka"]:
				loc='--Select---'
		elif state=="Kerala":
			loc=city+','+state
			if loc not in ["Cochin,Kerala","Kannur,Kerala","Kollam,Kerala","Kozhikode,Kerala","Thiruvananthapuram,Kerala"]:
				loc='--Select---'
		elif state=="Maharashtra":
			loc=city+','+state
			if loc not in ["Alandi,Maharashtra","Aurangabad,Maharashtra","Borivli,Maharashtra","Chandrapur,Maharashtra","Kalyan,Maharashtra","Lohogaon,Maharashtra","Mumbai,Maharashtra","Nagpur,Maharashtra","Pimpri,Maharashtra","Pune,Maharashtra","Thane,Maharashtra","Uran,Maharashtra","Virar,Maharashtra"]:
				loc='--Select---'
		elif state=="Odisha":
			loc=city+','+state
			if loc not in ["Brajrajnagar,Odisha","Talcher,Odisha"]:
				loc='--Select---'
		elif state=="Punjab":
			loc=city+','+state
			if loc not in ["Amritsar,Punjab","Jalandhar,Punjab","Khanna,Punjab","Ludhiana,Punjab","Patiala,Punjab"]:
				loc='--Select---'
		elif state=="Rajasthan":
			loc=city+','+state
			if loc not in ["Ajmer,Rajasthan","Alwar,Rajasthan","Jaipur,Rajasthan","Jodhpur,Rajasthan","Pali,Rajasthan","Udaipur,Rajasthan"]:
				loc='--Select---'
		elif state=="Tamil Nadu":
			loc=city+','+state
			if loc not in ["Chennai,Tamil Nadu","Chinnasekkadu,Tamil Nadu","Madukkarai,Tamil Nadu"]:
				loc='--Select---'
		elif state=="Telangana":
			loc=city+','+state
			if loc not in ["Hyderabad,Telangana"]:
				loc='--Select---'
		elif state=="Uttar Pradesh":
			loc=city+','+state
			if loc not in ["Agra,Uttar Pradesh","Baraut,Uttar Pradesh","Bulandshahr,Uttar Pradesh","Dadri,Uttar Pradesh","Dasna,Uttar Pradesh","Ghaziabad,Uttar Pradesh","Hapur,Uttar Pradesh","Kanpur,Uttar Pradesh","Loni,Uttar Pradesh","Lucknow,Uttar Pradesh","Meerut,Uttar Pradesh","Moradabad,Uttar Pradesh","Muzaffarnagar,Uttar Pradesh","Noida,Uttar Pradesh","Varanasi,Uttar Pradesh"]:
				loc='--Select---'
		elif state=="West Bengal":
			loc=city+','+state
			if loc not in ["Asansol,West Bengal",",West Bengal","Chakapara,West Bengal","Kolkata,West Bengal","Medinipur,West Bengal","Solap,West Bengal"]:
				loc='---Select---'
	else:
		loc='---Select--'
	return loc