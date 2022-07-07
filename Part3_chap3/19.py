'''
근삿값
    : 특정 값에 가장 가까운 값
'''
import random
nums = random.sample(range(0, 50), 20)
print(f'nums : {nums}')

inNum = int(input('input number : '))
print(f'inNum : {inNum}')

nearNum = 0   # 입력된 숫자와 차이가 가장 큰 숫자
minNum = 50   # 입력된 숫자와의 차이값. 숫자가 많은 경우엔 최댓값 알고리즘 사용해서 초기화 하기

for n in nums:
    absNum = abs(n - inNum)

    if absNum < minNum:
        minNum = absNum
        nearNum = n

print(f'nearNum : {nearNum}')
