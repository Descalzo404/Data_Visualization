import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Makes an API call and stores the answer
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code",r.status_code)

#Stores the API response in a variable
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

#Explores the information about the repositories
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : repo_dict['description'],
        'xlink' : repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

#Creates the visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('introduction_to_API/python_repos.svg')
