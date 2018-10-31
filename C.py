"""
There are n candy boxes in front of Tania. The boxes are arranged in a row from left to right, numbered from 1 to n. 
The i-th box contains ri candies, candies have the color ci (the color can take one of three values — red, green, or blue). 
All candies inside a single box have the same color (and it is equal to ci).
Initially, Tanya is next to the box number s. Tanya can move to the neighbor box (that is, with a number that differs by one) or 
eat candies in the current box. Tanya eats candies instantly, but the movement takes one second.
If Tanya eats candies from the box, then the box itself remains in place, but there is no more candies in it. 
In other words, Tanya always eats all the candies from the box and candies in the boxes are not refilled.
It is known that Tanya cannot eat candies of the same color one after another 
(that is, the colors of candies in two consecutive boxes from which she eats candies are always different). 
In addition, Tanya's appetite is constantly growing, so in each next box from which she eats candies, 
there should be strictly more candies than in the previous one.
Note that for the first box from which Tanya will eat candies, there are no restrictions on the color and number of candies.
Tanya wants to eat at least k candies. What is the minimum number of seconds she will need? 
Remember that she eats candies instantly, and time is spent only on movements.

Input
The first line contains three integers n, s and k (1≤n≤50, 1≤s≤n, 1≤k≤2000) — number of the boxes, 
initial position of Tanya and lower bound on number of candies to eat. 
The following line contains n integers ri (1≤ri≤50) — numbers of candies in the boxes. 
The third line contains sequence of n letters 'R', 'G' and 'B', meaning the colors of candies in the correspondent boxes 
('R' for red, 'G' for green, 'B' for blue). 
Recall that each box contains candies of only one color. The third line contains no spaces.

Output
Print minimal number of seconds to eat at least k candies. If solution doesn't exist, print "-1".
"""
INF = 1e10
max_n = 50
max_k = 2000
def main():
    n, s, k = map(int, input().split())
    s -= 1
    buf = ['']*(max_n + 1)
    dp = [[0 for i in range(max_n + 1)] for j in range(max_k)] 
    r = list(map(int, input().split()))
    c = input()
    answer = INF
    for i in range(len(c)):
        buf[i] = c[i]
    for i in range(k, -1, -1):
        for j in range(n):
            dp[i][j] = INF
    for j in range(n):
        value = abs(j - s)
        if k - r[j] <= 0:
            answer = min(answer, value)
        else:
            dp[k - r[j]][j] = value
    for i in range(k, 0, -1):
        for j in range(n):
            if dp[i][j] < INF:
                for l in range(n):
                    if buf[j] != buf[l] and r[j] < r[l]:
                        value = dp[i][j] + abs(j - l)
                        if i - r[l] <= 0:
                            answer = min(answer, value)
                        else:
                            dp[i - r[l]][l] = min(dp[i - r[l]][l], value)
    if answer == INF:
        print(-1)
        return
    print(answer)

if __name__=="__main__":
    main()
