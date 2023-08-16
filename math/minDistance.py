def minDistance(w1, w2):
    m, n = len(w1), len(w2)
    if (m == 0):
        return m
    if (n == 0):
        return n
    step = [[0]*(n+1)for _ in range(m + 1)]
    for i in range(1, m+1):
        step[i][0] = i
    for j in range(1, n+1):
        step[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if w1[i-1] == w2[j-1]:
                diff = 0
            else:
                diff = 1
            step[i][j] = min(step[i-1][j-1]+diff, step[i-1]
                             [j]+1, step[i][j-1]+1)
    return step[m][n]


# s = ['precision', 'revive', 'length', 'sailors', 'external']
# s = ['planes', 'livingexpenses', 'deepdiving']
s = ['winds', 'drown']
for i, j in zip(s, s[1:]):
    print(minDistance(i, j))
