""" main.py """

# Libraries
import requests
from bs4 import BeautifulSoup as bf
import schedule
import time

# Parameters
from parameters import url, headers, interval

def search_job():
    response = requests.get(url= url,headers= headers)
    html = bf(response.text, 'html.parser')

    for item in html.select('.project-item'):
        
        time = item.select_one('.project-header strong').text
        title = item.select_one('.project-title span').text
        price = item.select_one('.budget span').text
        abstract = item.select_one('.project-details').text
        #if ('minuto' in time) or ('Agora' in time):
        print("\n",time)
        print(title," => ",price,abstract)
        print("_"*120)
            
schedule.every(interval).minutes.do(search_job)

if __name__ == '__main__':
    search_job()
    while 1:
      schedule.run_pending()
      time.sleep(1)