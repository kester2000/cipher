with open('chengyu.txt', encoding='utf-8') as f:
    words = f.readlines()

words = [w.strip() for w in words]
words = [w for w in words if len(w) == 4 and w[0] == '不' and w[1] == '一']

print(len(words))
print(*words, sep='\n')
