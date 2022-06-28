from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from datetime import datetime

"""
Criar separado o scrapper para pegar os videos
Arrumar o bot para ler os videos separados.
Arrumar o output
"""


class Bot():
    def __init__(self):
        options = Options()
        options.headless = False
        self.browser = webdriver.Firefox(options=options)
        self.pages = ['https://www.youtube.com/channel/UCZTgQpHlnWvrSNpHBDCP3mg/videos',
          'https://www.youtube.com/channel/UCSPueZnmf5kfA0vVrXBv4Xg/videos']
        self.videos = []

    def open_url(self, url):
        try:
            self.browser.get(url)
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao entrar na URL passada!
                {error}\n{"-"*50}''')

    def get_video_urls(self):
        try:
            videos = self.browser.find_elements(By.ID, 'thumbnail')
            urls = [video.get_attribute('href') for video in videos]
            urls.pop(0)
            return urls
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao pegar URLS!{error}\n{"-"*50}''')

    def get_videos(self):
        for page in self.pages:
            self.open_url(page)
            sleep(1)
            urls = self.get_video_urls() # ver se da para retornar direto essa list
            for link in urls:  # rever esta parte, acho que esta redundante.
                self.videos.append(link)
        print(len(self.videos))
        # retornar a lista com as urls

    def get_video_duration(self):
        try:
            duration = self.browser.find_element(
                By.CLASS_NAME, 'ytp-time-duration')
            return duration.text
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting video duration!
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

    def get_time_watched(self):
        try:
            time_watched = self.browser.find_element(
                By.CLASS_NAME, 'ytp-time-current')
            return time_watched.text
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting current video time!
                {error}\n{"-"*50}''')

    def get_video_name(self):
        try:
            name = self.browser.find_element(
                By.CSS_SELECTOR, '#container > h1 > yt-formatted-string')
            print(name.text)
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting current video name!
                {error}\n{"-"*50}''')

    def close_browser(self):
        try:
            self.browser.close()
        except Exception as error:
            print(f'{"-"*50}\nFail to close the browser!\n\n{error}\n{"-"*50}')

# 24 e 18
#canais = ['https://www.youtube.com/channel/UCZTgQpHlnWvrSNpHBDCP3mg/videos',
#          'https://www.youtube.com/channel/UCSPueZnmf5kfA0vVrXBv4Xg/videos']
bot = Bot()
urls = bot.get_videos()
print(f"Foram encontrados {len(urls)} videos")
views = 10

for view in range(views):
    for video in urls:
        bot.open_url(video)
        print(video)
        sleep(3)
        bot.get_video_name()
        total_dur = bot.get_video_duration()
        bot.speed_up()
        sleep(2)
        test = bot.get_time_watched()
        if test == '0:00':
            bot.play_video()
            print('Forced play!')
        print('-'*40 + '->')
        print(f'Watching! {datetime.now():%d-%m-%y %H:%M:%S}')
        time_before = datetime.now()
        watched = 0
        while total_dur != watched:
            if watched == 0:
                sleep(1)
            watched = bot.get_time_watched()
            time_after = datetime.now() - time_before
            if time_after.seconds >= 480:
                print('Bug or ad too long, starting next video!')
                break

        print(f'View {view+1} completa!')
        print('-'*40 + '->')
        print()
        sleep(1)
        bot.close_browser()