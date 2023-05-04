
import os
import pinyin
from copy import deepcopy


def is_chinese(c):
    return '\u4e00' <= c <= '\u9fa5' or '\u3400' <= c <= '\u4db5'


def chinese_split(s):
    ret = []
    tmp = ''
    for c in s:
        if is_chinese(c):
            tmp += c
        elif tmp != '':
            ret.append(deepcopy(tmp))
            tmp = ''
    if tmp != '':
        ret.append(deepcopy(tmp))
        tmp = ''
    return ret


def check(s):
    if len(s) == 7:
        pys = pinyin.get(s, delimiter=' ', format='strip').split()
        if True\
                and len(pys[0]) == 2\
                and len(pys[1]) == 5 and pys[1].endswith('ng')\
                and len(pys[2]) == 4 and pys[2].endswith('ng')\
                and len(pys[3]) == 2 and pys[3].startswith('g')\
                and len(pys[4]) == 2\
                and len(pys[5]) == 4\
                and len(pys[6]) == 4 and pys[6].endswith('n')\
                and True:
            print(s)


def dfs(dir):
    if os.path.isfile(dir):
        if dir.endswith('.csv'):
            with open(dir, "r", encoding='utf-8') as f:
                s = f.read()
            sp = chinese_split(s)
            for v in sp:
                check(v)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            if s.startswith('.'):
                continue
            newDir = os.path.join(dir, s)
            dfs(newDir)

# with open('Poetry/当代.csv', "r", encoding='utf-8') as f:
#     s = f.read()


dfs('Poetry')
# print(pinyin.get('遍历', delimiter=' ', format='strip').split())
