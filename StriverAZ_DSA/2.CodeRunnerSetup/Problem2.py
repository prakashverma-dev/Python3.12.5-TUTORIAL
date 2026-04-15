def solve(N, A):
    import math
    from collections import defaultdict

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    prev = {}
    ans = 0

    for x in A:
        cur = defaultdict(int)
        cur[x] += 1

        for g, cnt in prev.items():
            ng = math.gcd(g, x)
            cur[ng] += cnt

        for g, cnt in cur.items():
            for p in primes:
                if g % p != 0:
                    ans += cnt * p
                    break

        prev = cur

    return ans

# -------- INPUT HANDLING --------
T = int(input())

for _ in range(T):
    N = int(input())
    parent = list(map(int, input().split()))
    print(solve(N, parent))



'''

Sample Input : -

1 
4
2 4 8 3

Sample Ouput : -
26

Explantion : First line Denotes T = 1, the no of total test cases.


'''