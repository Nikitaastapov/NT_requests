import requests
import datetime
import time


def get_today():
    today = datetime.date.today()
    tod_date = int((time.mktime(today.timetuple())))
    # print(tod_date)
    return tod_date

def get_past_day():
    past_date = datetime.date.today()-datetime.timedelta(days=2.0)
    past_date = int((time.mktime(past_date.timetuple())))
    # print(past_date)
    return past_date

def get_file():
    link = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': get_past_day(), 'todate': get_today(), 'tagged': 'Python', 'order': 'desc','site': 'stackoverflow', 'sort': 'creation', 'pagesize': 100}
    headers = {'Accept-Encoding': 'GZIP'}
    response = requests.get(link, headers = headers, params=params)
    print(response)
    return response.json()

def get_list():
    for items in get_file()['items']:
        print (f" - {items['title']}")
    

if __name__ == '__main__':
    get_list()
    

