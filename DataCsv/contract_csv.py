import pandas as pd
import numpy as np
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# driver_path = 'C:\\Users\\coex0\\Desktop\\chromedriver_win32\\chromedriver.exe'
# options = webdriver.ChromeOptions()
# #options.add_experimental_option('excludeSwitches', ['enable-logging'])
# service = ChromeService(executable_path = driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# base_Url = "https://www.naver.com/"
# driver.get(base_Url)

# driver.execute_script("window.scrollTo(300, 400)")
# main_window = driver.current_window_handle
# main_window
# windows = driver.window_handles
# windows
# driver.switch_to.window(windows[0])
# driver.switch_to.window(main_window)

def pop_alert():
                    
    url = pd.read_csv('benign.csv', \
                    low_memory=False,\
                    names = ['url'], \
                    encoding = 'UTF-8')

    url2 = pd.read_csv('phish.csv', \
                    low_memory=False,\
                    names = ['url2'], \
                    encoding = 'UTF-8')
    while True:
        find = driver.current_url
        print(find)
        
        find_row = url.loc[(url['url'] == find)]
        
        if len(find_row) != 0:
            print("정상 사이트 url입니다")

        elif len(find_row) == 0:
            find_row2 = url2.loc[(url2['url2'] == find)]

            if len(find_row2) == 0:
                pop_alert()
                print("해당 url은 존재하지 않는 url입니다")
                

            elif len(find_row2) != 0:
                print("피싱 사이트 url입니다")

            time.sleep(3)

        time.sleep(4)

pop_alert(sys.argv[0])

# https://www.hunter.com/ 

# p = 'url 입력하세여'.split('/') 
# result = [p[0], p[1], p[2]]
# result = ' '.join(s for s in result)
# result = result.replace(' ', '/')
# print(result)  # 뒤에 잡다한 것 제거  

# sort(result)
