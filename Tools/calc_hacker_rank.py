import requests


def get_score(user):
    user_rank_url = "https://www.hackerrank.com/rest/hackers/%s/scores_elo" % user

    result = requests.get(user_rank_url)
    user_score_data = result.json()

    python_user_data = [s for s in user_score_data if s['name'] == 'Python'].pop()
    user_score = python_user_data['practice']['score']
    return user_score


def get_username(user_url):
    return user_url.split('/')[-1]


users = [
    "https://www.hackerrank.com/nicke1ton",
    "https://www.hackerrank.com/rajmondluma",
    "https://www.hackerrank.com/bdynamite",
    "https://www.hackerrank.com/taya_skachkova",
    "https://www.hackerrank.com/nermohin",
    "https://www.hackerrank.com/otche_0",
    "https://www.hackerrank.com/maxim_7",
    "https://www.hackerrank.com/kataev_sm",
    "https://www.hackerrank.com/kuzinasv",
    "https://www.hackerrank.com/alexandra_sam",
    "https://www.hackerrank.com/Desyatov_V",
    "https://www.hackerrank.com/rudestar"
]

result = []
for user in users:
    user_name = get_username(user)
    score = get_score(user_name)
    result.append((user_name, score))

result.sort(key=lambda x: x[1], reverse=True)

for user_name, score in result:
    print("%s: %s Points" % (user_name, score))
