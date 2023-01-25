import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

URL_TWITTER = "https://twitter.com/i/flow/login"
URL_SPEEDTEST = "https://www.speedtest.net/"
TWITTER_EMAIL = os.environ.get("twitter_email")
TWITTER_PASSWORD = os.environ.get("twitter_password")
TWITTER_USERNAME = os.environ.get("twitter_username")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class TwitterBotInternetSpeed:

    def __init__(self):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_Speed(self):
        self.driver.get(URL_SPEEDTEST)
        sleep(4)
        self.driver.find_element(By.CLASS_NAME, "onetrust-banner-options").click()
        sleep(3)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        sleep(50)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        print(self.up, self.down)

    def email_input(self):
        self.driver.get(URL_TWITTER)
        sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL)
        sleep(1)
        email.send_keys(Keys.ENTER)
        sleep(1)

    def password_input(self):
        type_password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        type_password.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
        login_button.click()
        time.sleep(2)

    def username_input(self):
        input_username = self.driver.find_element(By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")
        input_username.send_keys(TWITTER_USERNAME)
        input_next_button = self.driver.find_element(By.XPATH, "//div[@data-testid='ocfEnterTextNextButton']")
        input_next_button.click()

    def write_tweet(self):
        input = driver.find_element(By.CSS_SELECTOR, "br[data-text='true']")
        input.send_keys(f"My current speed is {bot.down} Download and {bot.up} Upload")
        sleep(3)
        tweet = driver.find_element(By.XPATH,
                                    "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet.click()
        time.sleep(3)
        print("Tweet done")


bot = TwitterBotInternetSpeed()

try:
    bot.get_internet_Speed()
    sleep(5)
    bot.email_input()
    sleep(3)
    bot.password_input()
    sleep(3)
    bot.write_tweet()
    sleep(5)

except NoSuchElementException:
    bot.username_input()
    sleep(3)

bot.password_input()
sleep(3)
bot.write_tweet()
sleep(5)

driver.quit()






driver.quit()





















