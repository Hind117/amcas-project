# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://solarsystem.nasa.gov/asteroids-comets-and-meteors/comets/1p-halley/in-depth/")

# soup = BeautifulSoup(page.content, 'html.parser')

# # wysiwyg_content
# results = soup.find('div', class_="countdown_module")

# print(results['data-react-props'])

# mon = soup.find('span', class_="time_and_label_container")
# year = soup.find('div', class_="time_years")
# days = soup.find('div', class_="time_days")

# print(mon)
# # for res in results:
# # 	print(res['data-react-props'])


import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta

a = '2061-07-27T17:00:00.000-07:00'
date = parser.parse(a)

b = datetime.datetime.now().astimezone()



print(date)
print(b)
# print(date-b)
# start = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
# ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

diff = relativedelta(date, b)
print(diff)