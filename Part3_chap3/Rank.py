# 순위 (실습)
import random
# 학급 학생(20명)들의 중간고사와 기말고사 성적을 이용해서 각각의 순위를 구하고
# 중간고사 대비 기말고사 순위 변화(편차)를 출력 해라 (시험 성적은 난수를 이용)
# 선생님 풀이

class RankDeviation:

    def __init__(self, mss, ess):
        self.midScores = mss
        self.midRanks = [0 for i in range(20)]
        self.endScores = ess
        self.endRanks = [0 for i in range(20)]


    def setRank(self, scores, rsnks):
        for idx, score1 in enumerate(scores):
            for score2 in scores:
                if score1 < score2:
                    rsnks[idx] += 1

    def setMidRank(self):
        self.setRank(self.midScores, self.midRanks)

    def getMidRank(self):
        return self.midRanks

    def setEndRank(self):
        self.setRank(self.endScores, self.endRanks)

    def getEndRank(self):
        return self.endRanks


    def printDeviation(self):
        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.endRanks[idx]

            if deviation > 0:
                deviation = '↑' + str(abs(deviation))

            elif deviation < 0:
                deviation = '↓' + str(abs(deviation))

            else:
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank : {mRank}, end_rank : {self.endRanks[idx]}, Deviation : {deviation}')









