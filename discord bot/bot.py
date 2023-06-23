import requests
from bs4 import BeautifulSoup
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False  # typing 이벤트 비활성화
intents.presences = False  # presence 이벤트 비활성화
intents.message_content = True #v2

app = commands.Bot(command_prefix='/', intents=intents)

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)


#2. 멜론TOP100
@app.command()
async def 멜론탑100(ctx): 
    try:
        driver.implicitly_wait(5) #웹페이지가 로딩될때까지 5초 기다린다
        driver.maximize_window() #윈도우창 최대화 
        driver.get("https://www.melon.com/chart/") #웹페이지 해당 주소이동

        #멜론 TOP100 정보 div
        chart = driver.find_elements(By.CSS_SELECTOR, "#lst50")
        rank = 1

        for song in chart:
            title_element = song.find_element(By.CSS_SELECTOR, '.wrap_song_info .ellipsis.rank01 a')
            artist_element = song.find_element(By.CSS_SELECTOR, '.wrap_song_info .ellipsis.rank02 a')
            title = title_element.text
            artist = artist_element.text
            
            await ctx.send(f'[{rank}위] {title} - {artist}')
            rank += 1
    except Exception as e:
        print(e)
        await ctx.send('테스트 봇 오류 발생')


        
app.run('MTEyMTMxMDIxODcxNDg5NDMzNg.GJcleR.Yig2RVX7mQvnLHt6pfrGlyzPWGzSWJ4rHki7XQ')
