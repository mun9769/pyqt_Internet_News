import threading
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}



def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]' , '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
 
    return cleaned_text

threading_lst = []
flag = [False,False,False]

class JoongangOpinion(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = "https://news.joins.com/opinion?cloc=joongang-home-gnb1"
        self.my_res = requests.get(self.url)
        self.my_res.raise_for_status()
        self.my_soup = BeautifulSoup(self.my_res.text,"lxml")
        self.opinions = self.my_soup.find_all("h3",attrs={"class":"mg"})
        
    def run(self):
        for i in range(3,len(self.opinions)): #사설칼럼 0,1,2는 빼준거다
            res = requests.get("https://news.joins.com"+self.opinions[i].a["href"])
            res.raise_for_status()
            soup = BeautifulSoup(res.text,"lxml")

            #기사 제목
            title = soup.find("h1",attrs={"class":"headline mg"}).get_text()
            cleanedtitle = clean_text(title) # utf8이 특수문자를 인식못해서 특수문자는 빼준다.
            #soup에서 부제목이 있다면 sub_title 변수에 저장
            if soup.find("div",attrs={"class":"article_body"}).find("div",attrs={"class":"ab_subtitle"}):
                sub_title = soup.find("div",attrs={"class":"article_body"}).find("div",attrs={"class":"ab_subtitle"}).get_text()
                soup.find("div",attrs={"class":"article_body"}).find("div",attrs={"class":"ab_subtitle"}).decompose()
            #기사 본문
            body =soup.find("div",attrs={"class":"article_body"}).get_text() #strip 삭제
            body = body.replace("     ","\n")

            
            threading_lst.append(title + "\n"+body)

            

        flag[0] = 1
            # with open("joongang_{}.txt".format(cleanedtitle),"w",encoding="utf8") as f:
            #     f.write(title)
            #     f.write(sub_title)
            #     f.write(body)


class HanyoerehOpinion(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url="http://www.hani.co.kr/arti/opinion/column/home01.html"
        self.my_res = requests.get(self.url)
        self.my_res.raise_for_status()
        self.my_soup = BeautifulSoup(self.my_res.text,"lxml")
        self.p= re.compile("^"+datetime.today().strftime("%Y-%m"))
        self.opinions_dates = self.my_soup.find_all("span",attrs={"class":"date"})


    def run(self):
        for i in range(len(self.opinions_dates)):
            m = self.p.match(self.opinions_dates[i].get_text())
            if m:  ###################### 밤12시 지나면 현재날짜와 칼럼날짜가 달라
                link = self.opinions_dates[i].parent.parent.a["href"]
                res = requests.get("http://hani.co.kr"+link)
                res.raise_for_status()
                soup = BeautifulSoup(res.text,"lxml")

                if soup.find("div",attrs={"class":"image-area"}):
                    soup.find("div",attrs={"class":"image-area"}).decompose()
                
                if soup.find("div",attrs={"class":"image-area"}):
                    soup.find("div",attrs={"class":"image-area"}).decompose()
                
                #기사 제목
                title = soup.find("span",attrs={"class":"title"}).get_text()
                cleanedtitle = clean_text(title)
                #기사 본문
                body = soup.find("div",attrs={"class":"text"}).get_text().strip()

                threading_lst.append(title + "\n"+body)
                
                # if soup.find("div",attrs={"class":"article_body"}).find("div",attrs={"class":"ab_subtitle"}):
                #     sub_title = soup.find("div",attrs={"class":"article_body"}).find("div",attrs={"class":"ab_subtitle"}).get_text()
                #     soup.find("div",attrs={"class":"article_body"}).find("div",attrs={"class":"ab_subtitle"}).decompose()

                
                # 한겨레는 subtitle이 없다
                
        flag[1] = 1

                
                # with open("han_{}.txt".format(cleanedtitle),"w",encoding="utf8") as f:
                #     f.write(title)
                #     # 한겨레는 subtitle이 없다
                #     f.write(body)
            
#애는 날짜가 메인에 없네 확인해주자
class KoreaEconomicOpinion(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = "https://www.hankyung.com/opinion"
        self.my_res = requests.get(self.url, headers=headers)
        self.my_res.raise_for_status()
        self.my_soup = BeautifulSoup(self.my_res.text,"lxml")
        self.opinions = self.my_soup.find_all("h3",attrs={"class":"tit"})
        
    def run(self):
        for i in range(3,len(self.opinions)): # 0,1,2는 사설칼럼이다.
    
            res = requests.get(self.opinions[i].a["href"])
            res.raise_for_status()
            soup = BeautifulSoup(res.text,"lxml")
            
            if soup.find("div",attrs={"class":"thumb_article al_r"}):
                soup.find("div",attrs={"class":"thumb_article al_r"}).decompose()
                
            
            title = soup.find("h1",attrs={"class":"title"}).get_text().strip()
            cleanedtitle = clean_text(title)
            body = soup.find("div",attrs={"id":"articletxt"}).get_text().lstrip()
            
            threading_lst.append(title + "\n"+body)
            
        flag[2] = 1
            
            # with open("Keconomic {}.txt".format(cleanedtitle),"w",encoding="utf8") as f:
            #     f.write(title)
            #     # subtitle 있는데 안해줄래
            #     f.write(body)

dir_path = "C:/Users/문희찬/Desktop/scraping"
if not(os.path.isdir(dir_path+"/"+datetime.today().strftime("%Y-%m-%d"))):
    os.mkdir(dir_path+"/"+datetime.today().strftime("%Y-%m-%d"))


        


han = HanyoerehOpinion()
joongang = JoongangOpinion()
Keco = KoreaEconomicOpinion()
han.start()
joongang.start()
Keco.start()


