from collections import defaultdict
from pprint import pprint

import vk

MY_LOGIN = '+79000000000'
MY_PASSWORD = 'qwerty123'

session = vk.AuthSession(app_id='5730932', user_login=MY_LOGIN, user_password=MY_PASSWORD)
api = vk.API(session)

user = api.users.get(user_ids=['miller_dina']).pop()
uid = user['uid']

friends = api.friends.get(user_id=uid, fields=['bdate'])

birthdays = []

years = defaultdict(int)


def get_year(date):
    if date.count('.') == 2:
        return date[-4:]

for friend in friends:
    if 'bdate' in friend:
        year = get_year(friend['bdate'])
        if year is not None:
            years[year] += 1
            birthdays.append(year)

pprint(years)