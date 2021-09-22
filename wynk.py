import expressiontest as et
from selenium import webdriver
import time
import random
import cv2

def playSongs():
    #calling the function for fer
    listt = et.detect_expressions()
    frameClone = listt[1]
    cv2.imshow('your_face',frameClone)
    emotion = listt[0]
    print(emotion)
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised","neutral"]

    driver = webdriver.Chrome(executable_path = r'C:\Users\DELL\Desktop\Emotated Music\chromedriver_win32\chromedriver.exe')

    #web address of the webpage of wynk moods
    driver.get("https://wynk.in/music/package/moods/redesign_moods?page=0")

    #maximizing the window of the browser
    driver.maximize_window()
    time.sleep(2)
    moods = driver.find_elements_by_class_name('pkg-img-cont')
    #print(moods)

    if emotion == EMOTIONS[0]: #angry
        moods[9].click() #dance
    elif emotion == EMOTIONS[1]: #disgust
        moods[0].click() #relaxed
    elif emotion == EMOTIONS[2]: #scared
        moods[6].click() #devotion
    elif emotion == EMOTIONS[3]: #happy
        moods[3].click() #romantic
    elif emotion == EMOTIONS[4]: #sad
        moods[8].click() #inspiration
    elif emotion == EMOTIONS[5]: #surprised
        moods[2].click() #sufi
    else: #neutral
        moods[1].click() #feel good

    time.sleep(4)
    playlist = driver.find_elements_by_class_name('pkg-img-cont')
    num = len(playlist)
    playlist[random.randint(0,num-1)].click()

    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="middle_cont"]/app-playlist/div[1]/div[1]/div[2]/div[2]/button[1]').click()
    #time.sleep(4)
    #driver.manage().window().setPosition((-2000, 0))
    #driver.minimize_window()
    #print(play)
    #play.click()
#playSongs()
