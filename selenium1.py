from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.edge_executable_path = "msedgedriver.exe"

driver = webdriver.Edge(options=options)
driver.get('https://www.ptt.cc/bbs/Baseball/index.html')
driver.maximize_window()
# driver.save_screenshot('nchu.png')
driver.close()