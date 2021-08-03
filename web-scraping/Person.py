import json
import time
from selenium import webdriver # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "first_year",
    password = "first_pass",
    database = "python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user")
usernames = mycursor.fetchall()

def decorator(func):
    def inner(username):
        available = True
        for x in usernames:
            if username == x[0]:
                available = False
        assert(not available), "Username does not exist"
        return func(username)
    return inner

class Person:
    def __init__(self, name, city = "Roorkee", work = None):
        self.name = name
        self.city = city
        if work != None:
            self.work = work
    
    def show(self):
        sentence = "My name is {} and my current city is {}"
        print(sentence.format(self.name, self.city))

@decorator
def scrap(username):
    try:
        mycursor.execute("CREATE TABLE user_scraped_details (username VARCHAR(255), name VARCHAR(255), city VARCHAR(255), work TEXT, favourites TEXT)")
    except:
        pass

    mycursor.execute("SELECT username FROM user_scraped_details")
    usernames = mycursor.fetchall()
    available = True
    for x in usernames:
        if username == x[0]:
            available = False
    
    if not available:
        mycursor.execute("SELECT * FROM user_scraped_details")
        data = mycursor.fetchall()[0]
        getName = data[1]
        getCity = data[2]
        getWork = data[3]
        global p
        if getCity != "" and getWork != []:
            p = Person(getName, getCity, getWork)
        elif getCity != "" and getWork == []:
            p = Person(getName, getCity)
        elif getCity == "" and getWork != []:
            p = Person(getName, getWork)
        elif getCity == "" and getWork == []:
            p = Person(getName)
        p.show()
        return

    NAME = ""
    CITY = ""
    WORK = []
    FAV = {}

    URL = "https://en-gb.facebook.com/"
    browser = webdriver.Chrome()
    browser.get(URL)
    email = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    try:
        submit = browser.find_element_by_id("loginbutton")
    except:
        submit = browser.find_element_by_name("login")
    email.send_keys("nrgiiwsbbgdndstxit@bptfp.net")
    password.send_keys("test_selenium")
    submit.click()
    time.sleep(1)

    browser.get("https://en-gb.facebook.com/"+username)
    time.sleep(1)

    SCROLL_PAUSE_TIME = 1

    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
          break
        last_height = new_height
    
    name = browser.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/h1')
    for ele in name:
        NAME = ele.text

    browser.get("https://en-gb.facebook.com/" + username +"/about_places")
    time.sleep(1)

    try:
        city = browser.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/a/span/span')
        for ele in city:
            CITY = ele.text
    except:
        pass

    browser.get("https://en-gb.facebook.com/" + username +"/about_work_and_education")
    time.sleep(1)

    try:
        workCont = browser.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]')
        rawWork = []
        for e in workCont:
            rawWork = e.text.split("\n")
        WORK = [rawWork[i] for i in range(len(rawWork)) if i % 2 != 0]

    except:
        pass

    browser.get("https://www.facebook.com/" + username + "/likes_all")
    time.sleep(1)


    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
          break
        last_height = new_height

    like_all = browser.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[3]')
    like_list = like_all[0].find_elements_by_xpath("./div")
    rawFav = []
    for e in like_list:
        rawFav.append(e.text)
    rawFav = list(filter(None, rawFav))

    for e1 in rawFav:
        itemList = []
        tl1 = e1.split("\n")
        for e2 in rawFav:
            tl2 = e2.split("\n")
            if tl1[-1] == tl2[-1]:
                itemList.append(tl2[0])
        FAV[tl1[-1]] = itemList

    if FAV != {}:
        print(FAV)
    else:
        print("There are no favourites")
    
    sql = "INSERT INTO user_scraped_details (username, name, city, work, favourites) VALUES (%s, %s, %s, %s, %s)"
    workStr = json.dumps(WORK)
    favStr = json.dumps(FAV)
    val = (username, NAME, CITY, workStr, favStr)

    mycursor.execute(sql, val)
    mydb.commit()

    global person
    if CITY != "" and WORK != []:
        person = Person(NAME, CITY, WORK)
    elif CITY != "" and WORK == []:
        person = Person(NAME, CITY)
    elif CITY == "" and WORK != []:
        person = Person(NAME, WORK)
    elif CITY == "" and WORK == []:
        person = Person(NAME)

