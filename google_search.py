from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, EdgeOptions, FirefoxOptions
import time
from random import *
from fake_useragent import UserAgent

class crawler():
    def __init__(self):
        self.ua = UserAgent()
        self.driver_use = ['chrome', 'edge', 'firefox']
    
    def setup_driver(self):
        driver_use = sample(self.driver_use, k=1)[0]
        if driver_use.lower() == 'edge':
            options = EdgeOptions()
            options.edge_executable_path = "msedgedriver.exe"
            self.options.accept_untrusted_certs = True
            self.options.add_argument('--user-agent={' + self.ua.edge + '}')
            self.driver = webdriver.Edge(options=self.options)
            self.driver.maximize_window()
        elif driver_use.lower() == 'firefox':
            self.options = FirefoxOptions()
            self.options.firefox_executable_path = "geckodriver.exe"
            self.options.accept_untrusted_certs = True
            self.options.add_argument('--user-agent={' + self.ua.firefox + '}')
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.maximize_window()
        else:
            self.options = ChromeOptions()
            self.options.chrome_executable_path = "chromedriver.exe"
            self.options.accept_untrusted_certs = True
            self.options.add_argument('--user-agent={' + self.ua.chrome + '}')
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.maximize_window()

    def crawl_google_search(self, query):
        self.driver.get('https://www.google.com/search?q={}&filter=0'.format(str(query.replace(' ', '+'))))
        time.sleep(uniform(1,3))
        elements = self.driver.find_elements(By.CLASS_NAME, 'yuRUbf')
        old_elements = len(elements)
        print(len(elements))
        
        while len(elements)<100 : 
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(uniform(1,3))
            elements = self.driver.find_elements(By.CLASS_NAME, 'yuRUbf') + \
                        self.driver.find_elements(By.CLASS_NAME, 'xe8e1b')
            new_elements = len(elements)
            print(old_elements, new_elements)
            if new_elements > old_elements:
                old_elements = new_elements
            else:
                try:
                    print('Click')
                    show_more_button = self.driver.find_element(By.XPATH, '//span[text()="更多結果"]')
                    time.sleep(uniform(1,3))
                    show_more_button.click() 
                except:
                    print('No more results')
                    return elements
        return elements

    def write_results(self, query):
        self.setup_driver()
        print('')
        print(query)
        elements = self.crawl_google_search(query=query)
        with open('crawl_text/{}.txt'.format(query.replace('\n', '')), 'w+', encoding='UTF-8') as f:
            counts = 1
            for element in elements:
                title = element.find_element(By.TAG_NAME, 'h3').text
                href = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                f.write(str(counts) + '\n')
                f.write(title + '\n')
                f.write(href + '\n')
                f.write('\n')
                counts += 1
                if counts >100: break
        self.driver.close()
    

# if __name__ == '__main__':
#     start = time.time()
#     query = 'foonyew'
#     write_results(query)
#     print('Search time : {:3.2f} seconds'.format(time.time() - start))