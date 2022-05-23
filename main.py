from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from datetime import datetime

# testando o github


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


'''['https://www.youtube.com/watch?v=ELUyXkFAshw&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=yYpVPFU2j7c&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=6m7cAQgxtJA&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=rIlHQ7iCZJs&ab_channel=Tips%26Reviews']

['https://www.youtube.com/watch?v=9ywHBxX2KA0&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=kGkq58BWhFs&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=yTtJhXLTGMw&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=WXthUZGSRyM&ab_channel=Tips%26Reviews']

['https://www.youtube.com/watch?v=obXGuYkAjNc&ab_channel=Dicas%26Reviews%C2%AE',
'https://www.youtube.com/watch?v=WKnzzRNe9Jg&ab_channel=Dicas%26Reviews%C2%AE',
'https://www.youtube.com/watch?v=khsZkciyghg&ab_channel=Dicas%26Reviews%C2%AE',]

['https://www.youtube.com/watch?v=8TOFWnJEDkI&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=3_OVKnw60U0&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=pFumZOMmWas&ab_channel=Tips%26Reviews',
'https://www.youtube.com/watch?v=245ONuV9KDw&ab_channel=Tips%26Reviews']'''

with open('links.txt', 'r', encoding="utf8") as arquivo:
    url = [linha.strip() for linha in arquivo]

views = 30
for view in range(views):
    for video in url:
        yout_bot = Bot(video)  # pensar uma forma de nao inicializar toda vez
        yout_bot.open_url()
        total_dur = yout_bot.get_video_duration()
        yout_bot.speed_up()
        sleep(2)
        test = yout_bot.get_time_watched()
        if test == '0:00':
            yout_bot.play_video()
            print('Forced played!')
        print(f'Watching! {datetime.now():%d-%m-%y %H:%M:%S}')
        time_before = datetime.now()

        watched = 0
        while total_dur != watched:
            if watched == 0:
                sleep(1)
            watched = yout_bot.get_time_watched()
            time_after = datetime.now() - time_before
            if time_after.seconds >= 480:
                print('Bug or ad too long, starting next video!')
                break

        print(f'View {views+1} completa!')
        yout_bot.close_browser()
