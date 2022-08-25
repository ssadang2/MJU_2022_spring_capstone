from turtle import st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import time
import csv
import os
import urllib.request

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
s = Service(f'./{chrome_ver}/chromedriver.exe')

try:
    driver = webdriver.Chrome(service=s, options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(service=s, options=option)

driver.get("https://www.fragrantica.com/country/Russia.html")
driver.implicitly_wait(10)
driver.maximize_window()

f = open(r"C:\Users\WIN10\MJU_Study\capstone\rus_data_5.csv", 'w', encoding='UTF-8', newline='') 
csvWriter = csv.writer(f)                                                                           
cnt = 3 #시작 idx 3                                                                             
brand_num = 148 #시작 idx 2
brand = ""
while brand_num <= 879: #등록된 프랑스 향수 브랜드가 872개
    try:
        brand = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-8.large-9.cell > div.grid-x.grid-margin-x.grid-margin-y > div:nth-child({}) > a".format(brand_num)).text
        elem = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-8.large-9.cell > div.grid-x.grid-margin-x.grid-margin-y > div:nth-child({}) > a".format(brand_num))
        driver.execute_script("arguments[0].click();", elem)
        time.sleep(10)
    except:
        brand_num += 1
        continue
    while True:
        try:
            try:
                perfume_name = driver.find_element_by_css_selector("#brands > div:nth-child({}) > div:nth-child(1) > div.flex-child-auto > h3 > a".format(cnt)).text
                time.sleep(3)
            except:
                try:
                    cnt += 1
                    perfume_name = driver.find_element_by_css_selector("#brands > div:nth-child({}) > div:nth-child(1) > div.flex-child-auto > h3 > a".format(cnt)).text
                    time.sleep(5)
                except:
                    driver.back()
                    time.sleep(3)
                    brand_num += 1
                    cnt = 3
                    break
            
            elem = driver.find_element_by_css_selector("#brands > div:nth-child({}) > div:nth-child(1) > div.flex-child-auto > h3 > a".format(cnt))
            driver.execute_script("arguments[0].click();", elem)
            time.sleep(2)

            rating = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div.small-12.medium-6.text-center > div > p.info-note > span:nth-child(1)").text
            rating = float(rating)
            time.sleep(5)

            voters_num = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div.small-12.medium-6.text-center > div > p.info-note > span:nth-child(3)").get_attribute("content")
            voters_num = int(voters_num)
            time.sleep(5)

            gender = driver.find_element_by_css_selector("#toptop > h1 > small").text
            time.sleep(2)
            if(len(gender) == 9): #여성용
                gender = "women"
            elif(len(gender) == 17): #공용
                gender = "both"
            else: #남성용
                gender = "men"

            main_accord1 = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1)").text
            time.sleep(2)
            main_accord2 = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2)").text
            time.sleep(3)
            main_accord3 = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3)").text
            time.sleep(2)

            main_accord1_ratio = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div").get_attribute("style")
            time.sleep(2)
            start = main_accord1_ratio.find("width") + 7
            end = main_accord1_ratio.find("%")
            main_accord1_ratio = float(main_accord1_ratio[start:end])

            main_accord2_ratio = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > div").get_attribute("style")
            time.sleep(5)
            start = main_accord2_ratio.find("width") + 7
            end = main_accord2_ratio.find("%")
            main_accord2_ratio = float(main_accord2_ratio[start:end])

            main_accord3_ratio = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div").get_attribute("style")
            time.sleep(2)
            start = main_accord3_ratio.find("width") + 7
            end = main_accord3_ratio.find("%")
            main_accord3_ratio = float(main_accord3_ratio[start:end])

            denominator = main_accord1_ratio + main_accord2_ratio + main_accord3_ratio

            main_accord1_ratio = round(main_accord1_ratio/denominator, 2)
            main_accord2_ratio = round(main_accord2_ratio/denominator, 2)
            main_accord3_ratio = round(main_accord3_ratio/denominator, 2)

            top_note = []
            middle_note = []
            base_note = []

            notes = driver.find_elements_by_css_selector("#pyramid > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(4) > div > div")
            for i in notes:
                top_note.append(i.text)
            time.sleep(2)

            if not top_note:
                raise Exception

            notes = driver.find_elements_by_css_selector("#pyramid > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(6) > div > div")
            for i in notes:
                middle_note.append(i.text)
     
            time.sleep(3)

            if not middle_note:
                raise Exception

            notes = driver.find_elements_by_css_selector("#pyramid > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(8) > div > div")
            for i in notes:
                base_note.append(i.text)
            time.sleep(2)

            if not base_note:
                raise Exception

            top_note = " ".join(top_note)
            middle_note = " ".join(middle_note)
            base_note = " ".join(base_note)

            launch_year = "NULL"
            description = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(5) > div > p:nth-child(1)").text
            time.sleep(4)
            start = description.find("launched in") + 12
            end = start + 4
            if(start != 11):
                launch_year = int(description[start:end])

            spring = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(2) > div.voting-small-chart-size > div > div").get_attribute("style")
            time.sleep(2)
            start = spring.find("width") + 7
            end = spring.find("%")
            spring = [float(spring[start:end]), "spring"]

            summer = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(3) > div.voting-small-chart-size > div > div").get_attribute("style")
            time.sleep(2)
            start = summer.find("width") + 7
            end = summer.find("%")
            summer = [float(summer[start:end]), "summer"]

            fall = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(4) > div.voting-small-chart-size > div > div").get_attribute("style")
            time.sleep(5)
            start = fall.find("width") + 7
            end = fall.find("%")
            fall = [float(fall[start:end]), "fall"]

            winter = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(1) > div.voting-small-chart-size > div > div").get_attribute("style")
            time.sleep(2)
            start = winter.find("width") + 7
            end = winter.find("%")
            winter = [float(winter[start:end]), "winter"]

            season = sorted([spring, summer, fall, winter])[3][1]

            day = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(5) > div.voting-small-chart-size > div > div").get_attribute("style")
            time.sleep(3)
            start = day.find("width") + 7
            end = day.find("%")
            day = [float(day[start:end]), "day"]

            night = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(6) > div.voting-small-chart-size > div > div").get_attribute("style")
            time.sleep(2)
            start = night.find("width") + 7
            end = night.find("%")
            night = [float(night[start:end]), "night"]

            day_or_night = sorted([day, night])[1][1]

            longevity = []
            sillage = []

            elem = driver.find_elements_by_class_name("vote-button-legend")
            for i in range(11, len(elem)):
                if(i >= 11 and i <= 15):
                    longevity.append(int(elem[i].text))
                elif(i >= 16 and i <= 19):
                    sillage.append(int(elem[i].text))

            very_weak = [longevity[0], "very_weak"]

            weak = [longevity[1], "weak"]

            moderate = [longevity[2], "moderate"]

            long_lasting = [longevity[3], "long_lasting"]

            eternal = [longevity[4], "eternal"]

            longevity = sorted([very_weak, weak, moderate, long_lasting, eternal])[4][1]

            intimate = [sillage[0], "intimate"]

            moderate = [sillage[1], "medium"]

            strong = [sillage[2], "strong"]

            enormous = [sillage[3], "enormous"]

            sillage = sorted([intimate, moderate, strong, enormous])[3][1]

            print("=====", perfume_name, brand, gender, launch_year, main_accord1, main_accord2, main_accord3, top_note, middle_note, base_note, season, day_or_night, longevity, sillage, rating, voters_num, main_accord1_ratio, main_accord2_ratio, main_accord3_ratio, "=====")
            csvWriter.writerow([perfume_name, brand, gender, launch_year, main_accord1, main_accord2, main_accord3, top_note, middle_note, base_note, season, day_or_night, longevity, sillage, rating, voters_num, main_accord1_ratio, main_accord2_ratio, main_accord3_ratio])

            image = driver.find_element_by_css_selector("#main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > div > img").get_attribute("src")
            img_folder = './russia_perfume_img'
 
            if not os.path.isdir(img_folder): #이미지 저장
                os.mkdir(img_folder)
            urllib.request.urlretrieve(image, "./russia_perfume_img/{}.jpg".format(perfume_name))

            cnt += 1
            driver.back()
            time.sleep(7)
        except:
            try:
                driver.back()
                time.sleep(5)
                cnt += 1
                try:
                    driver.find_element_by_css_selector("#brands > div:nth-child({}) > div:nth-child(1) > div.flex-child-auto > h3 > a".format(cnt)).text
                    time.sleep(10)
                except:
                    cnt += 1
                    driver.find_element_by_css_selector("#brands > div:nth-child({}) > div:nth-child(1) > div.flex-child-auto > h3 > a".format(cnt)).text
                    time.sleep(3)
            except:
                driver.back()
                time.sleep(4)
                brand_num += 1
                cnt = 3
                break
            continue
f.close()