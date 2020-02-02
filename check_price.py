#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep 
import re

path_chromedriver = os.getcwd()
path_chromedriver = path_chromedriver.replace('\\','/')

cache_data = ''
def open_web(path_web):
    #/media/pi/Luu Cong Dac
    # instantiate a chrome options object so you can set the size and headless preference
    options = Options()
    options.headless = True
    options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox') # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized') # 
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(path_chromedriver + '/chromedriver', chrome_options=options)
    driver.get(path_web)

    sleep(1)
    content_newfeed = driver.page_source
    cache_data = content_newfeed

    with open('data_base.txt', 'w') as f:
        f.write(str(content_newfeed.encode('utf-8')))
    #print ("Done") 
    #input('Press anything to quit') 
    driver.quit() 
    #print("Finished") 
    return(cache_data)
#///////////////////////////////////////////////////////////////////////////////////
def reg_ex_data(string_sample):
    regex = r"data-title=(\".*?\")\sdata-price=(\".*?\")"

    test_str = string_sample
    matches = re.finditer(regex, test_str, re.MULTILINE)
    result = ''
    count = 0
    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        result = ''
        count += 1
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
            result = result +'-'+ match.group(groupNum) + '---'
        result = result.replace('\"','')
        print(result)
# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
    print('Number of products: ',count)
    return()

#main functin
print('Tiki search \n')
try:
    while(True):
        reg_ex_data(open_web('https://tiki.vn/search?q=' + input('Type search content: ')))
    
    #reg_ex_data(open_web('https://tiki.vn/search?q=air%20blade'))
    #reg_ex_data(open_web('https://tiki.vn/search?q=apple'))
    #reg_ex_data(open_web('https://tiki.vn/deal-hot?tab=now&page=1'))
    #reg_ex_data(open_web('https://tiki.vn/deal-hot?tab=now&page=2'))
finally:
    print('Stop!')
