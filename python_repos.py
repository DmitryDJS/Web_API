import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Статус код:", r.status_code)

# Save response API
response_dict = r.json()

print("Общее количество репозиториев:", response_dict['total_count'])

# Analysis of repository information
repo_dicts = response_dict['items']
print("Возвращенные репозитории:", len(repo_dicts))
print("Выбранная информация о каждом репозитории.")

"""
# Analysis first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print("\nВыбрана информация из первого случайного  репозитория:")
"""
i = 1
for repo_dict in repo_dicts:
    print("********* " + str(i) + " ***********")
    print('Имя:', repo_dict['name'])
    print('Владелец:', repo_dict['owner']['login'])
    print('Звезды:', repo_dict['stargazers_count'])
    print('Репозиторий:', repo_dict['html_url'])
    print('Создание:', repo_dict['created_at'])
    print('Обновление:', repo_dict['updated_at'])
    print('Описание:', repo_dict['description'])
    print("************************")
    i += 1
