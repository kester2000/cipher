import pinyin

with open('poetrys.txt', 'r', encoding='utf-8') as f:
    poetrys = f.read().split()
with open('chinexe_split.txt', 'r', encoding='utf-8') as f:
    chinexe_split = eval(f.read())
# l = [k for k in d if '亻化右' in ''.join(d[k])]
for p in poetrys:
    if len(p) == 7 and p[6] == '风' \
            and pinyin.get(p, ' ', 'strip').split()[3] == 'fan' \
            and p[4] in chinexe_split and '亻化右' in ''.join(chinexe_split[p[4]]):
        print(p)
