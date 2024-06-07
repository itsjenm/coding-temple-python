'''
Python Loops and Tuples in Analytical Applications

Objective:
This assignment is designed to strengthen your expertise in using Python loops and tuples, particularly in data analysis and processing scenarios. 
By completing these tasks, you will gain practical experience in handling and analyzing data using these fundamental Python concepts.

'''

# Task 1: Stock Market Data Analysis
# Enhance your skills in data manipulation and analysis using tuples and loops.

# You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date, and the closing price. 
# Your task is to analyze this data to find the average closing price of a specified stock over a given period.

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def avg_closing_price(stock_data, stock_symbol):
    """
    Calculate the average closing price of the specified stock over the given period.
    """

    total_price = 0
    count = 0
    
    for data in stock_data:
        symbol, date, price = data
        if symbol == stock_symbol:
            total_price += price
            count += 1
    
    if count == 0:
        return None  # If no data is found for the given stock symbol
    
    average_price = total_price / count
    if average_price is not None:
        print(f"The average closing price for {stock_symbol} is {average_price:.2f}")
    else:
        print(f"No data found for stock symbol {stock_symbol}")


stock_symbol = "AAPL"
average_price = avg_closing_price(stock_data, stock_symbol)
