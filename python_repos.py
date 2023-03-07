import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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

names, stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


# building a visualization.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=50, show_legend=False)
chart.title = 'Самые звездные Python проекты на GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')



