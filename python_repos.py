import pygal
import requests

from config import my_config, my_style
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


names, stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


# building a visualization.
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Самые звездные Python проекты на GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')



