import time
from selenium import webdriver
import csv
list = []
browser = webdriver.Chrome('C:\\Users\\dell\\Desktop\\chromedriver.exe')
cate = ['travel vlogs','food vlogs','science and technology','manufacturing','history','art and music']
for k in cate:
    browser.get('https://www.youtube.com/results?search_query='+k+'&sp=EgIQAQ%253D%253D')
    no_of_pages = 5
    while no_of_pages:
        t = 6000
        browser.execute_script("window.scrollBy(0,{})".format(t),'')
        time.sleep(1)
        no_of_pages-=1
    hrefs = []
    elems = browser.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        a =  (elem.get_attribute("href"))
        c = 'https://www.youtube.com/watch'
        if c in a:
                hrefs.append(a)
    print(len(hrefs))
    import bs4
    import urllib.request as url
    list1 = []
    for j in hrefs:

        web = url.urlopen(j)
        id = j[32:]
        page = bs4.BeautifulSoup(web,'lxml')
        element2 = page.find_all('h1')[1]
        name = (element2.text.replace('\n',''))

        element3 = page.find_all('p')
        temp = (element3)
        for l in temp:
            if len(l)>15:
                d = l.text
                print(d)
        list1.append((id,name,d,k))

    with open("output_youtube.csv", "a",newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(list1)