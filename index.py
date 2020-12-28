import requests
from bs4 import BeautifulSoup
import time


# j, d, page 순서
job = {"히어로" : [1, 12, 28], "팔라딘" : [1, 22, 18], "다크나이트" : [1, 32, 18] , 
       "불독" : [2, 12, 73], "썬콜" : [2, 22, 37], "비숍" : [2, 32, 63], 
       "보마" : [3, 12, 13] , "신궁" : [3, 22, 6], "패파" : [3, 32, 91], 
       "나로" : [4, 12, 64] , "섀도어" : [4, 22, 48], "듀블" : [4, 34, 50], 
       "바이퍼" : [5, 12, 30] , "캡틴" : [5, 22, 6], "캐슈" : [5, 32, 33],
       "소마" : [6, 11, 17] , "플위" : [6, 12, 20], "윈브" : [6, 13, 32],"나워" : [6, 14, 8] , "스커" : [6, 15, 7], "미하일" : [6, 16, 3],
       "아란" : [7, -1, 27],
       "에반" : [8, -1, 24] , 
       "배메" : [10, 32, 7] , "와헌" : [10, 33, 9], "메카" : [10, 35, 8],"데슬" : [10, 31, 18] , "데벤" : [10, 131, 22], "제논" : [10, 36, 21], "블래" : [10, 37, 6],
       "메르" : [11, -1, 21] ,
       "팬텀" : [12, -1, 38] ,
       "루미" : [13, -1, 17] ,
       "카이저" : [14, -1, 12] ,
       "엔버" : [15, -1, 41] ,
       "제로" : [17, -1, 35] ,
       "은월" : [18, -1, 45] ,
       "키네" : [20, -1, 16] ,
       "카데나" : [21, -1, 15] ,
       "일리움" : [22, -1, 4] ,
       "아크" : [23, -1, 35] ,
       "호영" : [24, -1, 7] ,
       "아델" : [25, -1, 33] ,
      }
# 유저 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

FIND_LEVEL = 260

def page_serch(val):
    
    j = val[0]
    d = val[1]
    page_num = val[2]
    re_page_num = page_num
    
    while page_num <= 1000:
        print(page_num, "페이지를 탐색 합니다.")
        url = 'https://maplestory.nexon.com/Ranking/World/Total?page=' + str(page_num) + '&j=' + str(j) + '&d=' + str(d)
        # User 설정
        res = requests.get(url, headers = headers)
        # res.content 주의
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # span.item_title 정보를 선택
        data = soup.select('.rank_table > tbody > tr')
              
        if int(str(data[9].select('td')[2])[7:10]) >= FIND_LEVEL:
            re_page_num = page_num
            page_num += 5
        else:
            i = 8
            while i >= 0:
                if int(str(data[i].select('td')[2])[7:10]) >= FIND_LEVEL:
                    print(page_num)
                    print(int(data[i].select('td > p')[0].get_text()))
                    page_num = 99999
                    break
                i -= 1
            if (page_num - 1) != re_page_num:
                page_num -= 1
            else:
                print(int(data[0].select('td > p')[0].get_text())-1)
                page_num = 99999
                
        time.sleep(1)

find_job = input("찾고 싶은 직업이 있다면 입력 (없다면 '없음' 입력): ")
if find_job == '없음':
    for key, val in job.items():
        print("직업 :" + key)

        page_serch(val)
else:
    print("직업 :" + find_job)
    print(job[find_job])
    page_serch(job[find_job])
    

