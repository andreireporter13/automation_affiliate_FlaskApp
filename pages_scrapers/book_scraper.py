# aplicatia pagina13.ro - scraperul pentru pagina /reduceri-books;
#
# scraper nr. 2 - html template books.html
#
# Try make a scrapers with OOP;
#
#
from bs4 import BeautifulSoup
# 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from time import sleep
import csv
import pandas as pd
#
from fake_useragent import UserAgent
#
import re
#
#
# Make a scraper with OOP ----->
#
#
# Configure Driver with OOP;
#
class ConfigDriver:

    name = "config_driver"


    # set options;
    def configure_options(self):
        
        options = webdriver.FirefoxOptions()
        options.set_preference("general.useragent.override", UserAgent().random)
        options.add_argument("--disable-blink-features=AutomationControled")
        options.headless = False # if True, browser don't show;

        return options

    
    # get service;
    def get_firefox_service(self):

        firefox_service = Service(executable_path='put_your_path_here')

        return firefox_service


    # return valid driver;
    def get_driver(self):
        driver = webdriver.Firefox(service=self.get_firefox_service(), options=self.configure_options())

        return driver


# scraper class;
class ScraperBooks:

    
    name = '/reduceri-books(scraper)'


    def __init__(self, link: str):
        self.link = link


    def gather_data(self, driver):
        '''
        So, this method is drawn for colect data from libris.ro;
        '''
        driver.get(self.link)

        new_soup = BeautifulSoup(driver.page_source, 'lxml')
        product_list = new_soup.find('div', class_='cc-pg-categ-products-ct').find_all('li', class_='categ-prod-item')

        list_with_products = []
        for data in product_list:

            try:
                title = data.find('div', class_='pr-history-item').find('h2', class_='pr-title-categ-pg').get_text()
            except:
                title = ''
            
            try:
                link = data.find('div', class_='pr-history-item').find('div', class_='item-title').find('a').get('href')
            except:
                link = ''
            
            try:
                img = data.find('div', class_='pr-history-item').find('a').find('img').get('src')
                sleep(0.5)
            except:
                img = ''

            # ------------------------------> end of project;




    def convert_data_to_csv(self):
        pass

    
    def run(self):
        driver = ConfigDriver().get_driver()
        self.gather_data(driver)

        sleep(5)
        driver.quit()


if __name__ == "__main__":
    scraper = ScraperBooks("https://www.libris.ro/carti?fp=2022iuliehumanitas20") # link with sale from libris;
    scraper.run()
    
