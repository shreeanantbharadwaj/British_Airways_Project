#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().system('pip install beautifulsoup4')



# In[42]:


import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape airline name and reviews
def scrape_airline_reviews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting airline name
    airline_name = soup.find('h1', itemprop='name').text.strip()
    
    # Extracting reviews
    reviews = soup.find_all('div', class_='text_content', itemprop='reviewBody')
    reviews_list = [review.get_text(strip=True) for review in reviews]
    
    return airline_name, reviews_list

# Function to save data to CSV
def save_to_csv(airline_name, reviews):
    filename = 'airline_reviews.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for review in reviews:
            writer.writerow([airline_name, review])

# Main function to scrape all airlines
def main():
    base_url = "https://www.airlinequality.com/review-pages/a-z-airline-reviews/"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in alphabet:
        url = f"{base_url}#{letter}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        airline_links = soup.find_all('div', class_='a_z_col_group')
        
        for link in airline_links:
            for item in link.find_all('a'):
                airline_url = "https://www.airlinequality.com" + item['href']
                airline_name, reviews = scrape_airline_reviews(airline_url)
                save_to_csv(airline_name, reviews)
                print(f"Reviews scraped and saved for '{airline_name}'")
                
                # Sleep for a short duration to avoid hitting the server too frequently
                time.sleep(2)

if __name__ == "__main__":
    main()

