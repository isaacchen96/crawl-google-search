from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.edge_executable_path = "msedgedriver.exe"

driver = webdriver.Edge(options=options)
# driver.maximize_window()
driver.get('https://www.ptt.cc/bbs/Baseball/index.html')
try:
    elements = driver.find_elements(By.CLASS_NAME, 'title')
    print(len(elements))
    print(type(elements))
    a = elements.find_element(By.TAG_NAME, 'a')
    href = a.get_attribute('href')
    print(a.text)
    print(href)
except:
    print('None')


# pages = 5
# for p in range(pages):
#     print(p)
#     elements = driver.find_elements(By.CLASS_NAME, 'title')
#     for e in elements:
#         print(e.text)
#         if '刪除' not in e.text:
#             a = e.find_element(By.TAG_NAME, 'a')
#             href = a.get_attribute('href') if a else None
#             print(href)
            
#         else:
#             print('None')
#         print('')
#     nextpage = driver.find_element(By.LINK_TEXT, '‹ 上頁')
#     nextpage.click()
