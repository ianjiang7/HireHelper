import pandas as pd
import time
import os
from selenium import webdriver # for interacting with website
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import sort_txt

df = pd.read_csv('cleaned_linkedin_links.csv')
names = []

def open_url_in_chrome(url):
    print('Opening ' + url)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return driver

def get_full_name(driver):
    full_name = driver.find_element(By.XPATH,"//*[@id='main-content']/section[1]/div/section/section[1]/div/div[2]/div[1]/button/h1")
    name = full_name.text
    return name

def dismiss_offer(driver):
    driver.find_element(By.XPATH,"//*[@id='base-contextual-sign-in-modal']/div/section/button").click()
    time.sleep(10)
    return "Offer Dismissed"


link_list = sort_txt.df_links["Links"].to_list()

for link in link_list:

    driver_temp = open_url_in_chrome("https://linkedin.com" + link)
    dismiss_offer(driver_temp)
    real_name = get_full_name(driver_temp)
    print(real_name)
    names.append(real_name)

df["Names"] = names

