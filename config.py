import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_x_guides = False
my_config.width = 1000

my_style = LS('#333366', base_style=LCS)