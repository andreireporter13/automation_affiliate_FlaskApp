# aplicatia pagina13.ro - scraperul pentru pagina /reduceri-beauty;
#
# scraper nr. 1, pagina /beauty
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

def configure_driver():

    options = webdriver.FirefoxOptions()

    # declare a UserAgent variable;
    user_agent = UserAgent()

    options.set_preference("general.useragent.override", user_agent.random) # set a random UserAgent;
    options.add_argument("--disable-blink-features=AutomationControled")
    options.headless = False # if True, driver don't show;

    # declare a firefox;
    firefox_service = Service(executable_path='put_your_path_here')

    # set a driver;
    driver = webdriver.Firefox(service=firefox_service, options=options)

    return driver


def gather_data(driver, link: str):

    driver.get(link)

    # get soup object;
    new_soup = BeautifulSoup(driver.page_source, 'lxml')
    product_list = new_soup.find('div', class_='gray_corner_first').find_all('div', class_='listaprod')

    # create a list with objects;
    list_with_products = []
    for item in product_list:

        try:
            link = item.find('a').get('href')
        except:
            link = ''

        try:
            title = item.find('a').get('title')
        except: 
            title = ''

        # get img
        try:
            img = str('https://www.esteto.ro') + str(item.find('img').get('src'))
        except: 
            img = ''
        
        # find price with regular expresion;
        try: 
            sale_price = item.find('p', text=re.compile('Pret\s*redus:\s*\d*\s*Lei')).get_text()
        except:
            sale_price = ''

        try:
            procent_sale = item.select('div:nth-child(1)', text=re.compile('>.{1,}<'))[0].get_text()
        except:
            procent_sale = ''

        
        esteto_ro = "your_affiliete_link"
        affiliat_link = esteto_ro + 'www.esteto.ro' + link


        # append data to list;
        list_with_products.append([title, sale_price, procent_sale, img, affiliat_link])

        # condition - colect only 20 links
        if len(list_with_products) > 19:
            break

    header = ['title', 'sale_price', 'procent_sale', 'img', 'affiliat_link']
    df = pd.DataFrame(list_with_products, columns = header)
    df.to_csv(f"csv_data_base/beauty_data.csv", encoding="utf8")
    print('Done!')   

    return



def main():

    driver = configure_driver()
    print(gather_data(driver, 'https://www.esteto.ro/produse-cosmetice'))

    sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
