import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pygal.util
# creating API call and saving the answer
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

# saving API answer in variable
responce_dict = r.json()
print('Total repos: ', responce_dict['total_count'])
# handling result
repo_dicts = responce_dict['items']
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# building visualization
my_style = LS('#336699', base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=12
my_config.major_label_font_size=16
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart = pygal.Bar(style=my_style, config=my_config)
chart.title = 'Most-Starred Py Projects on Github'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('py_repos.svg')
# print('Repos returned: ', len(repo_dicts))
# print('\nSelected info bout each repo: ')
# for repo_dict in repo_dicts:
#     print('Name: ', repo_dict['name'])
#     print('Owner: ', repo_dict['owner']['login'])
#     print('Stars: ', repo_dict['stargazers_count'])
#     print('Repo: ', repo_dict['html_url'])

# repo_dict = repo_dicts[0]
# # print('\nKeys: ', len(repo_dict))
# # for key in sorted(repo_dict.keys()):
# #     print(key)
# print("\nSelected information about first repository:")
# print('Name: ',repo_dict['name'])
# print('Owner: ',repo_dict['owner']['login'])
# print('Stars: ',repo_dict['stargazers_count'])
# print('Repo: ',repo_dict['html_url'])
