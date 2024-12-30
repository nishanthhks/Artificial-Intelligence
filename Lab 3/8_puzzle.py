import heapq
import numpy as np

goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
vis = set()
q = []
path = []

def manhattan(curr):
    ans = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if goal[i][j] == curr[k][l]:
                        ans += abs(i - k) + abs(l - j)
    return ans

def moves(curr):
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            if curr[i][j] == 0:
                x = i
                y = j
                break
    poss = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    x1 = x
    y1 = y
    for pos in poss:
        x += pos[0]
        y += pos[1]
        if 0 <= x < 3 and 0 <= y < 3:
            curr1 = [row.copy() for row in curr]
            curr1[x1][y1], curr1[x][y] = curr1[x][y], curr1[x1][y1]
            tuple_curr1 = tuple(map(tuple, curr1))
            if tuple_curr1 not in vis:
                heapq.heappush(q, (manhattan(curr1), curr1))
                vis.add(tuple_curr1)
        x = x1
        y = y1

def dfs(curr):
    if curr == goal:
        path.append(curr)
        return True
    moves(curr)
    if q:
        curr = heapq.heappop(q)[1]
        if dfs(curr):
            path.append(curr)
            return True
    return False

c = [[4, 8, 3], [5, 0, 6], [1, 7, 2]]
dfs(c)
print(np.array(c))
for state in reversed(path):
    print(np.array(state))