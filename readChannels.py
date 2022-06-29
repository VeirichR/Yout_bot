from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from datetime import datetime


class channelReader:
    def __init__(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.pages = ['https://www.youtube.com/channel/UCZTgQpHlnWvrSNpHBDCP3mg/videos',
                      'https://www.youtube.com/channel/UCSPueZnmf5kfA0vVrXBv4Xg/videos']
        self.videos = []

    def get_videos(self):
        for page in self.pages:
            self.open_url(page)
            sleep(1)
            urls = self.get_video_urls()
            self.videos.extend(urls)
        self.browser.close()
        # print(f'Teste {self.videos}')
        # print(f'Tamanho = {len(self.videos)}')
        return self.videos

    def open_url(self, page):
        try:
            self.browser.get(page)
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao entrar na URL passada!
                {error}\n{"-"*50}''')

    def close_browser(self):
        '''
        Fecha o browser
        '''
        try:
            self.browser.close()
        except Exception as error:
            print(f'{"-"*50}\nFail to close the browser!\n\n{error}\n{"-"*50}')

    def get_video_urls(self):
        try:
            videos = self.browser.find_elements(By.ID, 'thumbnail')
            urls = [video.get_attribute('href') for video in videos]
            urls.pop(0)
            print(f'{len(urls)} videos carregados com sucesso!')
            return urls
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao pegar URLS!{error}\n{"-"*50}''')

    def writeTxt(self, links):
        with open('links.txt', 'w') as arquivo:
            arquivo.writelines(f'{l}\n' for l in links)