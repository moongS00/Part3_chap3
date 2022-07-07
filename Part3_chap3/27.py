'''
병합 정렬
     : 자료구조를 분할하고 각각 분할된 자료구조를 정렬하면서 병합
앞의 정렬 방법들보다 속도가 빠름
재귀함수를 사용
'''
# 선생님 풀이, 1도 이해 안됨....

def mSort(ns):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    leftNums = mSort(ns[0:midIdx])
    rightNums = mSort(ns[midIdx:len(ns)])

    print(f'midIdx : {midIdx}')
    print(f'leftNums : {leftNums}')
    print(f'rightNums : {rightNums}')

    mergeNums = []
    leftIdx = 0
    rightIdx = 0

    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if leftNums[leftIdx] < rightNums[rightIdx]:
            mergeNums.append(leftNums[leftIdx])
            print(f'if:leftNums[{leftIdx}]:{leftNums[leftIdx]},rightNums[{rightIdx}]:{rightNums[rightIdx]}, mergeNums:{mergeNums}')
            leftIdx += 1

        else:
            mergeNums.append(rightNums[rightIdx])
            print(f'else:leftNums[{leftIdx}]:{leftNums[leftIdx]},rightNums[{rightIdx}]:{rightNums[rightIdx]}, mergeNums:{mergeNums}')
            rightIdx += 1


    mergeNums = mergeNums + leftNums[leftIdx:]
    mergeNums = mergeNums + rightNums[rightIdx:]
    print(f'mergeNums : {mergeNums}')
    print()

    return mergeNums



nums = [8, 1, 4, 3, 2, 12]

print(f'mSort(nums) : {mSort(nums)}')