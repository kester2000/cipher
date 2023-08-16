import pinyin


def inside(a, b, mp):
    return a in mp and b in mp and any(mp[a] == mp[b][i:i+len(mp[a])] for i in range(len(mp[b])-len(mp[a])+1))


with open('poetrys.txt', 'r', encoding='utf-8') as f:
    poetrys = f.read().split()
with open('chinexe_split.txt', 'r', encoding='utf-8') as f:
    chinexe_split = eval(f.read())

for p in poetrys:
    if len(p) == 7 and p[6] == '风' \
            and pinyin.get(p[3], format='strip') == 'fan' \
            and inside('化', p[4], chinexe_split):
        print(p)
