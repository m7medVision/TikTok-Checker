import random
import string
import requests
def link(User):
    headers = {
    'authority': 'www.tiktok.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                                                }

    r = requests.get(f'https://www.tiktok.com/@{User}', headers=headers)
    if r.status_code == 404: 
        print('Good ',User)
        with open('good.txt','a') as f:
            f.write(User+'\n')
    else : print('Bad ',User)
def checker():
    while True:
        letters = string.ascii_lowercase + string.digits
        User= ''.join(random.choice(letters) for i in range(6))
        link(User)
checker()
