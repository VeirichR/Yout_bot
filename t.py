from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from datetime import datetime


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

    def get_video_urls(self):
        try:
            videos = self.browser.find_elements(
                By.ID, 'thumbnail')
            urls = [video.get_attribute('href') for video in videos]
            urls.pop(0)
            return urls
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao pegar URLS!
                {error}\n{"-"*50}''')


bot = Bot('https://www.youtube.com/channel/UCZTgQpHlnWvrSNpHBDCP3mg/videos')
bot.open_url()
urls = bot.get_video_urls()
print(urls)

'''with open('links2.txt', 'w', encoding="utf8") as arquivo:
    url = [linha.strip() for linha in arquivo]
    print(url)
    for linha in arquivo:
        print(linha, end=(''))'''
