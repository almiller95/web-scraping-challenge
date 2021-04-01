# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd


def img_browser():
    # Note - Using FireFox "GeckoDriver driver not Chrome
    executable_path = {'executable_path': GeckoDriverManager().install()}
    return Browser('firefox', **executable_path, headless=False)

def scrape():
    #browser = init_browser()
    mars_dictionary = {}

    # step 1 part 1 - NASA Mars News
    # print('Part 1 - NASA Mars News')
    
    # adding dictionary to store part 1 data
    mars_first_article_dict = {}

    main_url = 'https://mars.nasa.gov/news'
    # Retrieve page with the requests module
    response_main = requests.get(main_url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_main = BeautifulSoup(response_main.text, 'html.parser')
    # finding all article titles
    art_title_results = soup_main.find_all('div',class_='content_title')
    # grabbing the title of the first article
    first_article_title = art_title_results[0].text.split('\n\n')[1]
    # print(f'First arictle title: "{first_article_title}"')
    # grabbing the text of the first article
    # finding all article sample text
    art_title_text_results = soup_main.find_all('div', class_ ="rollover_description_inner")
    # grabbing the sample of the first article
    first_article_title_text = art_title_text_results[0].text.split('\n')[1]
    # print(f'First arictle title text: "{first_article_title_text}"')
    
    # adding part 1 to dictionary
    mars_first_article_dict["title"] = first_article_title
    mars_first_article_dict["text"] = first_article_title_text

    # Step 1 Part 2 - JPL Mars Space Images - Featured Image
    # print('-------------------')
    # print('Part 2 - NASA Mars News')
    
    # adding dictionary to store part 2 data
    mars_image_dict = {}
    # pulling browser function
    browser = img_browser()
    # adding variables for browser
    main_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    main_image_url_trim = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    # opening up browser on main mars image url
    browser.visit(main_image_url)
    
    # splinter for loop to grab needed data
    for x in range(1, 3):
        html = browser.html
        soup_img = BeautifulSoup(html, 'html.parser')
        featured_image_url_splinter = soup_img.find_all('img','src',class_='headerimage fade-in')
    # grabbing just the img url out of the html
    featured_image_url_short = featured_image_url_splinter[0]["src"]
    # print(f'Image url short: {featured_image_url_short}')
    # creating the full string for the img url
    featured_image_url = f'{main_image_url_trim}{featured_image_url_short}'
    # print(f'Image url: {featured_image_url}')
    #browser.visit(main_url)
    
    # adding results to dictionary
    mars_image_dict["image_url"] = featured_image_url


    # Step 1 Part 3 - Mars Facts
    # print('-------------------')
    # print('Part 3 - Mars Facts')
    facts_url = 'https://space-facts.com/mars/'
    # reading data into python
    facts_index_short = ['ed','pd','mass','moon','od','op','st','fr','rb']
    facts_tables_1 = pd.read_html(facts_url)[0]
    facts_tables_1.columns = ["label","mars_table"]
    facts_tables_1['key'] = facts_index_short
    facts_df = facts_tables_1.set_index('key')
    facts_dict = facts_df.to_dict()
    # print(facts_tables_df)

    # Step 1 Part 4 - Mars Hemispheres
    # print('-------------------')
    # print('Part 4 - Mars Hemispheres')
    # astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls_dict = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]
    # print(hemisphere_image_urls_dict)

    # Step 1 Part 5 - Full scraped dictionary
    # print('-------------------')
    # print('Part 5 - Dictionary')   
    mars_dictionary["article"] = mars_first_article_dict
    mars_dictionary["mars_image"] = mars_image_dict
    mars_dictionary["mars_facts"] = facts_dict
    mars_dictionary["hemisphere_urls"] = hemisphere_image_urls_dict

    # Close the browser after scraping
    browser.quit

    # print(mars_dictionary)
    return mars_dictionary

# scrape()