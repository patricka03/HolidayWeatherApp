import sys
from http.client import responses

import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from requests import HTTPError, RequestException


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Holiday Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Arial;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
                padding: 10px;
                min-width: 300px;
            }
            QPushButton#get_weather_button{
                font-size: 40px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 75px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)


        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        from config import API_KEY
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weathers(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_errors("400 Bad Request:\nThe weather service couldn't understand your request. Please check the city name or parameters.")
                case 401:
                    self.display_errors("401 Unauthorized:\nAccess to the weather data requires valid credentials. Please verify your API key.")
                case 403:
                    self.display_errors("403 Forbidden:\nYou don’t have permission to access this weather resource. Your API access may be restricted.")
                case 404:
                    self.display_errors("404 Not Found:\nThe requested weather data could not be found. The location may not exist or be misspelled.")
                case 500:
                    self.display_errors("500 Internal Server Error:\nThe weather server encountered an issue. Try again later.")
                case 502:
                    self.display_errors("502 Bad Gateway:\nThe weather service received an invalid response. It might be temporarily down.")
                case 503:
                    self.display_errors("503 Service Unavailable:\nThe weather service is currently unavailable. Please try again in a few minutes.")
                case _:
                    self.display_errors(f"HTTP error occured\n", {http_error})

        except requests.exceptions.ConnectionError:
            self.display_errors("Connection Error: \nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_errors("Timeout Error: \nThe request has timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_errors("To many redirects: \nCheck the URL")
        except requests.RequestException as req_error:
            self.display_errors(f"Request Error: \n {req_error}")

    def display_errors(self, message):
        self.temperature_label.setStyleSheet("font-size: 10px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weathers(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temp_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temp_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "🌩"  # Thunderstorm
        elif 300 <= weather_id <= 321:
            return "🌦"  # Drizzle
        elif 500 <= weather_id <= 531:
            return "🌧"  # Rain
        elif 600 <= weather_id <= 622:
            return "❄️"  # Snow
        elif 701 <= weather_id <= 741:
            return "🌫"  # Fog/Mist
        elif weather_id == 762:
            return "🌋"  # Volcanic Ash
        elif weather_id == 771:
            return "🌬"  # Squalls
        elif weather_id == 781:
            return "🌪"  # Tornado
        elif weather_id == 800:
            return "🌞"  # Clear Sky
        elif 801 <= weather_id <= 804:
            return "🌥"  # Clouds
        else:
            return ""  # Unknown or unhandled condition

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())