import requests

heroes_list=['Hulk', 'Captain America', 'Thanos']
Token = '2619421814940190'
hero_int = 0
result = None


def get_hero_id (hero):
    url = 'https://superheroapi.com/api/2619421814940190/'
    resp = requests.get(url+'search/'+ hero)
    
    return resp.json()['results'][0]['id']

def get_hero_intelligence(hero_id):
    url = 'https://superheroapi.com/api/2619421814940190/'
    resp = requests.get(url + hero_id +'/powerstats')
    return resp.json()['intelligence']


if __name__ == '__main__':
    for hero in heroes_list:
        res_int = int(get_hero_intelligence(get_hero_id(hero)))
        if res_int > hero_int:
            result = hero
            hero_int = res_int
    print (f'The most intelligence hero is {result}')