import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





#pre requisites please make sure that you have selenium installed in the project location where you wish to run this
#pip install selenium
#make sure you also have chromedriver.exe in the same path as this code and chrome browser installed in your computer
#please dont ask me why imported all the above modules as i myself have no idea xd  i have just set  a standard for
#browser automation with selenium import all the above and you should be good to go
#the following lines below are instructions to the chrome driver to start browser in maximized form as you can see from the
#names respectively you can skip them if you want



options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")


#in the line below the browser is initialized as you can see the chromedriver.exe path means that chrome driver is in
#the same path as the code file itself moreover ignore the error you get when starting the script doesnt affect anything


browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')


#i will be using time.sleep command throughout the code to make sure that page has enough time to load properly
#you can remove or change them to make the process a little faster if you have relatively fast internet
#connection


browser.get('https://www.google.com.pk/search?ei=NjD8W5z6Ecz5kwWDubaQCg&q=live+price+usd+to+pkr&oq=live+price+usd+to+pkr&gs_l=psy-ab.3..0i22i30l2.4219.8371..8524...0.0..0.676.3689.4-3j4......0....1..gws-wiz.......0j0i71j0i67j0i131i67j0i131.A67hmIj6vnw')
time.sleep(2)
taki=browser.find_element_by_xpath('//*[@id="knowledge-currency__updatable-chart-column"]/div/div[1]/div/div[1]/div/div/div/div')
taki.click()

gg=browser.find_element_by_xpath('//*[@id="knowledge-currency__v2-header"]').text



#enter your username and password for facebook respectively below

browser.get('https://www.facebook.com')
time.sleep(2)
taki2=browser.find_element_by_id('email')
taki2.send_keys('Your Username here')
taki3=browser.find_element_by_id('pass')
taki3.send_keys('Your password here')
taki4=browser.find_element_by_xpath('//*[@id="loginbutton"]')
taki4.click()
time.sleep(3)

#in the statement below xhpc_message is the name of the text field in which u will post
#your status


taki5=browser.find_element_by_name('xhpc_message')
taki5.click()




#here gg refers to what you will be posting on your wall in this case
#the stock prices you can freely change it to a string to post on fb replacing it
#with 'your text' make sure you add single quotes
#i couldnt exactly find the id or xpath of the post button so i instead sent tab 4 times to move
#highlighted area to the post button then send space for pressing it




taki5.send_keys(gg,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.SPACE)

time.sleep(5)
quit()




