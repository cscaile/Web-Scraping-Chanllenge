from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import requests



def mars_news():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    # results = soup.find_all('div', class_='slide')
    news_title = result.find('div', class_='content_title').text
    news_p = result.find('div', class_='rollover_description_inner').text
    print(news_title)
    print(news_p)
    mars_news["new_title"]=news_title
    mars_news["news_p"]=news_p
    broswer.quit()

    return mars_news


def featured_image():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)  
    # URL of page to be scraped
    url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url1)
    # Retrieve page with the requests module
    response = requests.get(url1)
    relative_image_path = soup.find_all('img')[3]["src"]
    jpl_img = url1 + relative_image_path

    return jpl_img

def mars_facts():
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)  
    # URL of page to be scraped
    url2 = 'https://space-facts.com/mars/'
    browser.visit(url2)    
    tables = pd.read_html(url2)
    df = tables[0]
    df.columns = ['Description','Mars']
    df.to_html(table_id="html_tbl_css", justify='center', index=False)
    data=df.to_dict(orient='records')
    df

    mars_df=df.to_html(classes='table table-striped')

    print(mars_df)

    return mars_facts

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
]
def scrape_all()
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False) 
    mars_info_dict= {
        "latest_headline":news_title,
        "latest_paragraph":news_p,
        "jpl_img":jpl_img,
        "mars_facts": mars_facts,
        "hemi_img": hemisphere_image_urls
    }
    return mars_info_dict