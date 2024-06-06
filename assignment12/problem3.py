'''
Advanced Python Data Processing and Analysis Challenge

Task 1: Travel Blog Sentiment Analysis:

Problem Statement: Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. 
Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").

Expected Outcome: 
A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.

'''

import re

# Define positive and negative words
positive_words = ["amazing", "enjoy", "beautiful", "great", "wonderful", "fantastic", "excellent"]
negative_words = ["bad", "disappointing", "poor", "terrible", "awful", "horrible", "unpleasant"]

def load_blog_entries(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().lower()  # Read the file and convert to lower case
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_sentiment_words(text, word_list):
    count = 0
    for word in word_list:
        count += len(re.findall(r'\b' + re.escape(word) + r'\b', text))
    return count

def main():
    file_path = "/workspaces/coding-temple-python/assignment12/travel_blogs.txt"  # Path to the travel blog entries file
    text = load_blog_entries(file_path)
    
    if text is not None:
        positive_count = count_sentiment_words(text, positive_words)
        negative_count = count_sentiment_words(text, negative_words)
        
        print("Sentiment Analysis Summary Report")
        print(f"Positive words count: {positive_count}")
        print(f"Negative words count: {negative_count}")


main()
