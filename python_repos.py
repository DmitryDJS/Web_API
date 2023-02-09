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

# Analysis first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print("\nВыбран информация из первого репозитория:")
print('Имя:', response_dict['name'])
print('Владелиц:', response_dict['owner']['login'])
print('Звезды:', response_dict['stargazers_count'])
print('Репозиторий:', response_dict['html_url'])
print('Создание:', response_dict['created_at'])
print('Обновление:', response_dict['updated_at'])
print('Описание:', response_dict['description'])