# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser

def scrape_mars():
    # SCRAPE - PART 1
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news'
    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the sections containing titles
    results = soup.find_all('div', class_="content_title")
    # Find the sections containing paragraphs
    results2 = soup.find_all('div', class_="rollover_description_inner")
    # Identify and return title
    news_title = results[0].find('a').text
    # Identify and return price of listing

    # Identify and return title
    news_parag = results2[0].text
    # Identify and return price of listing

    # SCRAPE - PART 2
    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # Set up Browser.
    browser = Browser('chrome')
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Find the sections containing images
    results = soup.find_all('div', class_='image_and_description_container')
    # Find just the div containing the first image.
    image = results[0].find_all('div', class_="img")
    # Drill down to just the image.
    thumbs = image[0].find_all('img', class_="thumb") 
    # Retrieve the image partial url.
    partial_image_url = thumbs[0].get('src')
    # Concatenate with the base url to get the full url.
    featured_image_url = "https://www.jpl.nasa.gov" + partial_image_url

    # SCRAPE - PART 3
    # URL of page to be scraped
    url = 'https://space-facts.com/mars'
    # Use pandas to read the html tables. (Not sure how it knows to get the table specifically...)
    tables = pd.read_html(url)
    # Turn it from a list into a dataframe. (Not sure how this this simple code does this either.)
    df = tables[0]
    # Name dataframe columns.
    df.columns = ['Data Attribute', 'Value']
    # Turn from dataframe into an html.
    html_table = df.to_html()

    # SCRAPE - PART 4
    # URL of pages to be scraped
    url1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    url2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    url3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    # Set up Browser.
    browser1 = Browser('chrome')
    browser1.visit(url1)
    browser2 = Browser('chrome')
    browser2.visit(url2)
    browser3 = Browser('chrome')
    browser3.visit(url3)
    browser4 = Browser('chrome')
    browser4.visit(url4)
    # Set up html.
    html1 = browser1.html
    html2 = browser2.html
    html3 = browser3.html
    html4 = browser4.html
    soup1 = BeautifulSoup(html1, 'html.parser')
    soup2 = BeautifulSoup(html2, 'html.parser')
    soup3 = BeautifulSoup(html3, 'html.parser')
    soup4 = BeautifulSoup(html4, 'html.parser')
    # Drill down to img tags.
    image1 = soup1.find_all('img', class_='wide-image')
    image2 = soup2.find_all('img', class_='wide-image')
    image3 = soup3.find_all('img', class_='wide-image')
    image4 = soup4.find_all('img', class_='wide-image')
    # Drill down to the partial url's.
    partial_image_url1 = image1[0].get('src')
    partial_image_url2 = image2[0].get('src')
    partial_image_url3 = image3[0].get('src')
    partial_image_url4 = image4[0].get('src')
    # Concatenate with the base url to get the full url's.
    full_image_url1 = "https://astrogeology.usgs.gov" + partial_image_url1
    full_image_url2 = "https://astrogeology.usgs.gov" + partial_image_url2
    full_image_url3 = "https://astrogeology.usgs.gov" + partial_image_url3
    full_image_url4 = "https://astrogeology.usgs.gov" + partial_image_url4
    # Retrieve the titles.
    title1 = soup1.find('h2', class_='title').get_text()
    title2 = soup2.find('h2', class_='title').get_text()
    title3 = soup3.find('h2', class_='title').get_text()
    title4 = soup4.find('h2', class_='title').get_text()
    # Put the titles and corresponding url's into a dictionary.
    mars_dict = {
        "table": html_table , 
        "news_title": [news_title] ,
        "news_parag": [news_parag] ,
        "featured_image_url": [featured_image_url] , 
        "titles": [title1, title2, title3, title4] ,
        "links": [full_image_url1, full_image_url2, full_image_url3, full_image_url4]
        }
    return mars_dict
