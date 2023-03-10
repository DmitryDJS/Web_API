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


names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)


# building a visualization.
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Самые звездные Python проекты на GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')



