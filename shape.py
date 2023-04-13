with open('words/words.txt', encoding='utf-8') as f:
    words = f.readlines()

words = [w.strip() for w in words]
words = [w for w in words if w.isalpha()]
words = [w.lower() for w in words]


def get_shape(word):
    ans = ''
    ind = 1
    dic = {}
    for c in word:
        if c not in dic:
            dic[c] = ind
            ind += 1
        ans += str(dic[c])
    return ans


words = [w for w in words if get_shape(w) == '112334']
print(words)
