with open('words.txt', encoding='utf-8') as f:
    words = f.readlines()

words = [w.strip() for w in words]
words = [w for w in words if w.isalpha()]
words = [w.lower() for w in words]


def get_shape(word):
    ans = ''
    ind = 97
    dic = {}
    for c in word:
        if c not in dic:
            dic[c] = ind
            ind += 1
        ans += chr(dic[c])
    return ans

# print(get_shape('additional'))
shape = 'abbcdcefag'
words = [w for w in words if len(w) == len(shape)]
words = [w for w in words if get_shape(w) == shape]
print(words)
