import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

email = "YOUR TWITTER EMAIL HERE"
password = "YOUR TWITTER PASSWORD"

Edge_driver_path = r"C:\Users\nagav\EdgeDriver\edgedriver_win64\msedgedriver.exe"
service = Service(executable_path=Edge_driver_path)


# internet_speedtest_url = "https://www.speedtest.net/"
# twitter_url = "https://twitter.com/i/flow/login"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Edge(service=Service(executable_path=Edge_driver_path))
        self.down = 0
        self.up = 0

    def get_down_and_up_speed(self):
        internet_speedtest_url = "https://www.speedtest.net/"
        self.driver.get(internet_speedtest_url)
        sleep(5)
        get_speed = self.driver.find_element(By.CSS_SELECTOR,
                                             "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a")
        get_speed.click()
        sleep(45)

        download_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                  "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span")
        print(download_speed.text)
        self.down = download_speed.text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span")
        print(upload_speed.text)
        self.up = upload_speed.text
        return self.down, self.up

    def tweet_the_speed(self, up, down):
        twitter_url = "https://twitter.com/i/flow/login"
        self.driver.get(twitter_url)
        sleep(3)

        email_input = self.driver.find_element(By.TAG_NAME, value="input")
        print(email_input.text)
        sleep(1)

        email_input.send_keys(email)
        sleep(2)

        email_input.send_keys(Keys.ENTER)
        sleep(1)
        try:
            user_name_input = self.driver.find_element(By.NAME, "text")
            user_name_input.send_keys("YOUR TWITTER USER NAME")
            user_name_input.send_keys(Keys.ENTER)
            time.sleep(2)

            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            sleep(2)

        except NoSuchElementException:
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            sleep(2)

        tweet_input = self.driver.find_element(By.CSS_SELECTOR,
                                               "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span > span")
        tweet_input.send_keys(
            f"This is vikas,checking my current internet speed is download speed: {down}, upload speed: {up}")
        sleep(5)
        tweet_text = self.driver.find_element(By.CSS_SELECTOR,
                                              "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span")
        tweet_text.click()
        sleep(4)

        go_to_profile_to_delete_your_tweet = self.driver.find_element(By.CSS_SELECTOR,
                                                                      "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div.css-1dbjc4n.r-1habvwh > div.css-1dbjc4n.r-15zivkp.r-1bymd8e.r-13qz1uu > nav > a:nth-child(7)")
        go_to_profile_to_delete_your_tweet.click()
        sleep(2)
        select_options_menu = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div")
        select_options_menu.click()
        sleep(3)
        delete_from_select_options = self.driver.find_element(By.XPATH,
                                                              "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[1]")
        delete_from_select_options.click()
        sleep(3)
        delete_confirmation = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div")
        delete_confirmation.click()
        sleep(3)

        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot()
speeds = twitter_bot.get_down_and_up_speed()
down = float(speeds[0])
up = float(speeds[1])
twitter_bot.tweet_the_speed(up=up, down=down)
