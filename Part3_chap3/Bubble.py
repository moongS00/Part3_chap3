# 버블정렬 (실습)

# 새 학년이 되어 학급에 20명의 새로운 학생들이 모였다. 학생들을 키 순서대로 줄세워보자.
# 키는 랜덤으로 170-185 사이로 생성한다.

import copy

def bubbleSort(ns, deepCopy = True):

    if deepCopy:
        cns = copy.copy(ns)  #깊은 복사

    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j+1]:
                cns[j], cns[j+1] = cns[j+1], cns[j]

    return cns
