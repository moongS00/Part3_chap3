# 병합정렬 (실습)

'''
1-100사이 난수 10개를 생성해
병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
&
모율에 오름차순과 내림차순 옵션 추가
'''


def mSort(ns, asc=True):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx], asc=asc)  # 재귀호출 할떄도 옵션이 유지되도록 한다
    rightNums = mSort(ns[midIdx:len(ns)], asc=asc)

    mergeNums = []
    leftIdx = 0
    rightIdx = 0

    mergeNums = []
    leftIdx = 0
    rightIdx = 0

    while leftIdx < len(leftNums) and rightIdx < len(rightNums):
        if asc:
            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1
        else:
            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]

    return mergeNums


import random as rd
rNums = rd.sample(range(1, 101), 10)
print(f'정렬 전 : {rNums}')
print(f'오름차순 정렬 후 : {mSort(rNums)}')
print(f'내림차순 정렬 후 : {mSort(rNums, asc=False)}')