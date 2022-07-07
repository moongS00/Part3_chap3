# 평균(실습)
# 점수의 평균을 구하고 순위를 정하는 알고리즘

scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
ranks = [9.12, 8.95, 8.12, 7.90, 7.88]
print(f'ranks : {ranks}')

totalScore = 0
for s in scores:
    totalScore += s

avgScore = round(totalScore / len(scores), 2)
print(f'avgScore : {avgScore}')


for idx, sc in enumerate(ranks):
    if sc < avgScore:
        ranks.insert(idx, avgScore)
        break

print(f'ranks : {ranks}')


# 선생님 풀이

class Rank:
    def __init__(self, cs, ns):
        self.currentScores = cs
        self.newScore = ns

    def setScore(self):

        nearIdx = 0
        nearScore = 0
        minNum = 10.0

        for i, s in enumerate(self.currentScores):
            absNum = abs(self.newScore - s)

            if absNum < minNum:
                minNum = absNum
                nearIdx = i
                nearScore = s

        if self.newScore >= self.currentScores[nearIdx]:
            for i in range(len(self.currentScores) -1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i-1]   # 왜 -인가? + 아닌가?

            self.currentScores[nearIdx] = self.newScore
        else:
            for i in range(len(self.currentScores) -1, nearIdx, -1):
                self.currentScores[i] = self.currentScores[i+1]

            self.currentScores[nearIdx] = self.newScore


    def getRes(self):
        return self.currentScores
