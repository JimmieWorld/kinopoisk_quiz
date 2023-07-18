import cv2 
import numpy as np
import time
import pytesseract
from PIL import ImageGrab as ig
import matplotlib.pyplot as plt
import pyautogui
import keyboard
import re
import pyclip

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
config = r'--oem 3 --psm 6'
flag = ''
qwest = ''
answer = []

def batton1():
    coords = [130, 650, 480, 730]
    img1 = np.array(ig.grab(bbox = coords))
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    stroka1 = pytesseract.image_to_string(img1, lang = 'rus', config=config)
    stroka1 = stroka1.replace("\n"," ")
    return stroka1

def batton2():
    coords = [480, 650, 830, 730]
    img1 = np.array(ig.grab(bbox = coords))
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    stroka1 = pytesseract.image_to_string(img1, lang = 'rus', config=config)
    stroka1 = stroka1.replace("\n"," ")
    return stroka1

def batton3():
    coords =[130, 730, 480, 810]
    img1 = np.array(ig.grab(bbox = coords))
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    stroka1 = pytesseract.image_to_string(img1, lang = 'rus', config=config)
    stroka1 = stroka1.replace("\n"," ")
    return stroka1

def batton4():
    coords = [480, 730, 830, 810]
    img1 = np.array(ig.grab(bbox = coords))
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    stroka1 = pytesseract.image_to_string(img1, lang = 'rus', config=config)
    stroka1 = stroka1.replace("\n"," ")
    return stroka1

def search_answer(str1, qwest, flag):
    if 'А воти нет!' in str1 or 'А вот и нет!' in str1 or 'Игра окончена' in str1:
        answer = str1.replace("\n","")
        answer = answer.partition('«')[2]
        answer = answer.rpartition('»')[0]
        answer = answer.replace(" ","")
        answer = re.sub("[.,'‘]", '', str(answer))
        answer = answer.lower()
        blok = f'{qwest}::{answer}'
#        print(blok)
        if blok != flag:  
            with open("cheats_opis.txt", "a", encoding='utf-8') as f:
                f.write(blok + '\n')
#            flag = blok
            pyautogui.moveTo(440, 635, duration=0.2)
            pyautogui.click()
        return blok
    else: 
        pyautogui.moveTo(305, 720, duration=0.2)
        pyautogui.click()
        time.sleep(0.7)

def find_answer(qwest):
    with open('cheats_opis.txt', 'r+', encoding='utf-8') as f:
        mass = []
        for line in f:
            answer = line[line.find('::')+2:-1]
            podstr = line[:line.find('::')]
            if (qwest in line) or (podstr == qwest):
                mass.append(answer)
        return mass
            
def vibor(file_answer):
    a1 = re.sub("[.,' ‘]", '', str(batton1().rstrip())).lower()
    a2 = re.sub("[.,' ‘]", '', str(batton2().rstrip())).lower()
    a3 = re.sub("[.,' ‘]", '', str(batton3().rstrip())).lower()
    a4 = re.sub("[.,' ‘]", '', str(batton4().rstrip())).lower()
    for answer in file_answer:
        if answer == a1:
            pyautogui.moveTo(305, 720, duration=0.2)
            pyautogui.click()
        elif answer == a2:
            pyautogui.moveTo(655, 720, duration=0.2)
            pyautogui.click()
        elif answer == a3:
            pyautogui.moveTo(305, 800, duration=0.2)
            pyautogui.click()
        elif answer == a4:
            pyautogui.moveTo(655, 800, duration=0.2)
            pyautogui.click()
        else: 
            print(file_answer, ':', a1, ':', a2, ':', a3, ':', a4, '/nЗдесь проблема!!! Запишешь САМ!!!')
            pyautogui.moveTo(440, 635, duration=0.2)
            pyautogui.click()
            
while True:
    img = np.array(ig.grab(bbox = (130, 230, 830, 630)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    stroka = pytesseract.image_to_string(img, lang = 'rus', config=config)
    
    if 'Авоти нет!' not in stroka and 'А вот и нет!' not in stroka and 'Игра окончена' not in stroka and 'А воти нет!' not in stroka and 'Время вышло!' not in stroka:
        pyautogui.moveTo(480, 620)
        pyautogui.rightClick()
        pyautogui.move(10, 90,)
        pyautogui.click()
        data = str(pyclip.paste())[2:-1]
    file_answer = find_answer(data)
    if file_answer != [] and data != '':
        vibor(file_answer)
    else: flag = search_answer(stroka, data, flag)

    if keyboard.is_pressed('a'):
        break
    time.sleep(1)
# https://avatars.mds.yandex.net/get-kinopoisk-image/1773646/51ce6166-a9fe-46af-825b-20831a832d23/orig