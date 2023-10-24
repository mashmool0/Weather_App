from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import datetime
import requests
import matplotlib.pyplot as plt
import plotly.express as px
# APP INFORMATION
root = Tk()
root.title('Weahter App')
root.iconbitmap('Weather.ico')
root.geometry('900x500+300+200')
root.resizable(0, 0)
# API 213f95374a9ee29ab7041cd44078c47e
# Variable


# ---- Funcitions  -----
# Search Button and update everything

# Search weather INFORMATION


def Search_Weather():
    global textField
    reader = True
    # First Time Set
    time_now = datetime.now().time().strftime('%H:%M %p')
    text_Time.config(text=time_now)
    # Get Weather  Information
    city = textField.get().capitalize()
    api_key = '213f95374a9ee29ab7041cd44078c47e'
    data = get_weather(city, api_key)

    if data == "Fill in the field":
        print(data)
        messagebox.showinfo("Fill in the field",
                            'The field is empty Or your entry is incorrect!')
        reader = False

    try:
        if reader == True:
            wind = data['wind']['speed']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            pressure = data['main']['pressure']
            temp = data['main']['temp']
            temp = str(float(temp) - 273.15)[0:4] + '°C'
            # add information in labels
            winddt.config(text=wind)
            humiditydt.config(text=humidity)
            descriptiondt.config(text=description)
            pressuredt.config(text=pressure)
            degree_label.config(text=temp)
    except:
        messagebox.showerror('Check Your entry ! ',
                             'are you sure about your choice ? ')

    # again refresh
    reader = True


def future_detail():
    # Random tempreture
    print('hello')
    Days = ['saturday', 'sunday', 'monday',
            'tuesday', 'wednesday', 'thursday', 'friday']
    tempreture = [12, 9, 21, 31, 8, 1, 17]
    plt.plot(Days, tempreture, color='purple')
    plt.title('Tempreture Prediction')
    plt.xlabel('Days')
    plt.ylabel('Tempreture')
    plt.show()


def get_weather(city, api_key):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data


# Search box
search_image = PhotoImage(file='Photos/Search.png')
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

# Detail Box
detail_box = PhotoImage(file='Photos/Box.png')
image_detailbox = Label(root, image=detail_box)
image_detailbox.place(y=400, x=65)
# Label on detail box
# sabet ha
wind_label = Label(root, text='WIND', font=(
    'poppins', 14, 'bold'), bg='#1ab5ef')
humidity_label = Label(root, text='HUMIDITY', font=(
    'poppins', 14, 'bold'), bg='#1ab5ef')
description_label = Label(root, text='DESCRIPTION',
                          font=('poppins', 14, 'bold'), bg='#1ab5ef')
pressure_label = Label(root, text='PRESSURE', font=(
    'poppins', 14, 'bold'), bg='#1ab5ef')

# Place of Labels
wind_label.place(x=130, y=420)
humidity_label.place(x=260, y=420)
description_label.place(x=430, y=420)
pressure_label.place(x=630, y=420)

# Future
future = Button(root, text='future', font=(
    'pippin', 20, 'bold'), bg='#404040', fg='white', bd=6, command=lambda: future_detail())
future.place(x=490, y=30)


# moteghayer ha

winddt = Label(root, text='...', bg='#1ab5ef', fg='white',
               font=('poppins', 14, 'bold'))
winddt.place(x=130, y=460)
humiditydt = Label(root, text='...', bg='#1ab5ef', fg='white',
                   font=('poppins', 14, 'bold'))
humiditydt.place(x=260, y=460)
descriptiondt = Label(root, text='...', bg='#1ab5ef', fg='white',
                      font=('poppins', 14, 'bold'))
descriptiondt.place(x=430, y=460)
pressuredt = Label(root, text='...', bg='#1ab5ef', fg='white',
                   font=('poppins', 14, 'bold'))
pressuredt.place(x=630, y=460)
degree_label = Label(root, text='--°C',
                     font=('Arial', 40, 'bold'), fg='red')
degree_label.place(x=410, y=200)


# Text field
textField = tk.Entry(root, justify='center', width=17, font=(
    'poppins', 25, 'bold'), bg='#404040', border=0, fg='white')
textField.place(x=50, y=40)
textField.focus()


#  Button Icaon
Search_icon = PhotoImage(file='Photos/Search_icon.png')
myimage_icon = Button(image=Search_icon, cursor='hand2',
                      borderwidth=0, bg='#404040', command=lambda: Search_Weather())
myimage_icon.place(x=400, y=34)


# Logo
logo_image = PhotoImage(file='Photos/Logo.png')
myimage_logo = Label(image=logo_image)
myimage_logo.place(x=150, y=100)

# Labels
text_label = Label(root, font=('poppins', 17, 'bold'), text='Current Wheater')
text_label.place(x=45, y=100)


# Time Now label
time_now = datetime.now().time().strftime('%H:%M %p')
text_Time = Label(root, font=('poppins', 13,), text=time_now)
text_Time.place(x=50, y=135)


root.mainloop()
