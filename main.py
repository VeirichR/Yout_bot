from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from datetime import datetime

# testando o git
class Bot:
    def __init__(self, url):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.url = url

    def open_url(self):
        try:
            self.browser.get(self.url)
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao entrar na URL passada!
                {error}\n{"-"*50}''')

    def get_video_duration(self):
        try:
            duration = self.browser.find_element(
                By.CLASS_NAME, 'ytp-time-duration')
            return duration.text
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting video duration!
                {error}\n{"-"*50}''')

    def get_time_watched(self):
        try:
            time_watched = self.browser.find_element(
                By.CLASS_NAME, 'ytp-time-current')
            return time_watched.text
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting current video time!
                {error}\n{"-"*50}''')

    def play_video(self):
        try:
            play_btn = self.browser.find_element(
                By.CSS_SELECTOR, '.ytp-play-button')
            play_btn.click()
        except Exception as error:
            print(
                f'{"-"*50}\nFail to play! \n\n{error}\n{"-"*50}')

    def speed_up(self):
        try:
            teste = self.browser.find_element(
                By.CSS_SELECTOR, '.ytp-settings-button')
            teste.click()
            teste.send_keys('m')
            for i in range(4):
                teste.send_keys(Keys.SHIFT + '.')
        except Exception as error:
            print(f'{"-"*50}\nFail to speed up! \n\n{error}\n{"-"*50}')

    def close_browser(self):
        try:
            self.browser.close()
        except Exception as error:
            print(f'{"-"*50}\nFail to close the browser!\n\n{error}\n{"-"*50}')


url = ['https://www.youtube.com/watch?v=ELUyXkFAshw&ab_channel=Tips%26Reviews',
       'https://www.youtube.com/watch?v=yYpVPFU2j7c&ab_channel=Tips%26Reviews',
       'https://www.youtube.com/watch?v=6m7cAQgxtJA&ab_channel=Tips%26Reviews',
       'https://www.youtube.com/watch?v=rIlHQ7iCZJs&ab_channel=Tips%26Reviews'
       ]

for i in range(10):
    for video in url:
        yout_bot = Bot(video)
        yout_bot.open_url()
        total_dur = yout_bot.get_video_duration()
        yout_bot.speed_up()
        sleep(2)
        test = yout_bot.get_time_watched()
        if test == '0:00':
            yout_bot.play_video()
            print('Foi no teste')
        watched = 0
        print(f'Watching! {datetime.now():%d-%m-%y %H:%M:%S}')
        while total_dur != watched:
            sleep(1)
            watched = yout_bot.get_time_watched()

        print(f'View {i+1} completa!')
        yout_bot.close_browser()
