from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
number = '+91**********'
def flipkart(number):
    driver.get('https://www.flipkart.com/account/login?signup=true')
    sleep(1)
    num_inp = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
    num_inp.send_keys(number)
    num_inp.send_keys(u'\ue007')
    try:
        sleep(1)
        req_otp = driver.find_element_by_xpath("//button[text()='Request OTP']")
        req_otp.click()
        print('working')
    except:
        print('nope')
    sleep(1)
    # driver.quit()

def snapdeal(number):
    driver.get('https://m.snapdeal.com/signin')
    num_inp = driver.find_element_by_xpath('//*[@id="react-login"]/div[2]/section/div/div/div[2]/input')
    num_inp.send_keys(number)
    nex = driver.find_element_by_xpath('//*[@id="react-login"]/div[2]/section/div/div/div[3]')
    nex.click()
    try:
        sleep(1)
        name = driver.find_element_by_xpath('//input[@placeholder="Name"]')
        name.send_keys('raja bhalwala')
        cont = driver.find_element_by_xpath('//*[@id="react-login"]/div/section/div/div/div/div[2]/div[4]')
        cont.click()
    except:
        print('nope snapdeal ')
    sleep(1)
    # driver.quit()


def sonyliv(number):
    driver.get('https://www.sonyliv.com/signin')
    num_inp = driver.find_element_by_id('userMobileEmail')
    num_inp.send_keys(number)
    sleep(1)
    noti = driver.find_element_by_xpath('//*[@id="wzrk-cancel"]')
    noti.click()
    net = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/form/div[2]/div[2]/div[1]/button')
    net.click()
    sleep(1)
    otp = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/form/p[2]/button')
    otp.click()
    sleep(1)
    # driver.quit()

def tinder(number):
    driver.get('https://tinder.com')
    sleep(1)
    try:
        signup_bts = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[4]/div[1]/button/span')
        signup_bts.click()
    except:
        pass
    sleep(1)
    try:
        phone_but = driver.find_element_by_xpath("//span[text()='Log in with phone number']")
        phone_but.click()
    except:
        print('not working tinder')
    sleep(1)
    input_num = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
    input_num.send_keys(number)
    sleep(1)
    button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button/span')
    button.click()
    sleep(3)    
    # driver.quit()


def goibibo(number):
    driver.get('https://www.goibibo.com/accounts/login/?next=/myaccount/gocash/')
    num_inp = driver.find_element_by_xpath('//*[@id="authMobile"]')
    num_inp.send_keys(number)
    cont_bts = driver.find_element_by_xpath('//*[@id="mobileSubmitBtn"]')
    cont_bts.click()
    sleep(1)
    # driver.quit()

def hotstar(number):
    driver.get('https://www.hotstar.com/in/subscribe/sign-in')
    num_inp = driver.find_element_by_xpath('//*[@id="phoneNo"]')
    num_inp.send_keys('8200024330')
    sub = driver.find_element_by_class_name('submit-button')
    sub.click()
    sleep(1)
    # driver.quit()



def lenskart(number):
    driver.get('https://www.lenskart.com/customer/account/login')
    sleep(1)
    num_inp = driver.find_element_by_name('emailOrPhone')
    num_inp.send_keys(number)
    sub = driver.find_element_by_name('send')
    sub.click()
    sleep(1)
    # driver.quit()


def medlife(number):
    driver.get('https://www.medlife.com/verifyMobile/false')
    sleep(1)
    num_in = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div/div/div[1]/form/div[2]/div/div/input')
    num_in.send_keys(number)
    sleep(1)
    otp_bts = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div/div/div[1]/form/div[4]/button')
    otp_bts.click()
    sleep(2)
    # driver.quit()


