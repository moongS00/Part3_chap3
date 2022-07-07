# 선형검색 (실습)
# 1. 리스트에서 가장 앞에 있는 숫자 7을 검색하고, 인덱스 출력
'''
nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

searchNum = 7
searchIdx = -1

n = 0
while True:
    if nums[n] == searchNum:
        searchIdx = n
        break

    n += 1

print(f'가장 앞에 있는 7 : {searchIdx}')
'''
# 2. 리스트에서 숫자 7을 모두 검색하고 각각의 위치와 검색 개수 출력
# 똑같이 했는데 실행이 안됨
nums = [4, 7, 10, 2, 4, 7, 0, 2, 7, 3, 9]

searchNum = 7
searchList = []

n2 = 0
while True:
    if nums[n2] == searchNum:
        if n2 != len(nums) - 1:
            searchList.append(n2)

        else:
            break

    n2 += 1
    if n2 == len(nums):
        break

print(f'7들의 인덱스 : {searchList}')