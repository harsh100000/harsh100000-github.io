import tkinter as tk
from tkinter import font, mainloop
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" +city +"&appid=c5c720a22ac1fd7c3f7badcbebdcc4d7"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-19800))

    final_info = condition + "\n" + str(temp) + " °C"
    final_data = "\n" + "Max Temp: " + str(max_temp) +"°C"+ "\n" + "Min Temp: " + str(min_temp) +"°C"+ "\n" + "Pressure: " + str(pressure) +" mmHg"+ "\n" + "humidity: " + str(humidity) +"%"+ "\n" + "Wind Speed: " + str(wind) +" Km/H"+ "\n" + "Sun Rise: " + str(sunrise) + "\n" + "Sun Set: " + str(sunset)

    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady=20)
textfield.focus()

textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()  
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()