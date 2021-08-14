#!/usr/bin/env python
# coding: utf-8

# Import Dependencies
from bs4 import BeautifulSoup as soup
import datetime as dt
import pandas as pd
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

################################################################################
#
# BEGIN Function Definitions
#
################################################################################

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "hemispheres": mars_hemisphere_images(browser),
      "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


# ### Mars News

def mars_news(browser):
    # Scrape Mars News

    # Visit the Mars NASA News site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up HTML Parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Start Scraping
        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


# ### Featured Images

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


# ### Mars Facts

def mars_facts():

    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes='table table-striped')


# ### Mars Hemisphere Images

def mars_hemisphere_images(browser):

    # # Deliverable 1: Scrape High-Resolution Mars Hemisphere Images and Titles

    # ### Hemispheres

    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    link_names = []
    link_urls = []
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    links = browser.links.find_by_partial_text('Hemisphere')

    for link in links:
        
        # Add link to 'link_names' list:
        link_names.append(link.value)
        
        # Add Link URL to 'link_urls' list:
        link_urls.append(link['href'])

    for link in link_urls:
        browser.visit(link)
        time.sleep(1)
        
        # Find 'Sample' Image Link:
        img_link = browser.links.find_by_text('Sample')
        
        # Add Image Link to 'hemisphere_image_urls' list:
        hemisphere_image_urls.append(img_link['href'])


    # Combine Lists into Dictionary:

    ### NOTE TO CODE REVIEWER: ###
    # I had to Implement this Method
    # because browser.back() would generate
    # errors for me no matter what I tried.
    #
    # Instead, I chose to slurp up all the information & URLs
    # I needed into a collection of lists
    # and combine those lists into a Dictionary at the end
    # in the format specified in the challenge

    keys = ['img_url', 'title']
    list_of_tuples = zip(hemisphere_image_urls, link_names)
    hemisphere_image_urls = [dict(zip(keys, values)) for values in list_of_tuples]

    return hemisphere_image_urls

################################################################################
#
# END Function Definitions
#
################################################################################


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
