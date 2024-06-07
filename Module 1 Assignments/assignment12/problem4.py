'''
Task 2: Historical Weather Data Compiler

Problem Statement: Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily temperature data. 
Calculate the average temperature for each year and identify the year with the highest average.

'''

import os
import re

def read_weather_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_temperatures(data):
    # Find all temperature data points
    temperature_data = re.findall(r'(\d{4}-\d{2}-\d{2}),(\d+)°C', data)
    temperatures = [(date, int(temp)) for date, temp in temperature_data]
    return temperatures

def calculate_yearly_averages(temperatures):
    yearly_data = {}
    for date, temp in temperatures:
        year = date.split('-')[0]
        if year not in yearly_data:
            yearly_data[year] = []
        yearly_data[year].append(temp)

    yearly_averages = {year: sum(temps)/len(temps) for year, temps in yearly_data.items()}
    return yearly_averages

def analyze_blog_sentiments():
    # List of weather data files
    weather_files = ["/workspaces/coding-temple-python/assignment12/weather_2020.txt", "weather_2021.txt"]
    
    all_temperatures = []
    for file in weather_files:
        data = read_weather_data(file)
        if data:
            all_temperatures.extend(extract_temperatures(data))

    if all_temperatures:
        yearly_averages = calculate_yearly_averages(all_temperatures)
        highest_average_year = max(yearly_averages, key=yearly_averages.get)

        print("Yearly Average Temperatures:")
        for year, avg_temp in yearly_averages.items():
            print(f"{year}: {avg_temp:.2f}°C")
        
        print(f"The year with the highest average temperature is {highest_average_year} with an average of {yearly_averages[highest_average_year]:.2f}°C")



analyze_blog_sentiments()