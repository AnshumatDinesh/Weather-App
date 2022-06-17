def categorize(n):# to categorise AQ
	if n in range(0,51):
		p_category='GOOD'
		w_color='#60ff00'
	elif n in range(51,101):
		p_category='MODERATE'
		w_color='#efff08'
	elif n in range(101,151):
		p_category='Unheatlthy for sensitive groups'
		w_color='#ffbb00'
	elif n in range(151,201):
		p_category='UNHEALTHY'
		w_color='#ff0000'
	elif n in range(201,301):
		p_category='VERY UNHEALTHY'
		w_color='#5010ff'
	elif n>301:
		p_category='HAZARDOUS'
		w_color='#c50000'
	return w_color