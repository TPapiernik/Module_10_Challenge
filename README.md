# Module 10 Challenge - Mission-to-Mars

## Overview

The purpose of this project is to create a Python-Flask web app to scrape and
display high-resolution images of the Hemispheres of Mars. Additionally, it
should be multi-device responsive.

### Deliverables
1. Scrape Full-Resolution Mars Hemisphere Images and Titles
2. Update the Web App with Mars Hemisphere Images and Titles
3. Add Bootstrap 3 Components

### Resources

- Software:
	- Bootstrap 3 Components loaded via HTML
	- Jupyter notebook server 6.3.0, running Python 3.7.10 64-bit (Dependencies: bs4[BeautifulSoup], pandas, splinter, webdriver_manager.chrome[ChromeDriverManager]) [Used for Development and Testing]
	- MongoDB Win32-x86_64 v4.2.15 64-bit
	- Python 3.7.10 64-bit used to run standalone Flask App within Anaconda v4.10.1 (Dependencies: bs4[BeautifulSoup], datetime, flask, flask_pymongo, pandas, splinter, webdriver_manager.chrome[ChromeDriverManager])
- Data:
	- `Mission_to_Mars_Challenge_starter_code.ipynb`, provided in Challenge. Incorporated into prior work `Mission_to_Mars.ipynb` created previously within Module 10, and saved as `Mission_to_Mars_Challenge.ipynb`
	- Web Resources Scraped from: https://redplanetscience.com/, https://spaceimages-mars.com, https://galaxyfacts-mars.com, and https://marshemispheres.com/

## Deliverables

### Deliverable 1

See `Mission_to_Mars_Challenge.ipynb`

### Deliverable 2

See `scraping.py` and `index.html`

### Deliverable 3

See `index.html`, `scraping.py`, and `mainpage.css`

Note: `df.to_html()` function was updated in `scraping.py` to output additional table class of `table table-striped` as defined by Bootstrap CSS. This default style was overridden in `mainpage.css` to include darker
background colors for the striped rows of the HTML Table. Additionally, `h1` was redefined to use the Google Font 'Audiowide' by default.
