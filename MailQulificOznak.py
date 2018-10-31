import sys
from collections import deque
input = sys.stdin.readline
out = sys.stdout

def main():
    n = int(input())
    a = list(map(int, input().split()))
    graph = {i + 1:set() for i in range(n)}
    for i in range(n - 1):
        graph[a[i]].add(i + 2)
        graph[i + 2].add(a[i])
    start_vertex = 1
    end_vertex = n
    distances = [None]*(n + 1)
    parents = [None]*(n + 1)
    distances[start_vertex] = 0
    queue = deque([start_vertex])
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                parents[neigh_v] = cur_v
                distances[neigh_v] = distances[cur_v] + 1
                queue.append(neigh_v)
    path = [end_vertex]
    parent = parents[end_vertex]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]
    for p in path[::-1]:
        out.write(str(p) + ' ')
    
if __name__=="__main__":
    main()
