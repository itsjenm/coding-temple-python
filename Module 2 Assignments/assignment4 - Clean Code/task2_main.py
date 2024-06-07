'''

Task 1: Identifying and Creating Classes


Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. 
Create classes that represent different aspects of the weather forecast application, such as 
fetching data, parsing data, and user interaction.

Problem Statement:

The existing script for the weather forecast application is written in a procedural style and lacks organization.

'''


# Weather Forecast Application Script

# def fetch_weather_data(city):
#     # Simulated function to fetch weather data for a given city
#     print(f"Fetching weather data for {city}...")
#     # Simulated data based on city
#     weather_data = {
#         "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
#         "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
#         "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
#     }
#     return weather_data.get(city, {})

# def parse_weather_data(data):
#     # Function to parse weather data
#     if not data:
#         return "Weather data not available"
#     city = data["city"]
#     temperature = data["temperature"]
#     condition = data["condition"]
#     humidity = data["humidity"]
#     return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# def get_detailed_forecast(city):
#     # Function to provide a detailed weather forecast for a city
#     data = fetch_weather_data(city)
#     return parse_weather_data(data)

# def display_weather(city):
#     # Function to display the basic weather forecast for a city
#     data = fetch_weather_data(city)
#     if not data:
#         print(f"Weather data not available for {city}")
#     else:
#         weather_report = parse_weather_data(data)
#         print(weather_report)

# def main():
#     while True:
#         city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#         if city.lower() == 'exit':
#             break
#         detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#         if detailed == 'yes':
#             forecast = get_detailed_forecast(city)
#         else:
#             forecast = display_weather(city)
#         print(forecast)

# if __name__ == "__main__":
#     main()


# Weather Forecast Application Script

class WeatherForecast:
    # Constructor
    def __init__(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
    
    # getter / setter methods
    def set_weather_data(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def display_weather(self):
        # General method to display product info
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}F")
        print(f"Condition: {self.condition}")
        print(f"Humidity: {self.humidity}%")

    

chi_weather = WeatherForecast("Chicago", "80", "cloudy", "40")
tampa_weather = WeatherForecast("Tampa", "88", "sunny", "80")
houston_weather = WeatherForecast("Houston", "76", "sunny", "20")
chi_weather.set_weather_data("Chicago", "64", "rainy", "60")
chi_weather.display_weather()
print()
houston_weather.display_weather()