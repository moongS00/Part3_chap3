# 순위 : 수의 크고 작음을 이용해서 수의 순서를 정하는 것
import random
nums = random.sample(range(50, 101), 20)
ranks = [0 for i in range(20)]  # 각 숫자의 rank에 대응되는 인덱스
print(f'nums : {nums}')
print(f'ranks : {ranks}')
'''
# 내 풀이 
n = 0
while n <= len(nums):
    for i in range(1, len(nums) - n):
        if nums[n] < nums[n+i]:
            ranks[n+i] += 1

        elif nums[n] > nums [n+i]:
            ranks[n] += 1

    n += 1
'''

# 선생님 풀이
for idx, num1 in enumerate(nums):
    for num2 in nums:
        if num1 < num2:
            ranks[idx] += 1

print()
print(f'nums : {nums}')
print(f'ranks : {ranks}')

for i, m in enumerate(nums):
    print(f'num : {m}, rank : {ranks[i] + 1}')


