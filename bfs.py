#Author: Talent Koronya
#Purpose: Asssignment 20 Map part 3
#Date: 15/11/2023

from collections import deque

def bfs(start_vertex,goal_vertex):
    frontier = deque()
    b_pt = {}

    frontier.append(start_vertex)
    b_pt[start_vertex] = None

    while goal_vertex not in b_pt and len(frontier) > 0:
        u = frontier.popleft()
        for v in u.adj_list:
            if v not in b_pt:
                frontier.append(v)
                b_pt[v] = u


    path = []
    c = goal_vertex

    while c!= None:
        path.append(c)
        c = b_pt[c]

    return path
