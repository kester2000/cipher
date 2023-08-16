import random
import time


def get(word: str, ans: str) -> str:
    assert (len(word) == len(ans))
    n = len(word)
    u = [0 for _ in range(n)]
    v = [0 for _ in range(n)]
    for i in range(n):
        if ans[i] == word[i]:
            u[i] = 2
            v[i] = 2
    for i in range(n):
        for j in range(n):
            if not u[i] and not v[j] and word[i] == ans[j]:
                u[i] = 1
                v[j] = 1
    return ''.join(map(str, u))


def dfs(words, try_list):
    assert (words)
    best_cnt = 99999
    best_word = '$'
    for w in try_list:
        # print(w)
        d = {}
        for ans in words:
            if ans == w:
                continue
            s = get(w, ans)
            d[s] = d.get(s, [])+[ans]
        sum = 1  # the w itself
        for k in d:
            # print(k, d[k])
            cnt, _ = dfs(d[k], d[k])
            sum += len(d[k])*(cnt+1)
        if sum / len(words) < best_cnt:
            best_cnt = sum / len(words)
            best_word = w
    return best_cnt, best_word


with open('words.txt') as f:
    words = f.read().split()

my_word = 'basket'
other_words = [w for w in words if len(w) == len(
    my_word) and any(c1 == c2 for c1, c2 in zip(w, my_word))]

his = [
    # ('dancer', get('dancer', 'decree')),
    # ('render', get('render', 'decree')),
]

possible_words = other_words
for a, b in his:
    possible_words = [w for w in possible_words if get(a, w) == b]

print(possible_words)
print(len(possible_words))
if his:
    exp, word = dfs(possible_words, possible_words)
else:
    t0 = time.time()
    l = possible_words[:]
    random.shuffle(l)
    exp = 99999
    word = ''
    for i in l:
        e0, w0 = dfs(possible_words, [i])
        if e0 < exp:
            exp = e0
            word = w0
        if time.time() - t0 > 10:
            break
print(exp, word)