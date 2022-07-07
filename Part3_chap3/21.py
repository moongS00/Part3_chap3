'''
평균
'''

# 50-90 사이 수들의 평균
import random
nums = random.sample(range(0, 100), 30)
print(f'nums : {nums}')

total = 0
cnt = 0
for n in nums:
    if n >= 50 and n <= 90:
        total += n
        cnt += 1
avg = round(total / cnt, 1)
print(f'50-90 사이 수들의 평균 : {avg}')
print()

# 정수들의 평균
nums2 = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.15, 1, 11, 12.7]

sums = 0
count = 0

for n in nums2:
    if n == int(n):
        sums += n
        count += 1

intAvg = round(sums / count, 2)
print(f'정수들의 평균 : {intAvg}')


# 실수들의 평균
nums2 = [4, 5.12, 0, 5, 7.34, 9.1, 9, 3, 3.15, 1, 11, 12.7]

sums = 0
count = 0

for n in nums2:
    if n != int(n):
        sums += n
        count += 1

intAvg = round(sums / count, 2)
print(f'실수들의 평균 : {intAvg}')