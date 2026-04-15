
def solve(N, parent):
    import sys
    sys.setrecursionlimit(10**7)

    # Build tree
    children = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        p = parent[i - 1]
        if p != 0:
            children[p].append(i)

    dp0 = [0] * (N + 1)
    dp1 = [0] * (N + 1)

    def dfs(u):
        for v in children[u]:
            dfs(v)

        child_vals = [dp1[v] for v in children[u]]
        total = sum(child_vals)

        # dp1[u]: parent is included
        dp1[u] = max(u, total)

        # dp0[u]: parent is not included (u is root of component)
        best = u                       # no children
        if child_vals:
            best = max(best, u + max(child_vals))  # exactly one child
        if len(child_vals) >= 2:
            best = max(best, total)   # two or more children

        dp0[u] = best

    # Rooted at city 1 as given
    dfs(1)

    # Maximum achievable strength
    return max(dp0[1:])


# The Input code we need to past to use above // Many times platform gives -

# -------- INPUT HANDLING --------
T = int(input())

for _ in range(T):
    N = int(input())
    parent = list(map(int, input().split()))
    print(solve(N, parent))


'''

Sample input

1
5
0 5 5 1 4

Output
9


test Case 2 :-

Input : -

2 
7 
0 4 1 1 7 4 3
7
0 6 7 5 1 1 1

Output :-

15
18

'''