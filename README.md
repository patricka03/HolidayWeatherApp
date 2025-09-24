# 🌞 Holiday Weather App

A simple yet stylish weather application built with Python and PyQt5, inspired by a hot and windy day in Santorini while sipping a cocktail on the beach. With no access to Codecademy at the time, this project was created using my existing Python knowledge—proof that creativity can strike anywhere.

The app fetches real-time weather data from the OpenWeatherMap API and displays it with emoji-powered icons, making weather checks both functional and fun.

---------------

## ✨ Features
Search weather by city name
Displays temperature in Celsius (°C)
Emoji icons for different weather conditions (☀️ 🌧 ❄️ 🌪 etc.)
Clear error handling for invalid inputs or API issues
Clean, centered UI with large, readable fonts

---------------

## 📸 Example
Enter a city name (e.g., Madrid)
Get the current temperature, weather description, and a matching emoji

---------------

## 🛠️ Installation & Setup

### 1. Clone the Repository
bash
git clone https://github.com/patricka03/HolidayWeatherApp.git
cd HolidayWeatherApp
### 2. Create a Virtual Environment (optional but recommended)
bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
### 3. Install Dependencies
bash
pip install -r requirements.txt
(If you don’t have a requirements.txt yet, you can create one with:)
bash
pip freeze > requirements.txt
### 4. Add Your API Key
Create a file called config.py in the project root:
python
API_KEY = "your_openweathermap_api_key_here"
Make sure config.py is in your .gitignore so it won’t be pushed to GitHub.
### 5. Run the App
bash
python weather_app.py

---------------

## 📦 Requirements
Python 3.8+
PyQt5
Requests

---------------

## 🚀 Future Improvements
Add autocomplete for city names
Support multiple units (°C / °F)
Display 5-day forecast

---------------

## 🌍 Inspiration
This project was born on holiday in Santorini—a reminder that coding inspiration can appear anywhere, even on a beach with a cocktail in hand.
