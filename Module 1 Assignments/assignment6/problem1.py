'''
Product Review Analysis

Objective:
The aim of this assignment is to extract insights from product reviews by using string manipulation 
to categorize and summarize customer feedback for a SaaS product.

'''

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.

python_reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "Poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]


def search_reviews(review_list):
    keyword_list = ['good', 'excellent', 'bad', 'poor', 'average']
    for review in review_list:
        highlighted_review = review
        for keyword in keyword_list:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print(highlighted_review)


search_reviews(python_reviews)

# Task 2: Sentiment Tally 

# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

def tally_reviews(review_list):
    positive_tally = 0
    negative_tally = 0
    python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    for reviews in review_list:
        for positive_key in python_positive_words:
            if positive_key in reviews:
                positive_tally += 1
        for negative_key in negative_words:
            if negative_key in reviews:
                negative_tally += 1
    print(f"There are {positive_tally} positive words and {negative_tally} negative words")


tally_reviews(python_reviews)

# Task 3: Review Summary 

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

def review_summary(text):
    if len(text) <= 30:
        print(text)
    else:
        last_space_index = text.rfind(' ', 0, 30)
        if last_space_index == -1:
            # no space found
            print(text[:30] + '...')
        else:
            print(text[:last_space_index] + '...')
    

review_summary("This product is really good. I'm impressed with its quality.")

