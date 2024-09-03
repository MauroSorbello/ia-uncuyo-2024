import numpy as np
def bfs(env):
    desc = env.unwrapped.desc
    desc_str = [[cell.decode('utf-8') for cell in row] for row in desc]
    