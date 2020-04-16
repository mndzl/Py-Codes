import requests
from bs4 import BeautifulSoup
import mechanize
from bs4 import BeautifulSoup
import urllib3
import http.cookiejar as cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("http://eet24virtual.ddns.net/moodle/my/")
br.select_form(nr=1)
br.form['username'] = '95513580'
br.form['password'] = 'AV_eet24*95513580'
br.submit()

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

soup = BeautifulSoup(br.response(), 'html.parser')

region = soup.find(class_='block_calendar_upcoming')
tasks = region.find_all(class_='event')

if region:
    for task in tasks:
        type_task = task.find('span', class_='icon')
        type_task = type_task.img.get('title')

        title = task.a.text

        subject = task.find(class_='course').text

        date = task.find(class_='date').text

        print(type_task)
        print(title)
        print(subject)
        print(f'({date})')

        print()
else:
    print('no results found')
