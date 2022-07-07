'''
퀵 정렬
    : 기준값 보다 작은 값과 큰 값을 분리한 후 다시 합친다
재귀함수 사용
'''
# 선생님 풀이

def qSort(ns):
    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2  #기준값 선정
    midVal = ns[midIdx]

    smallNums = []
    sameNums = []
    bigNums = []

    for n in ns:
        if n < midVal:
            smallNums.append(n)

        elif n == midVal:
            sameNums.append(n)

        else:
            bigNums.append(n)


    return qSort(smallNums) + sameNums + qSort(bigNums)

nums = [8, 1, 4, 3, 2, 5, 4, 10, 6, 8]
print(f'정렬 전 : {nums}')
print(f'정렬 후 : {qSort(nums)}')