# importing the necessary libraries
import sys
import pandas as pd #For dataframe
from time import sleep #to sleep screen
from selenium import webdriver #for using selenium by webdriver
from selenium.webdriver.common.by import By #for using By commands ex:By.XPATH
from selenium.webdriver.common.keys import Keys #for sending keys


def googlescraper(search_key):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)


    #Getting the url
    url = "https://www.google.co.in/"
    driver.get(url)

    #sending the search key using send_keys
    search = driver.find_element(By.XPATH, '//input[@title="Search"]')
    search_stock = search.send_keys(search_key + " stock")
    search.send_keys(Keys.RETURN)

    #switching to the news section for scraping the news head
    news = driver.find_element(By.LINK_TEXT,"News").click()

    #switching to the tools section for getting the sort_by_date value
    tools = driver.find_element(By.ID,"hdtb-tls").click()
    sleep(1)
    #switching to the sort by date for gettinng the recent data
    sort_by_date = driver.find_element(By.XPATH,'//a[contains(text(), "Sorted by date")]').get_attribute("href")
    new_win = driver.execute_script("window.open('" + sort_by_date +"');")

    #switching to the new tab hence the link in opened in a new tab
    new_driver = driver.switch_to.window(driver.window_handles[1])


    #looping through the contents head for getting the title and storing it in a dataframe
    Data = []
    for p in range(2,4):
        try:
            page = driver.find_element(By.XPATH, f'//a[@aria-label="Page {p}"]').click()
            head = driver.find_elements(By.XPATH,'//div[@role="heading"]')
            sleep(2)
            for card in head:
                val = card.text
                content = {"content":val,
                           }
                Data.append(content)
        except:
            None


        df = pd.DataFrame(Data)
        df.to_csv("GoogleScrapy.csv",index=False)

if __name__ == "__main__":
    googlescraper(sys.argv[1])
