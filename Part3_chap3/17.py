'''
최빈값
'''

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
print(f'nums : {nums}')

def getMaxNum(nums):
    maxNum = nums[0]
    maxIdx = 0

    for idx, i in enumerate(nums):
        if maxNum < i:
            maxNum = i
            maxIdx = idx

    return maxNum, maxIdx

mn = getMaxNum(nums)[0]
idxs = [0 for i in range(mn+1)]

for n in nums:
    idxs[n] += 1

print(f'idxs : {idxs}')

mi = getMaxNum(idxs)
print(f'최빈값 : {mi[1]}, 횟수 : {mi[0]}')
