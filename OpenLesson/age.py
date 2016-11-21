# Без даты и года
# https://vk.com/ani.kira
# https://vk.com/g.ostanina


# Дата без года
# https://vk.com/kraftchikens
# https://vk.com/elmiralin
# https://vk.com/a.mechtaeva
# https://vk.com/id35319029
# https://vk.com/miller_dina
# на основе списка друзей
# на основе даты поступления / окончания школы / вуза
# дата - на основе поздравлений, подарков

# На ком можно проверить?
# возьмём преподавателя!

import time
from collections import defaultdict

import vk

MY_LOGIN = '+79000000000'
MY_PASSWORD = 'qwerty123'

session = vk.AuthSession(
    app_id='5730932',
    user_login=MY_LOGIN,
    user_password=MY_PASSWORD)
api = vk.API(session)

# распределение возраста друзей
# распределение возраста друзей того же пола


def get_year(bdate):
    if bdate.count(".") == 2:
        return bdate[-4:]


def predict_year_by_friends(friends):
    age_frequencies = defaultdict(int)
    for friend in friends:
        if 'bdate' in friend:
            friend_year = get_year(friend['bdate'])
            if friend_year is None:
                continue
            age_frequencies[friend_year] += 1

    #pprint(sorted(list(age_frequencies.items()), key=lambda x: x[1]))
    year = int(max(age_frequencies.items(), key=lambda x: x[1])[0])
    return year


def birthday_year_by(user):
    friends = api.friends.get(user_id=user['uid'], fields=['bdate', 'sex'] )
    friends_girls = [friend for friend in friends if friend['sex'] == user['sex']]

    #year_way1 = predict_year_by_friends(friends)
    year_way2 = predict_year_by_friends(friends_girls)

    #print('Оценка по всем друзьям: %s год рождения' % year_way1)

    return year_way2

#interesting_users = ['kraftchikens', 'elmiralin', 'a.mechtaeva', 'miller_dina', 'id35319029']
interesting_users = ['kiselyovaolga']
users = api.users.get(user_ids=interesting_users, fields=['sex'])
for user, uid in zip(users, interesting_users):
    print(user)
    year = birthday_year_by(user)
    print('%s: %s год рождения' % (uid,  year))

# интересно оценить насколько наш метод рабочий!
# давайте пройдёмся по моим друзьям и посмотрим

my_friends = api.friends.get(fields = ['sex', 'bdate'])
my_friends_with_birth_date = []
for friend in my_friends:
    if 'bdate' in friend:
        friend_year = get_year(friend['bdate'])
        if friend_year is None:
            continue
        my_friends_with_birth_date.append((friend_year, friend))

right_predictions = 0
wrong_predictions = 0
effort_cost = 0

print('всего друзей: %s' % len(my_friends_with_birth_date))

for friend_year, friend in my_friends_with_birth_date:
    predicted_year = birthday_year_by(friend)
    time.sleep(0.3)
    if int(friend_year) != int(predicted_year):
        wrong_predictions += 1
        effort_cost += abs(int(friend_year)  - int(predicted_year))
        print('ошибка для https://vk.com/id{0}, предсказали {1}, но {2}'.format(friend['uid'], predicted_year, friend_year))
    else:
        print('{0} верно'.format(friend['uid']))
        right_predictions += 1

print('правильных предсказаний {0}'.format(right_predictions))
print('ошибочных предсказаний {0}'.format(wrong_predictions))

