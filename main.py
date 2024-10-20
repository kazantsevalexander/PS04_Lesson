from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import random

def find_paragraphs():
    while True:
        sel = input('Выберите действие:\n1 - листать параграфы текущей статьи\n2 - перейти на одну из связанных страниц\n3 - выйти из программы\n')
        if sel == '1':
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input()

        if sel == '2':
            links = []
            body_content = browser.find_element(By.TAG_NAME, "p")
            for element in body_content.find_elements(By.TAG_NAME, "a"):
                link = element.get_attribute("href")
                links.append(link)
            browser.get(random.choice(links))

        if sel == '3':
            browser.quit()
            break

text_find = input('Введите поисковой запрос: ')

browser = webdriver.Firefox()
browser.get('https://www.wikipedia.org/')

assert 'Wikipedia' in browser.title
search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys(text_find)
search_box.send_keys(Keys.RETURN)

find_paragraphs()
