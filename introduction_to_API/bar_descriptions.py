import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['Project 1', 'Project 2', 'Project 3']

plot_dicts = [
    {'value' : 12000, 'label' : "Descripition of Project 1"},
    {'value' : 11000, 'label' : "Descripition of Project 2"},
    {'value' : 10000, 'label' : "Descripition of Project 3"},
]

chart.add('', plot_dicts)
chart.render_to_file('introduction_to_API/bar_description.svg')