from selenium import webdriver
from time import sleep

def get_page(driver, url):
    try:
        driver.get(url)
    except:
        sleep(2)
        try:
            driver.get(url)
        except:
            sleep(2)
        driver.get(url)

    sleep(1)
    return driver



driver = webdriver.Firefox()
# https://www.sec.gov/edgar/browse/?CIK=50863&owner=exclude


url = 'https://www.sec.gov/edgar/browse/?CIK=50863&owner=exclude'
driver = get_page(driver, url)


filing_links = driver.find_elements_by_class_name('filing-link-all-files')

# filing_links[0].click()


