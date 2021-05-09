import requests
from bs4 import BeautifulSoup


URL = "https://inshorts.com/en/read"
page = requests.get(URL)


soup = BeautifulSoup(page.content,'html.parser')

results = soup.find_all(itemprop='headline')
result_body = soup.find_all(itemprop = 'articleBody')
length = len(results)
# print(results)
news = {}
for i in range(length):
    # print(result.text, end='\n'*2)
    # news.append(result.text)
    # news[results[i].text] = result_body[i].text
    news[i] = (results[i].text,result_body[i].text)
i=0
# for result in news:
#     print("{}: {} \n".format(i,result))
#     i= i+1
n = input('How many news do you want? ')
while(next!='q'):
    for i in range(i,i+int(n)):
        print("{}: {} \n".format(i+1,news[i][0]))
    next = input('Press y for more news otherwise press q: ')
    i = i+1
    # if(int(next)>0 and int(next)<26):
    while(int(next)>0 and int(next)<26):
        print("{} :".format(news[int(next)-1][0]))
        print(news[int(next)-1][1])
        next = input('Press y for more news otherwise press q: ')
        if(int(next)<=0 or int(next)>=26):
            break



# for key,value in news.items():
#     print(key,end = '\n')


