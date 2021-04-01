# web-scraping-challenge
Web Scraping Homework - Web Scraping Homework - Mission to Mars

Step 1 - Scraping
  - mission_to_mars.ipynb - jupyter notebook
    - Contains scraping steps and stored variables

    
Step 2 - MongoDB and Flask Applicationn
  - scrape_mars.py - python script
    - Returns defined scrape function, which scrapes needed data and stores as dictionary
  - app.py - python script & flask app
    - Defines '/scrape' path linked to the above scrape_mars.py function
      - '/scrape' results stored in mongodb
    - Defines '/' path to show the results and store "scrape" button
  - index.html - html to format and return the results.

