import os
import sys
sys.path.append('..')

from team_points import *

print(os.getcwd())

print(stats_header)
print('\n')

vancouver = team_data('Vancouver Canucks')

print(vancouver)
