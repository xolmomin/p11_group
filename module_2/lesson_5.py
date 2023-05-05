# import os
# import json
#
# if not (os.path.exists('products.json') and os.path.isfile('products.json')):
#     with open('products.json', 'w') as f:
#         f.write('[]')
#
# with open('products.json', 'r') as f:
#     products: list[dict] = json.load(f)
#
# while True:
#     menu = '''
#     1.add product
#     2.exit
#     '''
#     key = input(menu)
#
#     if key == '1':
#         name, price, quantity = input('Productni kiriting (name, price, quantity): ').split()
#         price, quantity = int(price), int(quantity)
#         products.append({
#             'name': name,
#             'price': price,
#             'quantity': quantity
#         })
#
#     elif key == '2':
#         break
#
# with open('products.json', 'w') as f:
#     json.dump(products, f, indent=2)
#
#
# from collections import defaultdict
#
# course = defaultdict(list)
#
# course['foundation'].append('f1')
# course['python'].append('python group 1')
# course['python'].append('python group 2')
#
#
# print(course)
#
# from collections import defaultdict
#
# import httpx
# import json
#
# url = 'https://www.boredapi.com/api/activity'
#
# activities: dict = defaultdict(list)
#     # 'recreational': [
#     #     {
#     #         "activity": "Start a collection",
#     #         "participants": 1,
#     #         "price": 0,
#     #         "link": "",
#     #         "key": "1718657",
#     #         "accessibility": 0.5
#     #     },
#     #     {
#     #         "activity": "Try a food you don't like",
#     #         "participants": 1,
#     #         "price": 0.1,
#     #         "link": "",
#     #         "key": "6693574",
#     #         "accessibility": 0.05
#     #     }
#     # ],
#     # 'busywork': [
#     #     {
#     #         "activity": "Draft your living will",
#     #         "participants": 1,
#     #         "price": 0,
#     #         "link": "https://www.investopedia.com/terms/l/livingwill.asp",
#     #         "key": "2360432",
#     #         "accessibility": 0.5
#     #     }
#     # ]
#
#
# for _ in range(20):
#     response = httpx.get(url).json()
#     activities[response.pop('type')].append(response)
#
# data = [{'type': key, 'data': value} for key, value in activities.items()]
#
# with open('activities.json', 'w') as f:
#     json.dump(data, f, indent=2)


# from collections import defaultdict
#
# import httpx
# import json
#
# url = 'https://api.first.org/data/v1/countries'
#
# regions = defaultdict(list)
# response = httpx.get(url).json()
# for k, value in response['data'].items():
#     regions[value['region']].append(value['country'])
#
#
# with open('countries.json', 'w') as f:
#     json.dump(regions, f, indent=2)

'''
3ta project (restaran, magazin, oquv markaz)

pdp
botirjon

student

1. kursga qoshilish
2. kursdan chiqish
3. kusrlarni korish
4. exit


mentor
1. kurs qoshish
2. kursni olib tashash
3. ozi qoshgan kurslarni korish
4. exit

1. login
    -username
    -password
2. register
    -ism
    -username
    -phone
    -password
    -is_student

oquvchilar
course
mentor


----------------------------------------------------------------

magazin
restaranga oxshash + (product soni)


----------------------------------------------------------------
restaran

login
ovqat qoshish
ichimlik qoshish
hisobot


botirjon01
-mijoz

1. ovqatga buyurtma
2. oldingi buyurtmalari
3.exit

'''
