from weather import *

def main():
    loc1 = locator()
    loc1.get_loc()
    selection(loc1)
    r1 = reporter(loc1)
    r1.load_data()
    # creating a window
    root = tkinter.Tk()
    root.title('Weather')
    root.geometry('900x600')
    root.configure(bg='#262525')
    root.tk.call('wm', 'iconphoto', root._w,
                 tkinter.PhotoImage(file=r'Icon/bitmap.png'))
    # Creating A Scrollbar Using A Canvas
    main_frame = tkinter.Frame(root)
    main_frame.pack(fill='both', expand=1)
    main_frame.configure(bg='#262525')
    my_canvas = tkinter.Canvas(main_frame)
    my_canvas.pack(side='left', fill='both', expand=1)
    my_canvas.configure(bg='#262525')
    myscrollbar = tkinter.ttk.Scrollbar(
        main_frame, orient='vertical', command=my_canvas.yview)
    myscrollbar.pack(side='right', fill='y')
    my_canvas.configure(yscrollcommand=myscrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox('all')))
    root = tkinter.Frame(my_canvas)
    root.configure(bg='#262525')
    my_canvas.create_window((0, 0), window=root, anchor='nw')
    # First Set of Data Labels
    city_name = tkinter.Label(root, text=loc1.location["City"], font=(
        "Segoe UI", 70), justify='left', background='#262525', fg='#ffffff')
    AQI_name = tkinter.Label(root, text='AQI', font=(
        "Segoe UI", 30), justify='left', background='#262525', fg='#ffffff')
    AQI_val = tkinter.Label(root, text=r1.data["P_AQI"], relief="ridge", font=(
        "Segoe UI", 30), background=categorize(r1.data["P_AQI"]), justify='left')
    state_name = tkinter.Label(root, text=loc1.location["State"]+',India', font=(
        "Segoe UI", 30), justify='left', background='#262525', fg='#ffffff')
    temp = tkinter.Label(root, text=r1.data["W_temp"], font=(
        "Segoe UI", 30), justify='left', background='#262525', fg='#ffffff')
    condition = tkinter.Label(root, text=r1.data["W_condition"], font=(
        "Segoe UI", 18), justify='left', background='#262525', fg='#ffffff')
    city_name.grid(row=2, column=0)
    AQI_name.grid(row=2, column=2, padx=100)
    AQI_val.grid(row=2, column=3)
    state_name.grid(row=3, column=0)
    temp.grid(row=3, column=3)
    condition.grid(row=5, column=3)
    # Second Set of Data Labels
    l1 = tkinter.Label(root, text='Weather Today in '+loc1.get_string(), font=("Segoe UI",
                       34), justify='left', background='#262525', fg='#ffffff')
    feelslike = tkinter.Label(root, text='Feels Like  '+str(r1.data["W_feelslike"])+'C', font=(
        "Segoe UI", 20), justify='left', fg='#ffffff', background='#262525')
    humidity = tkinter.Label(root, text='Humidity  '+str(r1.data["W_humidity"])+'%', font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    pressure = tkinter.Label(root, text='Pressure  '+str(r1.data["W_pressure"])+'mb', font=(
        "Segoe UI", 20), justify='left', fg='#ffffff', background='#262525')
    wind = tkinter.Label(root, text='Wind  '+str(r1.data["W_wind"])+'Kmph', font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    visibility = tkinter.Label(root, text='Visibility  '+str(r1.data["W_visi"])+'Km', font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    UV = tkinter.Label(root, text='UV Index  '+str(r1.data["W_uv"])+' of 10', font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    hilo = tkinter.Label(root, text='High/Low  '+str(r1.data["F_high"])+'/'+str(r1.data["F_low"])+'C', font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    precep = tkinter.Label(root, text='Precipitation  '+str(r1.data["F_precip"])+' mm', font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    sunrise = tkinter.Label(root, text='Sunrise  '+str(r1.data["F_srise"]), font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')
    senset = tkinter.Label(root, text='Sunset  '+str(r1.data["F_sset"]), font=(
        "Segoe UI", 20), justify='left', background='#262525', fg='#ffffff')

    l1.grid(row=7, columnspan=4)
    feelslike.grid(row=8, column=0)
    wind.grid(row=8, column=3)
    humidity.grid(row=9, column=0)
    pressure.grid(row=9, column=3)
    visibility.grid(row=10, column=0)
    UV.grid(row=10, column=3)
    hilo.grid(row=11, column=0)
    precep.grid(row=11, column=3)
    sunrise.grid(row=13, column=0)
    senset.grid(row=13, column=3)
    # third Set of Data Labels
    l2 = tkinter.Label(root, text='Forecast for '+loc1.get_string(), font=("Segoe UI", 30),
                       justify='left', background='#262525', fg='#ffffff')
    mrng = tkinter.Label(root, text='5 Hour Ago', font=(
        "Segoe UI", 30), background='#262525', fg='#ffffff')
    mrng_temp = tkinter.Label(root, text=str(
        r1.data["F_mor"]["Temp"])+'°C', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    mrng_pop = tkinter.Label(root, text=str(
        r1.data["F_mor"]["Condition"])+'%', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    aft = tkinter.Label(root, text="An Hour Ago", font=(
        "Segoe UI", 30), background='#262525', fg='#ffffff')
    aft_temp = tkinter.Label(root, text=str(
        r1.data["F_aft"]["Temp"])+'C', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    aft_pop = tkinter.Label(root, text=str(
        r1.data["F_aft"]["Condition"])+'%', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    evn = tkinter.Label(root, text='An hour Later', font=(
        "Segoe UI", 30), background='#262525', fg='#ffffff')
    evn_temp = tkinter.Label(root, text=str(
        r1.data["F_even"]["Temp"])+'C', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    evn_pop = tkinter.Label(root, text=str(
        r1.data["F_even"]["Condition"])+'%', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    ovn = tkinter.Label(root, text='5 Hour Later', font=(
        "Segoe UI", 30), background='#262525', fg='#ffffff')
    ovn_temp = tkinter.Label(root, text=str(
        r1.data["F_ovn"]["Temp"])+'C', font=("Segoe UI", 30), background='#262525', fg='#ffffff')
    ovn_pop = tkinter.Label(root, text=str(
        r1.data["F_ovn"]["Condition"])+'%', font=("Segoe UI", 30), background='#262525', fg='#ffffff')

    l2.grid(row=18, columnspan=4)
    mrng.grid(row=20, column=0)
    mrng_temp.grid(row=22, column=0)
    mrng_pop.grid(row=23, column=0)
    aft.grid(row=20, column=1)
    aft_temp.grid(row=22, column=1)
    aft_pop.grid(row=23, column=1)
    evn.grid(row=20, column=2)
    evn_temp.grid(row=22, column=2)
    evn_pop.grid(row=23, column=2)
    ovn.grid(row=20, column=3)
    ovn_temp.grid(row=22, column=3)
    ovn_pop.grid(row=23, column=3)
    # Partitions B/W The Partitions
    prtition1 = tkinter.Label(root, text='___________________________________________________________________________________________________________________________________________________________________', font=(
        "Segoe UI", 14), fg='#ffffff', background='#262525', justify='left')
    prtition3 = tkinter.Label(root, text='__________________________________________________________________________________________________________________________________________________________________', font=(
        "Segoe UI", 14), fg='#ffffff', justify='left', background='#262525')

    prtition1.grid(row=6, columnspan=5)
    prtition3.grid(row=17, columnspan=5)
# Photo Logos
    logo = tkinter.Label(root, image=icon(r1.photo["photo"]), bg='#262525')
    logo.grid(row=4, column=3)
    logo_mrng = tkinter.Label(root, image=icon(r1.photo["ph_mrg"]), bg='#262525')
    logo_mrng.grid(row=21, column=0)

    logo_aft = tkinter.Label(root, image=icon(r1.photo["ph_aft"]), bg='#262525')
    logo_aft.grid(row=21, column=1)

    logo_evn = tkinter.Label(root, image=icon(r1.photo["ph_even"]), bg='#262525')
    logo_evn.grid(row=21, column=2)
    logo_ovn = tkinter.Label(root, image=icon(r1.photo["ph_ovn"]), bg='#262525')
    logo_ovn.grid(row=21, column=3)
# csv Database Link
    database = tkinter.Button(root, text='DATABASE', font=(
        "Segoe UI", 14), justify='left', background='#262525', fg='#ffffff', command=data)
    database.grid(row=24, column=3)
    W_hilo = str(r1.data["F_high"])+'/'+str(r1.data["F_low"])
    with open('DATABASE.csv', 'a') as fil:
        fld = [r1.data["timestamp"],loc1.get_string(), r1.data["W_temp"], r1.data["P_AQI"], r1.data["W_pressure"], r1.data["W_humidity"],
               W_hilo, r1.data["F_sset"], r1.data["F_srise"], r1.data["F_precip"],r1.data["W_uv"], r1.data["W_condition"]]
        fil_w = csv.writer(fil, delimiter=',')
        fil_w.writerow(fld)
    root.mainloop()


main()
