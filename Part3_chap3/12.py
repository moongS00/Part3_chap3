# 선택정렬 (실습)
# 선택정렬 알고리즘을 이용해 학생 20명의 시험점수를 오름차순, 내림차순으로 정렬하는 알고리즘 만들기
# 시험 점수는 50-100 사이

def sortNumber(ns, asc=True):
    if asc:
        for i in range(len(ns) - 1):
            minIdx = i

            for j in range(i+1, len(ns)):
                if ns[minIdx] > ns[j]:
                    minIdx = j

            ns[i], ns[minIdx] = ns[minIdx], ns[i]

    else:
        for i in range(len(ns) - 1):
            minIdx = i

            for j in range(i + 1, len(ns)):
                if ns[minIdx] < ns[j]:
                    minIdx = j

            ns[i], ns[minIdx] = ns[minIdx], ns[i]


    return ns

import random
import copy

scores = random.sample(range(50, 101), 20)
print(f'scores : {scores}')
print(f'scores length : {len(scores)}')
res1 = sortNumber(copy.deepcopy(scores))
print(f'result(ASC) : {res1}')
res2 = sortNumber(copy.deepcopy(scores),  asc=False)
print(f'result(DESC) : {res2}')
