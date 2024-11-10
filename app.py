import tkinter as tk
from tkinter import *
from tkinter import font
import datetime as dt
import requests

# Function to get weather data
def get_weather():
    city = city_entry.get()  # Get city from input field
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "Enter your own api key"

    url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url).json()

    if response.get("cod") != 200:
        temperature_label.config(text="--°C")
        description_label.config(text="City not found")
        feels_like_label.config(text="")
        humidity_label.config(text="")
        pressure_label.config(text="")
        wind_label.config(text="")
        visibility_label.config(text="")
        sunrise_label.config(text="")
        sunset_label.config(text="")
        return

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    temp = round(kelvin_to_celsius(response['main']['temp']))
    feels_like = round(kelvin_to_celsius(response['main']['feels_like']))
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']
    visibility = response['visibility'] / 1000  
    wind_speed = response['wind']['speed']
    description = response['weather'][0]['description'].capitalize()

    sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise']).strftime('%I:%M %p')
    sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset']).strftime('%I:%M %p')

    temperature_label.config(text=f"{temp}°C")
    description_label.config(text=description)
    feels_like_label.config(text=f"Feels like {feels_like}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    pressure_label.config(text=f"Pressure: {pressure} mb")
    wind_label.config(text=f"Wind: {wind_speed} km/h")
    visibility_label.config(text=f"Visibility: {visibility} km")
    sunrise_label.config(text=f"Sunrise: {sunrise_time}")
    sunset_label.config(text=f"Sunset: {sunset_time}")


root = tk.Tk()
root.title("Weather App")
root.geometry("900x500")
root.configure(bg="#57adff")
root.resizable(False, False)

#icon
icon =PhotoImage(file="images/logo.png")
root.iconphoto(False,icon)


font_large = font.Font(size=30, weight='bold')
font_medium = font.Font(size=18)
font_small = font.Font(size=12)
font_italic = font.Font(size=10, slant="italic")

search_frame = tk.Frame(root, bg="#57adff")
search_frame.place(x=600, y=20)

city_entry = tk.Entry(search_frame, font=font_small, width=20, bd=0, relief="solid")
city_entry.insert(0, "Enter city name")
city_entry.pack(side="left", padx=(0, 10), pady=5)

search_button = tk.Button(search_frame, text="Search", command=get_weather, bg="#FFDDC1", font=font_small, bd=0)
search_button.pack(side="left")

first_row_frame = tk.Frame(root, bg="#ffffff", bd=5, relief="ridge", width=850, height=150)
first_row_frame.place(x=25, y=100)

weather_icon = tk.Label(first_row_frame, text="☀️", bg="#ffffff", font=font_large)
weather_icon.grid(row=0, column=0, padx=15)

temperature_label = tk.Label(first_row_frame, text="--°C", bg="#ffffff", font=font_large)
temperature_label.grid(row=0, column=1, padx=20)

description_label = tk.Label(first_row_frame, text="Weather Description", bg="#ffffff", font=font_medium)
description_label.grid(row=0, column=2, padx=20)

feels_like_label = tk.Label(first_row_frame, text="Feels like --°C", bg="#ffffff", font=font_small)
feels_like_label.grid(row=1, column=2, padx=20, sticky="n")

second_row_frame = tk.Frame(root, bg="#ffffff", bd=5, relief="ridge", width=850, height=100)
second_row_frame.place(x=25, y=270)

humidity_label = tk.Label(second_row_frame, text="Humidity: --%", bg="#ffffff", font=font_small)
humidity_label.grid(row=0, column=0, padx=15, pady=10)

pressure_label = tk.Label(second_row_frame, text="Pressure: -- mb", bg="#ffffff", font=font_small)
pressure_label.grid(row=0, column=1, padx=15, pady=10)

wind_label = tk.Label(second_row_frame, text="Wind: -- km/h", bg="#ffffff", font=font_small)
wind_label.grid(row=0, column=2, padx=15, pady=10)

visibility_label = tk.Label(second_row_frame, text="Visibility: -- km", bg="#ffffff", font=font_small)
visibility_label.grid(row=0, column=3, padx=15, pady=10)

sunrise_label = tk.Label(second_row_frame, text="Sunrise: --", bg="#ffffff", font=font_small)
sunrise_label.grid(row=1, column=0, padx=15, pady=10)

sunset_label = tk.Label(second_row_frame, text="Sunset: --", bg="#ffffff", font=font_small)
sunset_label.grid(row=1, column=1, padx=15, pady=10)


get_weather()

root.mainloop()
