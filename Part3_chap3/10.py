# 1-1000 사이의 난수 100개를 생성하고 , 정렬한 뒤 최대ㅛ값과 최솟값 출력
import copy
def sortAsc(list,  deepCopy = True):
    if deepCopy:
        res_asc = copy.copy(list)

    for i1 in range(1, len(res_asc)):
        i2 = i1 - 1
        cNum = res_asc[i1]

        while (res_asc[i2] > cNum) and (i2 >= 0):
            res_asc[i2 + 1] = res_asc[i2]
            i2 -= 1

        res_asc[i2 + 1] = cNum

    return res_asc

def sortDesc(list, deepCopy = True):
    if deepCopy:
        res_desc = copy.copy(list)

    for i1 in range(1, len(res_desc)):
        i2 = i1 - 1
        cNum = res_desc[i1]

        while (res_desc[i2] < cNum) and (i2 >= 0):
            res_desc[i2 + 1] = res_desc[i2]
            i2 -= 1

        res_desc[i2 + 1] = cNum

    return res_desc


import random

rNum = random.sample(range(1, 1001), 100)

print(f'정렬 전 : {rNum}')
print(f'오름차순 정렬 : {sortAsc(rNum)}')
print(f'내림차순 정렬 : {sortDesc(rNum)}')
print(f'최솟값 : {sortAsc(rNum)[0]}')
print(f'최뎃값 : {sortAsc(rNum)[len(rNum) - 1]}')

