from html.parser import HTMLParser
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

from fastapi import FastAPI, Request
import uvicorn

import pymongo
from pymongo import MongoClient

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to facebook scrapper"

PATH = "C:/Users/zribi/Desktop/FacebookScrap/chromedriver.exe"


options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()

options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#driver.get("https://www.facebook.com/LinkedIn/")
sleep(5)

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['posts']

@app.get("/scrap/")
async def scrap_posts(page: str, limit: int = 2, save: bool = False):
    driver.get("https://www.facebook.com/"+page+"/")
    for i in range(limit):
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(5)


    soup=BeautifulSoup(driver.page_source,"html.parser")   
    all_posts=soup.find_all("div",{"class":"x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"})
    for post in all_posts:
                    
        name=post.find("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"}).text
                    
        
        timepost=post.find("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"}).text
    
        content=post.find("div",{"dir":"auto"}).text
        print(name,"    " ,timepost,"   ", content)
        
        if save:
            dict={}
            dict["name"]=name
            dict["timepost"]=timepost
            dict["content"]=content
            client["posts"]["db"].insert_one(dict)
        

@app.get("/load/")
async def load_data(request: Request):
    params = {item[0]: item[1] for item in request.query_params.multi_items()}
    res = client["posts"]["db"].find(params, {'_id': 0})
    return [i for i in res]




