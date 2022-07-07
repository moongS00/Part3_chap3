# 근삿값 (실습)
# 시험 점수를 입력하면 평균 점수에 따라 학점 출력
# 95에 근사 = A // 85에 근사 = B // 75에 근사 = C // 65에 근사 = D // 55에 근사 = F
# 선생님 풀이

ks = int(input('kor score : '))
es = int(input('eng score : '))
ms = int(input('mat score : '))
ss = int(input('sci score : '))
hs = int(input('his score : '))

totalScore = ks + es + ms + ss + hs
avgScore = round((totalScore / 5), 1)
print(f'totalScore : {totalScore}')
print(f'avgScore : {avgScore}')

def getNearNum(an):
    bascores = [95, 85, 75, 65, 55]
    nearNum = 0
    minNum = 100

    for n in bascores:
        absNum = abs(n - an)

        if absNum < minNum:
            minNum = absNum
            nearNum = n

    if nearNum == 95:
        return "A"
    elif nearNum == 85:
        return "B"
    elif nearNum == 75:
        return "C"
    elif nearNum == 65:
        return "D"
    elif nearNum == 55:
        return "F"




print(f'grade : {getNearNum(avgScore)}')