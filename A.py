"""
Once upon a time there was only one router in the well-known company Bmail. Years went by and over time new routers were purchased. 
Every time they bought a new router, they connected it to one of the routers bought before it. 
You are given the values pi — the index of the router to which the i-th router was connected after being purchased (pi<i).
There are nn routers in Boogle in total now. Print the sequence of routers on the path from the first to the nn-th router.
Input
The first line contains integer number n (2≤n≤200000) — the number of the routers. 
The following line contains n−1 integers p2,p3,…,pn (1≤pi<i), where pi is equal to index of the router to 
which the i-th was connected after purchase.
Output
Print the path from the 1-st to the n-th router. It starts with 1 and ends with n. 
All the elements in the path should be distinct.
"""

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
