# 최빈값(실습)
# 학생 100명의 점수 분포 나타내기
# 선생님 풀이

class MaxAlgorith:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxIdx = 0

    def setMaxNumIdx(self):
        self.maxNum = self.nums[0]
        self.maxIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxIdx = i

    def getMaxNum(self):
        return self.maxNum

    def getMaxIdx(self):
        return self.maxIdx


import random
scores = []

for i in range(100):
    rn = random.randint(71, 100)
    if rn != 100:
        rn = rn - (rn % 5)
    scores.append(rn)

print(f'scores : {scores}')
print(f'scores length: {len(scores)}')

#최댓값 알고리즘
maxAlo = MaxAlgorith(scores)
maxAlo.setMaxNumIdx()

maxNum = maxAlo.getMaxNum()
print(f'maxNum : {maxNum}')

maxIdx = maxAlo.getMaxIdx()
print(f'maxIdx : {maxIdx}')

#인덱스 리스트 생성
indxs = [0 for i in range(maxNum + 1)]
print(f'indxs : {indxs}')
print(f'indxs length: {len(indxs)}')

#인덱스 리스트에 빈도 저장
for n in scores:
    indxs[n] += 1
print(f'indxs : {indxs}')

#빈도 출력
n = 1
while True:
    maxAlo = MaxAlgorith(indxs)
    maxAlo.setMaxNumIdx()
    maxNum = maxAlo.getMaxNum()
    maxIdx = maxAlo.getMaxIdx()

    if maxNum == 0:
        break

    print(f'{n}. {maxIdx}빈도수 : {maxNum}\t', end='')
    print('+' * maxNum)

    indxs[maxIdx] = 0   # 다음 빈도수들도 출력하기 위해

    n += 1