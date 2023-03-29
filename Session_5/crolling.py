from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

# # 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = './chromedriver ' #chromedriver 경로
driver = webdriver.Chrome(chrome_driver, 
                          options= chrome_options
                          )

# 실행할 웹페이지 불러오기 (네이버 영화)
# driver.get('https://movie.naver.com/')

#과제1
# x_btn = driver.find_element(By.XPATH,'//*[@id="noti_popup"]/div[1]/button')
# x_btn.click()
# ranking_btn = driver.find_element(By.XPATH,'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
# ranking_btn.click()
# file = open('navermovie1.csv', mode="w", newline='', encoding="cp949")
# writer = csv.writer(file)
# writer.writerow(["top20 title"])
# for i in range(2,23):
#     if i != 12:
#         title1to20 = driver.find_element(By.XPATH,f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
#         print(title1to20)
#         writer.writerow([title1to20])
#     else:
#         pass
# file.close

#과제2 - try-except 사용했는데 이렇게 접근해도 되는건지 확인받아야함.
# x_btn = driver.find_element(By.XPATH,'//*[@id="noti_popup"]/div[1]/button')
# x_btn.click()
# ranking_btn = driver.find_element(By.XPATH,'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
# ranking_btn.click()
# file = open('navermovie2.csv', mode="w", newline='', encoding="cp949")
# writer = csv.writer(file)
# writer.writerow(['title','out-line','director','score'])
# for i in range(2,23):
#     #try-except block 이용해서, 요소 있으면 바로 텍스트 전환 없으면 동일 프로세스에서 하나 바꾼거
#     if i != 12:
#         try:
#             movie = driver.find_element(By.XPATH,f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
#             movie_t = movie.text
#             movie.click()
#             time.sleep(1)
#             outline = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text #a로 지명해야하는 경우 안돌아갈거임. 이때 방법 찾아야함.
#             time.sleep(2)
#             direc = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
#             time.sleep(2)
#             star = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
#             print(movie_t, outline, direc, star)
#             writer.writerow([movie_t, outline, direc, star])
#             ranking_btn = driver.find_element(By.XPATH,'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#             ranking_btn.click()
#         except:
#             star = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[4]/div[2]/div[2]/div[1]/div/div/em').text
#             print(movie-t, outline, direc, star)
#             writer.writerow([movie_t, outline, direc, star])
#             ranking_btn = driver.find_element(By.XPATH,'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
#             ranking_btn.click()
#     else:
#         pass

#과제3
# x_btn = driver.find_element(By.XPATH,'//*[@id="noti_popup"]/div[1]/button')
# x_btn.click()
# time.sleep(1)
# type_btn = driver.find_element(By.XPATH,'//*[@id="ipt_tx_srch"]')
# time.sleep(1)
# ActionChains(driver).send_keys_to_element(type_btn, '더 퍼스트 슬램덩크').perform()
# time.sleep(1)
# srch_btn = driver.find_element(By.XPATH,'//*[@id="jSearchArea"]/div/button')
# srch_btn.click()
# time.sleep(1)
# file = open('navermovie3.csv', mode="w", newline='', encoding="cp949")
# writer = csv.writer(file)
# writer.writerow(['title', 'director', 'score', 'number'])
# title = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li/dl/dt/a/strong').text
# time.sleep(1)
# direc = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li/dl/dd[3]/a').text
# time.sleep(1)
# score = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li/dl/dd[1]/em[1]').text
# time.sleep(1)
# num = driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li/dl/dd[1]/em[2]').text
# time.sleep(1)
# print(title,direc,score,num)
# writer.writerow([title, direc, score, num])
# file.close()

#과제4
#각각 함수로 만들고 결과값 받아서 csv로 변환 & csv encording 바꿔줘야함

#과제5
from bs4 import BeautifulSoup
import requests as req

#실행할 웹페이지 불러오기 (멜론)
driver.get("https://www.melon.com/index.htm")

popup_btn = driver.find_element(By.XPATH,'//*[@id="mainPop"]/div/div[2]/div[2]/button/span/span')
popup_btn.click()
type_btn2 = driver.find_element(By.XPATH,'//*[@id="top_search"]')
ActionChains(driver).send_keys_to_element(type_btn2,'빈지노').perform()
time.sleep(1)
srch_btn = driver.find_element(By.XPATH,'//*[@id="gnb"]/fieldset/button[2]/span')
srch_btn.click()
time.sleep(1)
html = driver.page_source


soup = BeautifulSoup(html,'html.parser')
li_songs = soup.select('div.ellipsis > a.fc_gray')
li_songs_clear = [e.text for e in li_songs ]
li_songs_10 = []
for i in range(0,10):
    li_songs_10.append(li_songs_clear[i])
print(li_songs_10)
