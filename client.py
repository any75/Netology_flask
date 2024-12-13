import requests
base_url = 'http://127.0.0.1:5000/adv'
create_ad_for_adv = [
    {'title': 'Продаю телефон', 
    'description': 'б/у телефон отдам недорого',
    'date': '13.12.2024',
    'name': 'Svetlana'},
    {'title': 'Меняю телефон', 
    'description': 'на айфон 16',
    'date': '12.12.2024',
    'name': 'Olga'}

]
for i in create_ad_for_adv:
    response_post = requests.post(base_url, json = i)
response_get = requests.get(base_url)
id_ad = 1
response_delete = requests.delete(f'{base_url}/{id_ad}')

