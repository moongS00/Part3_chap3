# 퀵 정렬 (실습)
'''
1-100사이 난수 10개를 생성해
병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
&
모율에 오름차순과 내림차순 옵션 추가
'''

def qSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2  #기준값 선정
    midVal = ns[midIdx]

    smallNums = []
    sameNums = []
    bigNums = []

    if asc:
        for n in ns:
            if n < midVal:
                smallNums.append(n)

            elif n == midVal:
                sameNums.append(n)

            else:
                bigNums.append(n)
    else:
        for n in ns:
            if n > midVal:
                smallNums.append(n)

            elif n == midVal:
                sameNums.append(n)

            else:
                bigNums.append(n)


    return qSort(smallNums, asc=asc) + sameNums + qSort(bigNums, asc=asc)

import random
nums = random.sample(range(1, 100), 10)
print(f'정렬 전 : {nums}')
print(f'오름차순 정렬 후 : {qSort(nums)}')
print(f'내림차순 정렬 후 : {qSort(nums, asc=False)}')