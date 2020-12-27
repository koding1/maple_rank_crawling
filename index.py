import requests
from bs4 import BeautifulSoup
import time


# j, d, page 순서
job = {"히어로" : [1, 12, 28], "팔라딘" : [1, 22, 18], "다크나이트" : [1, 32, 18] , "불독" : [2, 12, 73], "썬콜" : [2, 22, 18], "비숍" : [2, 32, 18]}
# 유저 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

FIND_LEVEL = 260


def page_serch(val):
    
    j = val[0]
    d = val[1]
    page_num = val[2]
    
    while page_num <= 200:
        print(page_num, "페이지를 탐색 합니다.")
        # 카이저 랭킹 페이지 (1)
        url = 'https://maplestory.nexon.com/Ranking/World/Total?page=' + str(page_num) + '&j=' + str(j) + '&d=' + str(d)
        # User 설정
        res = requests.get(url, headers = headers)
        # res.content 주의
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # span.item_title 정보를 선택
        data = soup.select('.rank_table > tbody > tr')
              
        if int(str(data[9].select('td')[2])[7:10]) >= FIND_LEVEL:
            page_num += 5
        else:
            i = 8
            while i >= 0:
                if int(str(data[i].select('td')[2])[7:10]) >= FIND_LEVEL:
                    print(data[i].select('td > p')[0].get_text())
                    page_num = 99999
                    break
                i -= 1
            page_num -= 1
        time.sleep(1)

for key, val in job.items():
    print("직업 :" + key)
    
    page_serch(val)

